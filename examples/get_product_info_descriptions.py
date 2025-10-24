"""
Задача: Выгрузить описания для всех товаров продавца.

Описание решения:
Будем выгружать список товаров с помощью метода product_list() пачками и,
по мере получения таких пачек, асинхронно получать описания для товаров
с помощью метода product_info_description().

Для этих целей используем очереди из модуля asyncio и будем производить
обработку по модели Производитель (producer) -> Очередь (queue) -> Потребитель (consumer).

Сделаем одного производителя для наполнения очереди необходимыми для выборки описаний
айдишниками товаров и несколько потребителей, каждый из которых будет доставать
айдишник из очереди и выгружать по нему описание, с ограничением кол-ва запросов в
секунду для каждого потребителя.
"""

import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig
from src.ozonapi.seller.schemas.products import ProductListRequest, ProductListResponse, \
    ProductInfoDescriptionRequest


# Настройки обработки, позволяющие наблюдать асинхронность выполнения логики
# Для production значение параметра product_list_limit может быть увеличено
# Общее кол-во генерируемых потребителями запросов составит consumers_amount * consumer_rate_limit в сек.
product_list_limit = 10                                     # Кол-во товаров, выгружаемых за одну итерацию
consumers_amount = 5                                        # Кол-во потребителей, выгружающих описания
consumer_rate_limit = 2                                     # Лимит запросов в секунду для каждого потребителя
queue_max_size = product_list_limit * consumers_amount      # Максимальный размер очереди

product_descriptions = list()

async def producer(queue):
    """Получает батчи из списка товаров и добавляет product_id в очередь на получение описания."""

    async with SellerAPI(
        config=SellerAPIConfig(
            # Понижаем уровень логирования (для наглядности),
            log_level="INFO"
        )
    ) as api:

        # Параметры, необходимые для выборки данных пачками
        products_count = 0      # Счетчик выбранных товаров
        last_id = str()         # Идентификатор для пагинации

        while True:
            # Отправляем запрос и получаем очередную пачку данных о товарах
            products_batch: ProductListResponse = await api.product_list(
                ProductListRequest(
                    limit=product_list_limit,
                    last_id=last_id
                ),
            )

            # Переопределяем идентификатор выборки для следующей итерации
            last_id = products_batch.result.last_id
            # Увеличиваем счетчик выбранных товаров
            products_count += len(products_batch.result.items)

            # Добавляем айдишник каждого товара в очередь задач для выгрузки описания
            for item in products_batch.result.items:
                await queue.put(item.product_id)

            # Отчитываемся (для наглядности)
            api.logger.info(
                f"Добавлено в обработку {products_count} из {products_batch.result.total} элементов."
            )

            # Если выгрузили все товары, то прерываем цикл
            if products_count == products_batch.result.total:
                break

async def consumer(queue):
    """Получает айдишники товаров из очереди и обрабатывает их."""

    async with SellerAPI(
        config=SellerAPIConfig(
            # Понижаем уровень логирования (для наглядности)
            log_level="INFO",
            # Ограничиваем кол-во запросов в секунду для каждого потребителя
            max_requests_per_second=consumer_rate_limit
        )
    ) as api:

        while True:
            # Достаем задачу на выгрузку (идентификатор очередного товара) из очереди
            product_id = await queue.get()

            # Отправляем запрос и получаем ответ с описанием
            product_description = await api.product_info_description(
                ProductInfoDescriptionRequest(
                    product_id=product_id
                ),
            )

            # Добавляем полученное описание в общий список
            # и выводим отчет о выполнении (для наглядности)
            product_descriptions.append(product_description.result)
            api.logger.info(f"Получено описание для товара {product_description.result.id}")

            # Помечаем задачу выполненной
            queue.task_done()


async def main() -> None:
    # Создаем очередь заданий на выгрузку описаний
    queue = asyncio.Queue(maxsize=queue_max_size)

    # Добавляем заданное кол-во потребителей (потребляют из очереди задачи на выгрузку описаний)
    # в событийный цикл
    [asyncio.create_task(consumer(queue)) for _ in range(consumers_amount)]

    # Запускаем производителя (производит задачи на выгрузку описаний и добавляет их в очередь)
    await producer(queue)

    # Дожидаемся, когда потребители обработают все задачи в очереди
    await queue.join()


if __name__ == '__main__':
    asyncio.run(main())

    # Выводим полученные описания
    for product_description in product_descriptions:
        pprint(product_description.model_dump())