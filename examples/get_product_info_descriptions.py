"""
Задача: Выгрузить текстовые описания их всех карточек продавца.

Описание решения:
Частями выгрузим список товаров методом product_list(),
чтобы узнать их product_id, и, по мере получения таких частей,
асинхронно получим описания для товаров с помощью метода
product_info_description().

Для этих целей поднимем очередь из модуля asyncio и обработаем
данные по схеме producer -> queue -> consumers.

Сделаем одного производителя, чтобы складывал идентификаторы в очередь,
и несколько потребителей, каждый из которых будет забирать по одному
из очереди и асинхронно выгружать его описание,
с ограничением запросов.
"""

import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig
from src.ozonapi.seller.schemas.products import ProductListRequest, ProductListResponse, \
    ProductInfoDescriptionRequest


# Подобраны настройки обработки, позволяющие наблюдать асинхронность выполнения логики.
# Для prod значение параметра product_list_limit может быть увеличено.
# Общее кол-во запросов составит consumers_amount * consumer_rate_limit в сек + запросы по
# дефолтным настройки из SellerAPIConfig для функции producer, но не больше допустимого максимума.

product_list_limit = 10                                 # Кол-во товаров, выгружаемых за одну итерацию
consumers_amount = 5                                    # Кол-во потребителей, выгружающих описания
consumer_rate_limit = 2                                 # Лимит запросов в секунду для каждого потребителя
queue_max_size = product_list_limit * consumers_amount  # Максимальный размер очереди

product_descriptions = list()

async def producer(queue):
    """Получает батчи из списка товаров и добавляет product_id в очередь на получение описания."""

    async with SellerAPI(
        config=SellerAPIConfig(
            # Понижаем уровень логирования (для наглядности)
            log_level="INFO"
        )
    ) as api:

        # Параметры, необходимые для выборки данных
        products_count = 0      # Счетчик выбранных товаров
        last_id = str()         # Идентификатор для пагинации

        while True:
            # Отправляем запрос и получаем очередную партию данных о товарах
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

            # Добавляем айдишник каждого товара в очередь на выгрузку описания
            for item in products_batch.result.items:
                await queue.put(item.product_id)

            # Отчитываемся в консоль
            api.logger.info(
                f"Добавлено в обработку {products_count} из {products_batch.result.total} элементов."
            )

            # Если выгрузили все товары, то прерываем цикл
            if products_count == products_batch.result.total:
                break

async def consumer(queue):
    """Получает айдишники товаров из очереди и получает описания."""

    async with SellerAPI(
        config=SellerAPIConfig(
            # Понижаем уровень логирования
            log_level="INFO",
            # Ограничиваем кол-во запросов в секунду для каждого потребителя
            max_requests_per_second=consumer_rate_limit
        )
    ) as api:

        while True:
            # Достаем идентификатор очередного товара из очереди
            product_id = await queue.get()

            # Отправляем запрос и получаем ответ с описанием
            product_description = await api.product_info_description(
                ProductInfoDescriptionRequest(
                    product_id=product_id
                ),
            )

            # Добавляем полученное описание в общий список
            # и выводим в консоль отчет о выполнении
            product_descriptions.append(product_description.result)
            api.logger.info(f"Получено описание для товара {product_description.result.id}")

            # Обновляем счетчик задач
            queue.task_done()


async def main() -> None:
    # Создаем очередь заданий на выгрузку описаний
    queue = asyncio.Queue(maxsize=queue_max_size)

    # Формируем заданное кол-во потребителей (выгружают описания)
    [asyncio.create_task(consumer(queue)) for _ in range(consumers_amount)]

    # Запускаем производителя (узнает product_id товаров и заказывает для них описания)
    await producer(queue)

    # Дожидаемся, когда потребители обработают все задачи в очереди
    await queue.join()


if __name__ == '__main__':
    asyncio.run(main())

    # Выводим полученные описания
    for product_description in product_descriptions:
        pprint(product_description.model_dump())