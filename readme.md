[![PyPI - Version](https://img.shields.io/pypi/v/ozonapi-async?logo=PyPI&color=0f81c2)](https://pypi.org/project/ozonapi-async/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/ozonapi-async)](https://pypi.org/project/ozonapi-async/)
[![GitHub last commit](https://img.shields.io/github/last-commit/a-ulianov/OzonAPI)](https://github.com/a-ulianov/OzonAPI)
[![Tests](https://github.com/a-ulianov/OzonAPI/actions/workflows/test.yml/badge.svg)](https://github.com/a-ulianov/OzonAPI/actions/workflows/test.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=a-ulianov_OzonAPI&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=a-ulianov_OzonAPI)[![codecov](https://codecov.io/gh/a-ulianov/OzonAPI/branch/main/graph/badge.svg)](https://codecov.io/gh/a-ulianov/OzonAPI) 
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


# 🌀 OzonAPI 

Предоставляет легковесный асинхронный pydantic-интерфейс для взаимодействия с **Ozon Seller API**.

**Поддерживает ограничения запросов, работу с несколькими кабинетами, классическую и OAuth-авторизацию и гибкую настройку через `.env`.**


**✅ Актуально на 3-й квартал 2026 года.**
**🤝 Коммиты приветствуются!**

**🤖 С 01.06.2026 сопровождение проекта делегировано Claude Code.**

[![Telegram](https://img.shields.io/badge/Telegram-Join%20Chat-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ozonapi_async)

## ⚡️ Применение

- **📊 Автоматизация сквозной аналитики и отчетов:** Excel, Google Sheets, Bitrix24, Power BI
- **🔄 Промежуточное программное обеспечение:** 1С, ERP, WMS, CRM и брокеры
- **🤖 Чат-боты:** Telegram, Max (потенциально), RAG (для актуализации контекста)
- **📦 PIM-системы:** управлениe контентом, товарами, ценами, остатками и отзывами
- **🗄️ DataLake:** товары, цены, остатки, заказы и доставки

## 🚀 Основные возможности и характеристики

- **✔️ Проверено в production** - используется на боевых кабинетах продавцов Ozon
- **🔑 Универсальная авторизация** - поддерживает как client_id и api_key, так и OAuth-токен
- **⚡️ Асинхронный дизайн** - построен на `aiohttp` для высокопроизводительных операций
- **👍 Простое использование** - быстрое развертывание и интеграция с вашим проектом
- **📝 Отличная документация** - все методы содержат подробное описание и примеры
- **👥 Мульти-аккаунт** - одновременная работа с несколькими кабинетами продавца Ozon
- **⏱️ Умное ограничение запросов** - автоматическое соблюдение лимитов API Ozon
- **➿ Гибкая настройка лимитов** - кастомные лимиты запросов для методов
- **⏳ Кеширование ответов** - для методов, возвращающих статичные данные
- **🔄 Автоповторы** - экспоненциальные повторные попытки запросов при сбоях
- **🛡️ Валидация данных** - строгая типизация с Pydantic v2
- **📊 Детальное логирование** - асинхронная трассировка операций
- **🎪 Гибкая конфигурация** - настройка через классы, переменные окружения или .env файл
- **🧹 Очистка ресурсов** - автоматический контроль посредством контекстных менеджеров
- **🧪 Полное покрытие тестами** - вся основная функциональность

🤝 Данный проект является форком с глубокой доработкой и актуализацией проекта [python-ozon-api](https://github.com/mephistofox/python-ozon-api) от [mephistofox](https://github.com/mephistofox):

## ⚙️ Быстрый старт

### Установка

```bash
pip install ozonapi-async
```

### Базовое использование

```python
import asyncio
from ozonapi import SellerAPI

async def main():
    async with SellerAPI(
        client_id="your_client_id",     # Обязательно, если не указан oauth-токен
        api_key="your_api_key",         # Обязательно, если не указан oauth-токен
        # token="your_oauth_token",     # Альтернативная авторизация с oauth-токеном
    ) as api:
        # Получение информации о владельце личного кабинета
        seller_info = await api.seller_info()
        
        print(f"Компания: {seller_info.company.name}")
        print(f"ИНН: {seller_info.company.inn}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Настройка через конфигурационный класс

---
<details>
<summary><b>🔆 <u>Доступные параметры конфигурации</u></b></summary>

```
- client_id: Идентификатор клиента Ozon (опционально, не требуется при указании token)
- api_key: Авторизационный ключ Ozon Seller API (опционально, не требуется при указании token)
- token: OAuth-токен Ozon Seller API (опционально, не требуется при указании api_key)
- base_url: Базовый URL API Ozon (опционально)
- max_requests_per_second: Максимальное количество запросов в секунду (опционально, по умолчанию 27)
- min_instance_ttl: Длительность памяти об активных клиентах в секундах для ограничения запросов (опционально)
- connector_limit: Лимит одновременных соединений для клиента (опционально, по умолчанию 100)
- request_timeout: Максимальное время ожидания ответа на запрос в секундах (опционально, по умолчанию 30)
- max_retries: Максимальное количество повторных попыток для неудачных запросов (опционально, по умолчанию 5)
- retry_min_wait: Минимальная задержка между повторами неудачных запросов в секундах (опционально, по умолчанию 2)
- retry_max_wait: Максимальная задержка между повторами неудачных запросов в секундах (опционально, по умолчанию 10)
- log_level: Уровень логирования (опционально, по умолчанию ERROR)
- log_json: Выводить в JSON (опционально)
- log_format: Формат лога (опционально)
- log_use_async: True, чтобы включить асинхронный режим (опционально, по умолчанию True)
- log_max_queue_size: Максимальный размер очереди (опционально, только для асинхронного режима)
- log_dir: Путь к директории с логами (опционально)
- log_file: Имя файла логов (опционально, при указании логирует в файл)
- log_max_bytes: Максимальный размер файла логов в байтах (опционально, по умолчанию 10M)
- log_backup_files_count: Кол-во файлов архивных логов, которые нужно хранить (опционально, по умолчанию 5)
```
</details>

---

```python
import asyncio
from ozonapi import SellerAPI, SellerAPIConfig

async def main():
    # Создание кастомной конфигурации
    config = SellerAPIConfig(
        token="your_oauth_token",
        log_level="DEBUG"
    )
    
    async with SellerAPI(config=config) as api:
        # Работа с товарами
        products = await api.product_list()
        # Работа с ценами
        prices = await api.product_info_prices()

asyncio.run(main())
```

### Настройка через .env файл


- Любой из параметров конфигурации можно задать в файле `.env`, расположенном в корне вашего проекта.
- Правило наименования параметров в `.env`: префикс `OZON_SELLER_` + имя параметра в верхнем регистре.

*Например, для `client_id` строка в файле `.env` примет вид: `OZON_SELLER_CLIENT_ID=1234556`*


Создайте файл `.env` в корне проекта:

```env
OZON_SELLER_CLIENT_ID=your_client_id
OZON_SELLER_API_KEY=your_api_key
OZON_SELLER_MAX_REQUESTS_PER_SECOND=30
OZON_SELLER_REQUEST_TIMEOUT=60.0
OZON_SELLER_MAX_RETRIES=5
```

Использование с автоматической загрузкой из .env:

```python
import asyncio
from ozonapi import SellerAPI

async def main():
    # Конфигурация автоматически загружается из .env
    async with SellerAPI() as api:
        # Ваши API вызовы
        warehouses = await api.warehouse_list()
        print(f"Доступно складов: {len(warehouses.warehouses)}")

asyncio.run(main())
```


### Пример использования

```python
"""
Задача: Выгрузить описания для всех товаров продавца.

Описание решения: 
Частями выгрузим список товаров методом product_list(), 
чтобы узнать их product_id, и по мере выгрузки 
асинхронно получим описания для товаров с помощью метода 
product_info_description().

Для этих целей используем очереди из модуля asyncio и обработаем
данные по схеме producer -> queue -> consumers.

Сделаем одного производителя, чтобы складывал идентификаторы в очередь,
и несколько потребителей, каждый из которых будет забирать по одному 
из очереди и асинхронно выгружать его описание.
"""

import asyncio
from pprint import pprint

from ozonapi import SellerAPI, SellerAPIConfig
from ozonapi.seller.schemas.products import ProductListRequest, ProductListResponse,

ProductInfoDescriptionRequest

"""
Подобраны настройки, позволяющие отслеживать выполнение логики.
Для prod значения параметров могут быть увеличены.
"""

product_list_limit = 10     # Кол-во товаров, выгружаемых за одну итерацию
consumers_amount = 5        # Кол-во потребителей, выгружающих описания
consumers_rps_max_limit = 6 # Максимальное кол-во запросов в секунду для каждого потребителя
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
        products_count = 0  # Счетчик выбранных товаров
        last_id = str()  # Идентификатор для пагинации

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
                # Ограничиваем кол-во запросов
                max_requests_per_second=consumers_rps_max_limit
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
```

---

### Работа с несколькими аккаунтами

```python
import asyncio
from ozonapi import SellerAPI

async def main():
    # Создание клиентов для разных аккаунтов
    configs = [
        {"client_id": "id1", "api_key": "key1"},
        {"client_id": "id2", "api_key": "key2"}
    ]
    
    tasks = []
    for config in configs:
        task = asyncio.create_task(fetch_account_data(config))
        tasks.append(task)
    
    results = await asyncio.gather(*tasks)

async def fetch_account_data(config):
    async with SellerAPI(**config) as api:
        products = await api.product_list()
        return {
            "client_id": config["client_id"],
            "product_count": len(products.result.items)
        }

asyncio.run(main())
```

## 🏗️ Архитектурные особенности

### Управление ограничениями запросов

Проект автоматически соблюдает лимиты API Ozon с возможностью тонкой настройки:

```python
# Кастомные лимиты
config = SellerAPIConfig(
    max_requests_per_second=25,  # Безопасный запас
    retry_min_wait=2.0,
    retry_max_wait=10.0
)
```
**💡 Обратите внимание:**
- *Реализовано 2 вида ограничителей запросов: общий для всех запросов с одним `client_id` или `token`, а также для каждого экземпляра `SellerAPI`.*
- *Общий ограничитель запросов определен в `SellerAPIConfig.max_requests_per_second` и может быть переопределен в `.env` `OZON_SELLER_MAX_REQUESTS_PER_SECOND`.*
- *Помимо общего ограничителя можно задавать ограничители запросов для каждого инстанса SellerAPI с помощью `max_requests_per_second`.*
- *Если кол-во запросов по всем инстансам одного `client_id` или `token` превысит значение общего ограничителя, то будет применен общий ограничитель.*
- *50 запросов в сек. — определенное документацией суммарное ограничение на все выполняемые запросы от всех методов с одного `client_id` в единицу времени.*
- *25-27 запросов в сек. - оптимальное значение для ненагруженных API-запросами кабинетов (получено экпериментальным путем).*
- *У многих методов есть свои ограничения, которые не описаны документацией и могут динамически меняться Ozon, в зависимости от нагрузки на сервера.*


### Обработка ошибок и повторные попытки

Автоматические повторы запросов с экспоненциальной задержкой:

```python
# Настройка стратегии повторов
config = SellerAPIConfig(
    max_retries=3,           # Максимум 3 попытки
    retry_min_wait=1.0,      # Минимальная задержка
    retry_max_wait=10.0      # Максимальная задержка
)
```

**💡 Обратите внимание:**
*Логер уведомляет об ошибке (например, при превышении кол-ва запросов), при этом планируется повторная отправка запроса, который инициировал исключение.*


## ⚠️ Важные примечания

### Производительность

Текущая реализация оптимизирована для однопоточного асинхронного использования. Для мультипроцессных сценариев требуется дополнительная настройка системы ограничения запросов.

### Лимиты API

Проект автоматически соблюдает [официальные лимиты Ozon API](https://docs.ozon.ru/api/seller/), но рекомендуется использовать консервативные настройки лимитов (оптимально 25-27 запросов в сек. в сумме)



## 🔧 Разработка

### Установка

```bash
git clone https://github.com/a-ulianov/OzonAPI.git
cd OzonAPI
pip install -e
pytest --cov=ozonapi --cov-report=html
```


## 🤝 Поддержка

- Документация: [GitHub Repository](https://github.com/a-ulianov/OzonAPI#readme)
- Issues: [GitHub Issues](https://github.com/a-ulianov/OzonAPI/issues)
- Changelog: [Releases](https://github.com/a-ulianov/OzonAPI/releases)
- Telegram: [OzonAPI Async](https://t.me/ozonapi_async)

## ✔️ Реализованные методы Ozon Seller API

**Реализовано методов: 389 / 447**

<details>
<summary>Информация по API-ключу (0/1)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/roles` | Получить список ролей и методов по API-ключу | `roles()` |
</details>
<details>
<summary>Информация по кабинету продавца (1/2)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/seller/info` | Информация о кабинете продавца | `seller_info()` |
| ☐ | `/v1/seller/ozon-logistics/info` | Информация о подключении продавца к Ozon Логистике | `seller_ozon_logistics_info()` |
</details>
<details>
<summary>Атрибуты и характеристики Ozon (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/description-category/tree` | Дерево категорий и типов товаров | `description_category_tree()` |
| ✓ | `/v1/description-category/attribute` | Список характеристик категории | `description_category_attribute()` |
| ✓ | `/v1/description-category/attribute/values` | Справочник значений характеристики | `description_category_attribute_values()` |
| ✓ | `/v1/description-category/attribute/values/search` | Поиск по справочным значениям характеристики | `description_category_attribute_values_search()` |
</details>
<details>
<summary>Загрузка и обновление товаров (18/20)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v3/product/import` | Создать или обновить товар | `product_import()` |
| ✓ | `/v1/product/import/info` | Узнать статус добавления или обновления товара | `product_import_info()` |
| ✓ | `/v1/product/import-by-sku` | Создать товар по SKU | `product_import_by_sku()` |
| ✓ | `/v1/product/attributes/update` | Обновить характеристики товара | `product_attributes_update()` |
| ✓ | `/v1/product/pictures/import` | Загрузить или обновить изображения товара | `product_pictures_import()` |
| ✓ | `/v3/product/list` | Список товаров | `product_list()` |
| ✓ | `/v1/product/rating-by-sku` | Получить контент-рейтинг товаров по SKU | `product_rating_by_sku()` |
| ✓ | `/v3/product/info/list` | Получить информацию о товарах по идентификаторам | `product_info_list()` |
| ✓ | `/v4/product/info/attributes` | Получить описание характеристик товара | `product_info_attributes()` |
| ✓ | `/v1/product/info/description` | Получить описание товара | `product_info_description()` |
| ✓ | `/v4/product/info/limit` | Лимиты на ассортимент, создание и обновление товаров | `product_info_limit()` |
| ✓ | `/v1/product/update/offer-id` | Изменить артикулы товаров из системы продавца | `product_update_offer_id()` |
| ✓ | `/v1/product/archive` | Перенести товар в архив | `product_archive()` |
| ✓ | `/v1/product/unarchive` | Вернуть товар из архива | `product_unarchive()` |
| ✓ | `/v2/products/delete` | Удалить товар без SKU из архива | `products_delete()` |
| ✓ | `/v1/product/info/subscription` | Количество подписавшихся на товар пользователей | `product_info_subscription()` |
| ✓ | `/v1/product/related-sku/get` | Получить связанные SKU | `product_related_sku_get()` |
| ✓ | `/v2/product/pictures/info` | Получить изображения товаров | `product_pictures_info()` |
| ☐ | `/v1/product/info/wrong-volume` | Список товаров с некорректными ОВХ | `product_info_wrong_volume()` |
| ☐ | `/v1/product/placement-zone/info` | Получить зоны размещения товаров по SKU перед поставкой | `product_placement_zone_info()` |
</details>
<details>
<summary>Штрихкоды товаров (2/2)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/barcode/add` | Привязать штрихкод к товару | `barcode_add()` |
| ✓ | `/v1/barcode/generate` | Создать штрихкод для товара | `barcode_generate()` |
</details>
<details>
<summary>Цены и остатки товаров (11/11)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/products/stocks` | Обновить количество товаров на складах | `products_stocks()` |
| ✓ | `/v4/product/info/stocks` | Информация о количестве товаров | `product_info_stocks()` |
| ✓ | `/v1/product/info/warehouse/stocks` | Получить информацию по остаткам на складе FBS и rFBS | `product_info_warehouse_stocks()` |
| ✓ | `/v1/product/info/stocks-by-warehouse/fbs` | Информация об остатках на складах продавца (FBS и rFBS) | `product_info_stocks_by_warehouse_fbs_v1()` |
| ✓ | `/v2/product/info/stocks-by-warehouse/fbs` | Информация об остатках на складах продавца (FBS и rFBS) | `product_info_stocks_by_warehouse_fbs()` |
| ✓ | `/v1/product/import/prices` | Обновить цену | `product_import_prices()` |
| ✓ | `/v1/product/action/timer/update` | Обновление таймера актуальности минимальной цены | `product_action_timer_update()` |
| ✓ | `/v1/product/action/timer/status` | Получить статус установленного таймера | `product_action_timer_status()` |
| ✓ | `/v5/product/info/prices` | Получить информацию о цене товара | `product_info_prices()` |
| ✓ | `/v1/product/info/discounted` | Узнать информацию об уценке и основном товаре по SKU уценённого товара | `product_info_discounted()` |
| ✓ | `/v1/product/update/discount` | Установить скидку на уценённый товар | `product_update_discount()` |
</details>
<details>
<summary>Акции Ozon (8/8)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/actions` | Список акций | `actions()` |
| ✓ | `/v1/actions/candidates` | Список доступных для акции товаров | `actions_candidates()` |
| ✓ | `/v1/actions/products` | Список участвующих в акции товаров | `actions_products()` |
| ✓ | `/v1/actions/products/activate` | Добавить товар в акцию | `actions_products_activate()` |
| ✓ | `/v1/actions/products/deactivate` | Удалить товары из акции | `actions_products_deactivate()` |
| ✓ | `/v1/actions/discounts-task/list` | Список заявок на скидку | `actions_discounts_task_list_v1()` |
| ✓ | `/v1/actions/discounts-task/approve` | Согласовать заявку на скидку | `actions_discounts_task_approve()` |
| ✓ | `/v1/actions/discounts-task/decline` | Отклонить заявку на скидку | `actions_discounts_task_decline()` |
</details>
<details>
<summary>Стратегии ценообразования (12/12)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/pricing-strategy/competitors/list` | Список конкурентов | `strategy_competitors_list()` |
| ✓ | `/v1/pricing-strategy/list` | Список стратегий | `strategy_list()` |
| ✓ | `/v1/pricing-strategy/create` | Создать стратегию | `strategy_create()` |
| ✓ | `/v1/pricing-strategy/info` | Информация о стратегии | `strategy_info()` |
| ✓ | `/v1/pricing-strategy/update` | Обновить стратегию | `strategy_update()` |
| ✓ | `/v1/pricing-strategy/products/add` | Добавить товары в стратегию | `strategy_products_add()` |
| ✓ | `/v1/pricing-strategy/strategy-ids-by-product-ids` | Список идентификаторов стратегий | `strategy_ids_by_product_ids()` |
| ✓ | `/v1/pricing-strategy/products/list` | Список товаров в стратегии | `strategy_products_list()` |
| ✓ | `/v1/pricing-strategy/product/info` | Цена товара у конкурента | `strategy_product_info()` |
| ✓ | `/v1/pricing-strategy/products/delete` | Удалить товары из стратегии | `strategy_products_delete()` |
| ✓ | `/v1/pricing-strategy/status` | Изменить статус стратегии | `strategy_status()` |
| ✓ | `/v1/pricing-strategy/delete` | Удалить стратегию | `strategy_delete()` |
</details>
<details>
<summary>Сертификаты брендов (0/1)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/brand/company-certification/list` | Список сертифицируемых брендов | `brand_company_certification_list()` |
</details>
<details>
<summary>Сертификаты качества (15/15)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/product/certificate/accordance-types` | Список типов соответствия требований (версия 1) | `product_certificate_accordance_types()` |
| ✓ | `/v2/product/certificate/accordance-types/list` | Список типов соответствия требований (версия 2) | `product_certificate_accordance_types_list()` |
| ✓ | `/v1/product/certificate/types` | Справочник типов документов | `product_certificate_types()` |
| ✓ | `/v2/product/certification/list` | Список сертифицируемых категорий | `product_certification_list()` |
| ✓ | `/v1/product/certification/list` | Список сертифицируемых категорий | `product_certification_list_v1()` |
| ✓ | `/v1/product/certificate/create` | Добавить сертификаты для товаров | `product_certificate_create()` |
| ✓ | `/v1/product/certificate/bind` | Привязать сертификат к товару | `product_certificate_bind()` |
| ✓ | `/v1/product/certificate/delete` | Удалить сертификат | `product_certificate_delete()` |
| ✓ | `/v1/product/certificate/info` | Информация о сертификате | `product_certificate_info()` |
| ✓ | `/v1/product/certificate/list` | Список сертификатов | `product_certificate_list()` |
| ✓ | `/v1/product/certificate/product_status/list` | Список возможных статусов товаров | `product_certificate_product_status_list()` |
| ✓ | `/v1/product/certificate/products/list` | Список товаров, привязанных к сертификату | `product_certificate_products_list()` |
| ✓ | `/v1/product/certificate/unbind` | Отвязать товар от сертификата | `product_certificate_unbind()` |
| ✓ | `/v1/product/certificate/rejection_reasons/list` | Возможные причины отклонения сертификата | `product_certificate_rejection_reasons_list()` |
| ✓ | `/v1/product/certificate/status/list` | Возможные статусы сертификатов | `product_certificate_status_list()` |
</details>
<details>
<summary>Работа со складами FBS и rFBS (10/10)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/warehouse/list` | Список складов | `warehouse_list_v1()` |
| ✓ | `/v1/delivery-method/list` | Список методов доставки склада | `delivery_method_list_v1()` |
| ✓ | `/v2/delivery-method/list` | Список методов доставки склада | `delivery_method_list()` |
| ✓ | `/v1/delivery-method/return/settings/get` | Получить информацию по возвратным настройкам rFBS и rFBS Express | `delivery_method_return_settings_get()` |
| ✓ | `/v2/warehouse/list` | Список складов | `warehouse_list()` |
| ✓ | `/v1/warehouse/operation/status` | Получить статус операции | `warehouse_operation_status()` |
| ✓ | `/v1/warehouse/archive` | Перенести склад в архив | `warehouse_archive()` |
| ✓ | `/v1/warehouse/unarchive` | Перенести склад из архива | `warehouse_unarchive()` |
| ✓ | `/v1/warehouse/invalid-products/get` | Получить список товаров с ограничениями по доставке | `warehouse_invalid_products_get()` |
| ✓ | `/v1/warehouse/warehouses-with-invalid-products` | Получить список складов с ограниченными для доставки товарами | `warehouse_warehouses_with_invalid_products()` |
</details>
<details>
<summary>Создание FBS-складов и управление ими (17/17)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/warehouse/fbs/create/drop-off/list` | Получить список drop-off пунктов для создания склада | `warehouse_fbs_create_drop_off_list()` |
| ✓ | `/v1/warehouse/fbs/update/drop-off/list` | Получить список drop-off пунктов для изменения информации склада | `warehouse_fbs_update_drop_off_list()` |
| ✓ | `/v1/warehouse/fbs/create/drop-off/timeslot/list` | Получить список таймслотов для создания склада с отгрузкой drop-off | `warehouse_fbs_create_drop_off_timeslot_list()` |
| ✓ | `/v1/warehouse/fbs/update/drop-off/timeslot/list` | Получить список таймслотов для обновления склада с отгрузкой drop-off | `warehouse_fbs_update_drop_off_timeslot_list()` |
| ✓ | `/v1/warehouse/fbs/create/pick-up/timeslot/list` | Получить список таймслотов для создания склада с отгрузкой pick-up | `warehouse_fbs_create_pick_up_timeslot_list()` |
| ✓ | `/v1/warehouse/fbs/update/pick-up/timeslot/list` | Получить список таймслотов для обновления склада с отгрузкой pick-up | `warehouse_fbs_update_pick_up_timeslot_list()` |
| ✓ | `/v1/warehouse/fbs/create` | Создать склад | `warehouse_fbs_create()` |
| ✓ | `/v1/warehouse/fbs/update` | Обновить склад | `warehouse_fbs_update()` |
| ✓ | `/v1/warehouse/fbs/first-mile/update` | Обновить первую милю | `warehouse_fbs_first_mile_update()` |
| ✓ | `/v1/warehouse/fbs/create/return-point/list` | Получить список пунктов возврата для создания склада | `warehouse_fbs_create_return_point_list()` |
| ✓ | `/v1/warehouse/fbs/update/return-point/list` | Получить список пунктов возврата для обновления склада | `warehouse_fbs_update_return_point_list()` |
| ✓ | `/v1/warehouse/fbs/return-mile/info` | Получить информацию о возвратной миле | `warehouse_fbs_return_mile_info()` |
| ✓ | `/v1/warehouse/fbs/return-mile/check` | Проверить необходимость установки возвратной мили на склад | `warehouse_fbs_return_mile_check()` |
| ✓ | `/v1/warehouse/fbs/pickup/courier/create` | Создать вызов курьера на забор отгрузки pick-up | `warehouse_fbs_pickup_courier_create()` |
| ✓ | `/v1/warehouse/fbs/pickup/courier/cancel` | Отменить вызов курьера на забор отгрузки pick-up | `warehouse_fbs_pickup_courier_cancel()` |
| ✓ | `/v1/warehouse/fbs/pickup/history/list` | Получить историю отгрузок курьерам | `warehouse_fbs_pickup_history_list()` |
| ✓ | `/v1/warehouse/fbs/pickup/planning/list` | Получить список складов для планирования отгрузок курьеру | `warehouse_fbs_pickup_planning_list()` |
</details>
<details>
<summary>Создание складов rFBS Express и управление ими (7/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/warehouse/erfbs/aggregator/create` | Создать склад с методом доставки «Партнёры Ozon» | `warehouse_erfbs_aggregator_create()` |
| ✓ | `/v1/warehouse/erfbs/update` | Обновить склад | `warehouse_erfbs_update()` |
| ✓ | `/v1/warehouse/erfbs/aggregator/delivery-method/update` | Обновить метод доставки «Партнёры Ozon» | `warehouse_erfbs_aggregator_delivery_method_update()` |
| ✓ | `/v1/warehouse/erfbs/non-integrated/create` | Создать склад с методом доставки «Вы или сторонняя служба» | `warehouse_erfbs_non_integrated_create()` |
| ✓ | `/v1/warehouse/erfbs/non-integrated/delivery-method/update` | Обновить метод доставки «Вы или сторонняя служба» | `warehouse_erfbs_non_integrated_delivery_method_update()` |
| ✓ | `/v1/warehouse/rfbs/pause` | Поставить rFBS-склад на паузу | `warehouse_rfbs_pause()` |
| ✓ | `/v1/warehouse/rfbs/unpause` | Снять rFBS-склад с паузы | `warehouse_rfbs_unpause()` |
</details>
<details>
<summary>Обработка заказов FBS и rFBS (24/24)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v3/posting/fbs/unfulfilled/list` | Список необработанных отправлений | `posting_fbs_unfulfilled_list_v3()` |
| ✓ | `/v4/posting/fbs/unfulfilled/list` | Получить список необработанных отправлений | `posting_fbs_unfulfilled_list()` |
| ✓ | `/v3/posting/fbs/list` | Список отправлений | `posting_fbs_list_v3()` |
| ✓ | `/v4/posting/fbs/list` | Получить список отправлений | `posting_fbs_list()` |
| ✓ | `/v3/posting/fbs/get` | Получить информацию об отправлении по идентификатору | `posting_fbs_get()` |
| ✓ | `/v2/posting/fbs/get-by-barcode` | Получить информацию об отправлении по штрихкоду | `posting_fbs_get_by_barcode()` |
| ✓ | `/v3/posting/multiboxqty/set` | Указать количество коробок для многокоробочных отправлений | `posting_fbs_multiboxqty_set()` |
| ✓ | `/v2/posting/fbs/product/country/list` | Список доступных стран-изготовителей | `posting_fbs_product_country_list()` |
| ✓ | `/v2/posting/fbs/product/country/set` | Добавить информацию о стране-изготовителе товара | `posting_fbs_product_country_set()` |
| ✓ | `/v1/posting/fbs/restrictions` | Получить ограничения пункта приёма | `posting_fbs_restrictions()` |
| ✓ | `/v2/posting/fbs/package-label` | Напечатать этикетку | `posting_fbs_package_label()` |
| ✓ | `/v1/posting/fbs/package-label/create` | Создать задание на выгрузку этикеток | `posting_fbs_package_label_create_v1()` |
| ✓ | `/v2/posting/fbs/package-label/create` | Создать задание на формирование этикеток | `posting_fbs_package_label_create()` |
| ✓ | `/v1/posting/fbs/package-label/get` | Получить файл с этикетками | `posting_fbs_package_label_get()` |
| ✓ | `/v1/posting/fbs/cancel-reason` | Причины отмены отправления | `posting_fbs_cancel_reason()` |
| ✓ | `/v2/posting/fbs/cancel-reason/list` | Причины отмены отправлений | `posting_fbs_cancel_reason_list()` |
| ✓ | `/v2/posting/fbs/product/cancel` | Отменить отправку некоторых товаров в отправлении | `posting_fbs_product_cancel()` |
| ✓ | `/v2/posting/fbs/cancel` | Отменить отправление | `posting_fbs_cancel()` |
| ✓ | `/v2/posting/fbs/arbitration` | Открыть спор по отправлению | `posting_fbs_arbitration()` |
| ✓ | `/v2/posting/fbs/awaiting-delivery` | Передать отправление к отгрузке | `posting_fbs_awaiting_delivery()` |
| ✓ | `/v1/posting/fbs/pick-up-code/verify` | Проверить код курьера | `posting_fbs_pick_up_code_verify()` |
| ✓ | `/v1/posting/global/etgb` | Таможенные декларации ETGB | `posting_global_etgb()` |
| ✓ | `/v1/posting/unpaid-legal/product/list` | Список неоплаченных товаров, заказанных юридическими лицами | `posting_unpaid_legal_product_list()` |
| ✓ | `/v2/posting/fbs/product/change` | Изменить вес весовых товаров (устарел, удалён из API Ozon) | `posting_fbs_product_change()` |
</details>
<details>
<summary>Полигоны (0/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/polygon/create` | Создайте полигон доставки | `polygon_create()` |
| ☐ | `/v1/polygon/bind` | Свяжите метод доставки с полигоном доставки | `polygon_bind()` |
| ☐ | `/v2/polygon/bind` | Связать метод доставки с полигоном | `polygon_bind()` |
| ☐ | `/v1/polygon/delete` | Удалить полигон из области доставки | `polygon_delete()` |
| ☐ | `/v1/polygon/list` | Получить список установленных полигонов на метод доставки | `polygon_list()` |
| ☐ | `/v1/polygon/time/coordinates/update` | Обновить координаты полигона доставки | `polygon_time_coordinates_update()` |
| ☐ | `/v1/polygon/time/set` | Установить новое время доставки в полигоне | `polygon_time_set()` |
</details>
<details>
<summary>Доставка FBO (15/15)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/posting/fbo/list` | Список отправлений | `posting_fbo_list_v2()` |
| ✓ | `/v3/posting/fbo/list` | Получить список отправлений | `posting_fbo_list()` |
| ✓ | `/v2/posting/fbo/get` | Информация об отправлении | `posting_fbo_get()` |
| ✓ | `/v1/posting/fbo/cancel-reason/list` | Причины отмены отправлений по схеме FBO | `posting_fbo_cancel_reason_list()` |
| ✓ | `/v1/supply-order/status/counter` | Количество заявок по статусам | `supply_order_status_counter()` |
| ✓ | `/v1/supply-order/bundle` | Состав поставки или заявки на поставку | `supply_order_bundle()` |
| ✓ | `/v3/supply-order/list` | Список заявок на поставку на склад Ozon | `supply_order_list()` |
| ✓ | `/v3/supply-order/get` | Информация о заявке на поставку | `supply_order_get()` |
| ✓ | `/v1/supply-order/timeslot/get` | Интервалы поставки | `supply_order_timeslot_get()` |
| ✓ | `/v1/supply-order/timeslot/update` | Обновить интервал поставки | `supply_order_timeslot_update()` |
| ✓ | `/v1/supply-order/timeslot/status` | Статус интервала поставки | `supply_order_timeslot_status()` |
| ✓ | `/v1/supply-order/pass/create` | Указать данные о водителе и автомобиле | `supply_order_pass_create()` |
| ✓ | `/v1/supply-order/pass/status` | Статус ввода данных о водителе и автомобиле | `supply_order_pass_status()` |
| ✓ | `/v1/supply-order/details` | Получить подробную информацию о заявке на поставку | `supply_order_details()` |
| ✓ | `/v1/supplier/available_warehouses` | Загруженность складов Ozon | `supplier_available_warehouses()` |
</details>
<details>
<summary>Создание и управление заявками на поставку FBO (29/29)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/cluster/list` | Информация о кластерах и их складах | `cluster_list_v1()` |
| ✓ | `/v1/warehouse/fbo/list` | Поиск точек для отгрузки поставки | `warehouse_fbo_list()` |
| ✓ | `/v1/draft/create` | Создать черновик заявки на поставку | `draft_create()` |
| ✓ | `/v1/draft/crossdock/create` | Создать черновик заявки на поставку кросс-докингом | `draft_crossdock_create()` |
| ✓ | `/v1/draft/direct/create` | Создать черновик заявки на прямую поставку | `draft_direct_create()` |
| ✓ | `/v1/draft/multi-cluster/create` | Создать черновик заявки на поставку для нескольких кластеров | `draft_multi_cluster_create()` |
| ✓ | `/v1/draft/create/info` | Информация о черновике заявки на поставку | `draft_create_info_v1()` |
| ✓ | `/v1/draft/timeslot/info` | Доступные таймслоты | `draft_timeslot_info_v1()` |
| ✓ | `/v2/draft/create/info` | Получить информацию о черновике заявки на поставку | `draft_create_info()` |
| ✓ | `/v1/draft/supply/create` | Создать заявку на поставку по черновику | `draft_supply_create_v1()` |
| ✓ | `/v1/draft/supply/create/status` | Информация о создании заявки на поставку | `draft_supply_create_status_v1()` |
| ✓ | `/v2/draft/timeslot/info` | Получить список доступных таймслотов | `draft_timeslot_info()` |
| ✓ | `/v1/cargoes/create` | Установка грузомест | `cargoes_create()` |
| ✓ | `/v2/cargoes/create/info` | Получить информацию по установке грузомест | `cargoes_create_info()` |
| ✓ | `/v1/cargoes/get` | Получить информацию о грузоместах | `cargoes_get()` |
| ✓ | `/v1/cargoes/delete` | Удалить грузоместо в заявке на поставку | `cargoes_delete()` |
| ✓ | `/v1/cargoes/delete/status` | Информация о статусе удаления грузоместа | `cargoes_delete_status()` |
| ✓ | `/v1/cargoes/rules/get` | Чек-лист по установке грузомест FBO | `cargoes_rules_get()` |
| ✓ | `/v1/cargoes-label/create` | Сгенерировать этикетки для грузомест | `cargoes_label_create()` |
| ✓ | `/v1/cargoes-label/get` | Получить идентификатор этикетки для грузомест | `cargoes_label_get()` |
| ✓ | `/v1/cargoes-label/file/{file_guid}` | Получить PDF с этикетками грузовых мест | `cargoes_label_file()` |
| ✓ | `/v1/supply-order/cancel` | Отменить заявку на поставку | `supply_order_cancel()` |
| ✓ | `/v1/supply-order/cancel/status` | Получить статус отмены заявки на поставку | `supply_order_cancel_status()` |
| ✓ | `/v1/supply-order/content/update` | Редактирование товарного состава | `supply_order_content_update()` |
| ✓ | `/v1/supply-order/content/update/status` | Информация о статусе редактирования товарного состава | `supply_order_content_update_status()` |
| ✓ | `/v1/supply-order/content/update/validation` | Проверить новый товарный состав | `supply_order_content_update_validation()` |
| ✓ | `/v2/draft/supply/create` | Создать заявку на поставку по черновику | `draft_supply_create()` |
| ✓ | `/v2/draft/supply/create/status` | Получить информацию о создании заявки на поставку | `draft_supply_create_status()` |
| ✓ | `/v1/warehouse/fbo/seller/list` | Получить список складов продавца | `warehouse_fbo_seller_list()` |
</details>
<details>
<summary>Склады FBO (1/1)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/warehouse/ozon/list` | Получить список складов Ozon | `warehouse_ozon_list()` |
</details>
<details>
<summary>Управление кодами маркировки и сборкой заказов для FBS/rFBS (7/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v4/posting/fbs/ship` | Собрать заказ (версия 4) | `posting_fbs_ship()` |
| ✓ | `/v4/posting/fbs/ship/package` | Частичная сборка отправления (версия 4) | `posting_fbs_ship_package()` |
| ✓ | `/v6/fbs/posting/product/exemplar/set` | Проверить и сохранить данные экземпляров | `fbs_posting_product_exemplar_set()` |
| ✓ | `/v6/fbs/posting/product/exemplar/create-or-get` | Получить данные созданных экземпляров | `fbs_posting_product_exemplar_create_or_get()` |
| ✓ | `/v5/fbs/posting/product/exemplar/status` | Получить статус добавления экземпляров | `fbs_posting_product_exemplar_status()` |
| ✓ | `/v5/fbs/posting/product/exemplar/validate` | Валидация кодов маркировки | `fbs_posting_product_exemplar_validate()` |
| ✓ | `/v1/fbs/posting/product/exemplar/update` | Обновить данные экземпляров | `fbs_posting_product_exemplar_update()` |
</details>
<details>
<summary>Доставка FBS (27/27)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/carriage/create` | Создание отгрузки | `carriage_create()` |
| ✓ | `/v1/carriage/approve` | Подтверждение отгрузки | `carriage_approve()` |
| ✓ | `/v1/carriage/set-postings` | Изменение состава отгрузки | `carriage_set_postings()` |
| ✓ | `/v1/carriage/cancel` | Удаление отгрузки | `carriage_cancel()` |
| ✓ | `/v1/carriage/delivery/list` | Список методов доставки и отгрузок | `carriage_delivery_list_v1()` |
| ✓ | `/v2/carriage/delivery/list` | Список методов доставки и отгрузок | `carriage_delivery_list()` |
| ✓ | `/v2/posting/fbs/act/create` | Подтвердить отгрузку и создать документы | `posting_fbs_act_create()` |
| ✓ | `/v1/posting/carriage-available/list` | Список доступных перевозок | `posting_carriage_available_list()` |
| ✓ | `/v1/carriage/get` | Информация о перевозке | `carriage_get()` |
| ✓ | `/v1/posting/fbs/split` | Разделить заказ на отправления без сборки | `posting_fbs_split()` |
| ✓ | `/v2/posting/fbs/act/get-postings` | Список отправлений в акте | `posting_fbs_act_get_postings()` |
| ✓ | `/v2/posting/fbs/act/get-container-labels` | Этикетки для грузового места | `posting_fbs_act_get_container_labels()` |
| ✓ | `/v2/posting/fbs/act/get-barcode` | Штрихкод для отгрузки отправления | `posting_fbs_act_get_barcode()` |
| ✓ | `/v2/posting/fbs/act/get-barcode/text` | Значение штрихкода для отгрузки отправления | `posting_fbs_act_get_barcode_text()` |
| ✓ | `/v2/posting/fbs/digital/act/check-status` | Статус формирования накладной | `posting_fbs_digital_act_check_status()` |
| ✓ | `/v2/posting/fbs/act/get-pdf` | Получить PDF c документами | `posting_fbs_act_get_pdf()` |
| ✓ | `/v1/carriage/act-discrepancy/pdf` | Получить акт о расхождениях по отгрузке FBS | `carriage_act_discrepancy_pdf()` |
| ✓ | `/v2/posting/fbs/act/list` | Список актов по отгрузкам | `posting_fbs_act_list()` |
| ✓ | `/v2/posting/fbs/digital/act/get-pdf` | Получить лист отгрузки по перевозке | `posting_fbs_digital_act_get_pdf()` |
| ✓ | `/v2/posting/fbs/act/check-status` | Статус отгрузки и документов | `posting_fbs_act_check_status()` |
| ✓ | `/v1/posting/fbs/traceable/split` | Разделить отправление с прослеживаемыми товарами | `posting_fbs_traceable_split()` |
| ✓ | `/v1/posting/fbs/product/traceable/attribute` | Получить список незаполненных атрибутов для прослеживаемых товаров | `posting_fbs_product_traceable_attribute()` |
| ✓ | `/v1/carriage/ettn/status` | Получить статус проверки электронной ТТН на прослеживаемой перевозке FBS | `carriage_ettn_status()` |
| ✓ | `/v1/assembly/carriage/posting/list` | Получить список отправлений в отгрузке | `assembly_carriage_posting_list()` |
| ✓ | `/v1/assembly/carriage/product/list` | Получить список товаров в отгрузке | `assembly_carriage_product_list()` |
| ✓ | `/v1/assembly/fbs/posting/list` | Получить список отравлений | `assembly_fbs_posting_list()` |
| ✓ | `/v1/assembly/fbs/product/list` | Получить список товаров в отправлениях | `assembly_fbs_product_list()` |
</details>
<details>
<summary>Доставка rFBS (7/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/fbs/posting/tracking-number/set` | Добавить трек-номера | `fbs_posting_tracking_number_set()` |
| ✓ | `/v2/fbs/posting/delivering` | Изменить статус на «Доставляется» | `fbs_posting_delivering()` |
| ✓ | `/v2/fbs/posting/last-mile` | Изменить статус на «Последняя миля» | `fbs_posting_last_mile()` |
| ✓ | `/v2/fbs/posting/delivered` | Изменить статус на «Доставлено» | `fbs_posting_delivered()` |
| ✓ | `/v1/posting/fbs/timeslot/change-restrictions` | Доступные даты для переноса доставки | `posting_fbs_timeslot_change_restrictions()` |
| ✓ | `/v1/posting/fbs/timeslot/set` | Перенести дату доставки | `posting_fbs_timeslot_set()` |
| ✓ | `/v1/posting/cutoff/set` | Уточнить дату отгрузки отправления | `posting_cutoff_set()` |
</details>
<details>
<summary>Пропуски (7/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/pass/list` | Список пропусков | `pass_list()` |
| ✓ | `/v1/carriage/pass/create` | Создать пропуск | `carriage_pass_create()` |
| ✓ | `/v1/carriage/pass/update` | Обновить пропуск | `carriage_pass_update()` |
| ✓ | `/v1/carriage/pass/delete` | Удалить пропуск | `carriage_pass_delete()` |
| ✓ | `/v1/return/pass/create` | Создать пропуск для возврата | `return_pass_create()` |
| ✓ | `/v1/return/pass/update` | Обновить пропуск для возврата | `return_pass_update()` |
| ✓ | `/v1/return/pass/delete` | Удалить пропуск для возврата | `return_pass_delete()` |
</details>
<details>
<summary>Возвраты товаров FBO и FBS (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/returns/list` | Информация о возвратах FBO и FBS | `returns_list()` |
| ✓ | `/v1/returns/settings/utilization/history` | Получить историю изменений автоутилизации | `returns_settings_utilization_history()` |
| ✓ | `/v1/returns/settings/utilization/info` | Получить настройки автоутилизации | `returns_settings_utilization_info()` |
| ✓ | `/v1/returns/settings/utilization/update` | Обновить настройки автоутилизации | `returns_settings_utilization_update()` |
</details>
<details>
<summary>Возвраты товаров rFBS (8/8)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/returns/rfbs/list` | Список заявок на возврат | `returns_rfbs_list()` |
| ✓ | `/v2/returns/rfbs/get` | Информация о заявке на возврат | `returns_rfbs_get()` |
| ✓ | `/v2/returns/rfbs/reject` | Отклонить заявку на возврат | `returns_rfbs_reject()` |
| ✓ | `/v2/returns/rfbs/compensate` | Вернуть часть стоимости товара | `returns_rfbs_compensate()` |
| ✓ | `/v2/returns/rfbs/verify` | Одобрить заявку на возврат | `returns_rfbs_verify()` |
| ✓ | `/v2/returns/rfbs/receive-return` | Подтвердить получение товара на проверку | `returns_rfbs_receive_return()` |
| ✓ | `/v2/returns/rfbs/return-money` | Вернуть деньги покупателю | `returns_rfbs_return_money()` |
| ✓ | `/v1/returns/rfbs/action/set` | Передать доступные действия для rFBS возвратов | `returns_rfbs_action_set()` |
</details>
<details>
<summary>Возвратные отгрузки (8/8)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/returns/company/fbs/info` | Количество возвратов FBS | `returns_company_fbs_info()` |
| ✓ | `/v1/return/giveout/is-enabled` | Проверить возможность получения возвратных отгрузок по штрихкоду | `return_giveout_is_enabled()` |
| ✓ | `/v1/return/giveout/list` | Список возвратных отгрузки | `return_giveout_list()` |
| ✓ | `/v1/return/giveout/info` | Информация о возвратной отгрузке | `return_giveout_info()` |
| ✓ | `/v1/return/giveout/barcode` | Значение штрихкода для возвратных отгрузок | `return_giveout_barcode()` |
| ✓ | `/v1/return/giveout/get-pdf` | Штрихкод для получения возвратной отгрузки в формате PDF | `return_giveout_get_pdf()` |
| ✓ | `/v1/return/giveout/get-png` | Штрихкод для получения возвратной отгрузки в формате PNG | `return_giveout_get_png()` |
| ✓ | `/v1/return/giveout/barcode-reset` | Сгенерировать новый штрихкод | `return_giveout_barcode_reset()` |
</details>
<details>
<summary>Отмены заказов (3/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/conditional-cancellation/list` | Получить список заявок на отмену rFBS | `conditional_cancellation_list()` |
| ✓ | `/v2/conditional-cancellation/approve` | Подтвердить заявку на отмену rFBS | `conditional_cancellation_approve()` |
| ✓ | `/v2/conditional-cancellation/reject` | Отклонить заявку на отмену rFBS | `conditional_cancellation_reject()` |
</details>
<details>
<summary>Чаты с покупателями (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/chat/send/file` | Отправить файл | `chat_send_file()` |
| ✓ | `/v2/chat/list` | Список чатов (устарел, 404) | `chat_list_v2()` |
| ✓ | `/v3/chat/list` | Список чатов | `chat_list()` |
| ✓ | `/v3/chat/history` | История чата | `chat_history()` |
</details>
<details>
<summary>Накладные (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/invoice/create-or-update` | Создать или изменить счёт-фактуру | `invoice_create_or_update()` |
| ✓ | `/v1/invoice/file/upload` | Загрузка счёта-фактуры | `invoice_file_upload()` |
| ✓ | `/v2/invoice/get` | Получить информацию о счёте-фактуре | `invoice_get()` |
| ✓ | `/v1/invoice/delete` | Удалить ссылку на счёт-фактуру | `invoice_delete()` |
</details>
<details>
<summary>Отчёты (11/11)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/report/info` | Информация об отчёте | `report_info()` |
| ✓ | `/v1/report/list` | Список отчётов | `report_list()` |
| ✓ | `/v1/report/products/create` | Отчёт по товарам | `report_products_create()` |
| ✓ | `/v2/report/returns/create` | Отчёт о возвратах | `report_returns_create()` |
| ✓ | `/v1/report/postings/create` | Отчёт об отправлениях | `report_postings_create()` |
| ✓ | `/v1/finance/cash-flow-statement/list` | Финансовый отчёт | `finance_cash_flow_statement_list()` |
| ✓ | `/v1/report/discounted/create` | Отчёт об уценённых товарах | `report_discounted_create()` |
| ✓ | `/v1/report/warehouse/stock` | Отчёт об остатках на FBS-складе | `report_warehouse_stock()` |
| ✓ | `/v1/report/placement/by-products/create` | Получить отчёт о стоимости размещения по товарам | `report_placement_by_products_create()` |
| ✓ | `/v1/report/placement/by-supplies/create` | Получить отчёт о стоимости размещения по поставкам | `report_placement_by_supplies_create()` |
| ✓ | `/v1/report/marked-products-sales/create` | Отчёт по продажам товаров с маркировкой | `report_marked_products_sales_create()` |
</details>
<details>
<summary>Аналитические отчёты (3/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/analytics/stock_on_warehouses` | Отчёт по остаткам и товарам | `analytics_stock_on_warehouses()` |
| ✓ | `/v1/analytics/turnover/stocks` | Оборачиваемость товара | `analytics_turnover_stocks()` |
| ✓ | `/v1/analytics/stocks` | Получить аналитику по остаткам | `analytics_stocks()` |
</details>
<details>
<summary>Финансовые отчёты (10/10)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v2/finance/realization` | Отчёт о реализации товаров (версия 2) | `finance_realization()` |
| ✓ | `/v1/finance/realization/posting` | Позаказный отчёт о реализации товаров | `finance_realization_posting()` |
| ✓ | `/v3/finance/transaction/list` | Список транзакций | `finance_transaction_list()` |
| ✓ | `/v3/finance/transaction/totals` | Суммы транзакций | `finance_transaction_totals()` |
| ✓ | `/v1/finance/document-b2b-sales` | Реестр продаж юридическим лицам | `finance_document_b2b_sales()` |
| ✓ | `/v1/finance/document-b2b-sales/json` | Реестр продаж юридическим лицам в JSON-формате | `finance_document_b2b_sales_json()` |
| ✓ | `/v1/finance/mutual-settlement` | Отчёт о взаиморасчётах | `finance_mutual_settlement()` |
| ✓ | `/v1/finance/products/buyout` | Отчёт о выкупленных товарах | `finance_products_buyout()` |
| ✓ | `/v1/finance/compensation` | Отчёт о компенсациях | `finance_compensation()` |
| ✓ | `/v1/finance/decompensation` | Отчёт о декомпенсациях | `finance_decompensation()` |
</details>
<details>
<summary>Чеки (3/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/receipts/get` | Получить чек в формате PDF | `receipts_get()` |
| ✓ | `/v1/receipts/seller/list` | Получить список чеков продавца | `receipts_seller_list()` |
| ✓ | `/v1/receipts/upload` | Загрузить чек | `receipts_upload()` |
</details>
<details>
<summary>Рейтинг продавца (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/rating/summary` | Получить информацию о текущих рейтингах продавца | `rating_summary()` |
| ✓ | `/v1/rating/history` | Получить информацию о рейтингах продавца за период | `rating_history()` |
| ✓ | `/v1/rating/index/fbs/info` | Получить индекс ошибок FBS и rFBS | `rating_index_fbs_info()` |
| ✓ | `/v1/rating/index/fbs/posting/list` | Список отправлений, которые повлияли на индекс ошибок FBS и rFBS | `rating_index_fbs_posting_list()` |
</details>
<details>
<summary>Работа с цифровыми товарами (2/2)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/posting/digital/codes/upload` | Загрузить коды цифровых товаров для отправления | `posting_digital_codes_upload()` |
| ✓ | `/v1/product/digital/stocks/import` | Обновить количество цифровых товаров | `product_digital_stocks_import()` |
</details>
<details>
<summary>Прочие методы (14/14)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/analytics/manage/stocks` | Управление остатками | `analytics_manage_stocks()` |
| ✓ | `/v1/removal/from-supply/list` | Отчёт по вывозу и утилизации с поставки FBO | `removal_from_supply_list()` |
| ✓ | `/v1/removal/from-stock/list` | Отчёт по вывозу и утилизации со стока FBO | `removal_from_stock_list()` |
| ✓ | `/v1/product/stairway-discount/by-quantity/set` | Управлять скидкой от количества | `product_stairway_discount_by_quantity_set()` |
| ✓ | `/v1/product/stairway-discount/by-quantity/get` | Получить информацию о скидке от количества | `product_stairway_discount_by_quantity_get()` |
| ✓ | `/v1/finance/balance` | Получить отчёт о балансе | `finance_balance()` |
| ✓ | `/v2/actions/discounts-task/list` | Получить список заявок на скидку | `actions_discounts_task_list()` |
| ✓ | `/v2/cluster/list` | Получить информацию о макролокальных кластерах | `cluster_list()` |
| ✓ | `/v1/product/visibility/set` | Настроить видимость товара на витрине Ozon и Ozon Селект | `product_visibility_set()` |
| ✓ | `/v2/posting/digital/list` | Получить список отправлений | `posting_digital_list()` |
| ✓ | `/v1/finance/accrual/postings` | Получить начисления по отправлениям | `finance_accrual_postings()` |
| ✓ | `/v1/finance/accrual/types` | Получить справочник начислений | `finance_accrual_types()` |
| ✓ | `/v1/finance/accrual/by-day` | Получить начисления за день | `finance_accrual_by_day()` |
| ✓ | `/v1/product/visibility/info` | Получить информацию о видимости товара | `product_visibility_info()` |
</details>
<details>
<summary>Работа с квантами (2/2)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/product/quant/list` | Список эконом-товаров | `product_quant_list()` |
| ✓ | `/v1/product/quant/info` | Информация об эконом-товаре | `product_quant_info()` |
</details>
<details>
<summary>Работа с отзывами (12/12)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/review/comment/create` | Оставить комментарий на отзыв | `review_comment_create()` |
| ✓ | `/v1/review/comment/delete` | Удалить комментарий на отзыв | `review_comment_delete_v1()` |
| ✓ | `/v2/review/comment/delete` | Удалить комментарий на отзыв | `review_comment_delete()` |
| ✓ | `/v1/review/comment/list` | Список комментариев на отзыв | `review_comment_list()` |
| ✓ | `/v1/review/change-status` | Изменить статус отзывов | `review_change_status_v1()` |
| ✓ | `/v2/review/change-status` | Изменить статус отзывов | `review_change_status()` |
| ✓ | `/v1/review/count` | Количество отзывов по статусам | `review_count_v1()` |
| ✓ | `/v2/review/count` | Получить количество отзывов по статусам | `review_count()` |
| ✓ | `/v1/review/info` | Получить информацию об отзыве | `review_info_v1()` |
| ✓ | `/v2/review/info` | Получить информацию по отзыву | `review_info()` |
| ✓ | `/v1/review/list` | Получить список отзывов | `review_list_v1()` |
| ✓ | `/v2/review/list` | Получить список отзывов | `review_list()` |
</details>
<details>
<summary>Работа с вопросами и ответами (8/8)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/question/answer/create` | Создать ответ на вопрос | `question_answer_create()` |
| ✓ | `/v1/question/answer/delete` | Удалить ответ на вопрос | `question_answer_delete()` |
| ✓ | `/v1/question/answer/list` | Список ответов на вопрос | `question_answer_list()` |
| ✓ | `/v1/question/change-status` | Изменить статус вопросов | `question_change_status()` |
| ✓ | `/v1/question/count` | Количество вопросов по статусам | `question_count()` |
| ✓ | `/v1/question/info` | Информация о вопросе | `question_info()` |
| ✓ | `/v1/question/list` | Список вопросов | `question_list()` |
| ✓ | `/v1/question/top-sku` | Товары с наибольшим количеством вопросов | `question_top_sku()` |
</details>
<details>
<summary>Акции продавца (18/18)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/seller-actions/create/discount` | Создать акцию с механикой «Скидка» | `seller_actions_create_discount()` |
| ✓ | `/v1/seller-actions/create/discount-with-condition` | Создать акцию с механикой «Скидка от суммы заказа» | `seller_actions_create_discount_with_condition()` |
| ✓ | `/v1/seller-actions/create/installment` | Создать акцию с механикой «Беспроцентная рассрочка» | `seller_actions_create_installment()` |
| ✓ | `/v1/seller-actions/create/multi-level-discount` | Создать акцию с механикой «Многоуровневая скидка от суммы» | `seller_actions_create_multi_level_discount()` |
| ✓ | `/v1/seller-actions/create/voucher` | Создать акцию с механикой «Скидка по промокоду» | `seller_actions_create_voucher()` |
| ✓ | `/v1/seller-actions/update/discount` | Обновить акцию с механикой «Скидка» | `seller_actions_update_discount()` |
| ✓ | `/v1/seller-actions/update/discount-with-condition` | Обновить акцию с механикой «Скидка от суммы заказа» | `seller_actions_update_discount_with_condition()` |
| ✓ | `/v1/seller-actions/update/installment` | Обновить акцию с механикой «Беспроцентная рассрочка» | `seller_actions_update_installment()` |
| ✓ | `/v1/seller-actions/update/multi-level-discount` | Обновить акцию с механикой «Многоуровневая скидка от суммы» | `seller_actions_update_multi_level_discount()` |
| ✓ | `/v1/seller-actions/update/voucher` | Обновить акцию с механикой «Скидка по промокоду» | `seller_actions_update_voucher()` |
| ✓ | `/v1/seller-actions/products/add` | Добавить товары в акцию | `seller_actions_products_add()` |
| ✓ | `/v1/seller-actions/products/candidates` | Получить список доступных для акции товаров | `seller_actions_products_candidates()` |
| ✓ | `/v1/seller-actions/products/delete` | Удалить товары из акции | `seller_actions_products_delete()` |
| ✓ | `/v1/seller-actions/products/list` | Получить список участвующих в акции товаров | `seller_actions_products_list()` |
| ✓ | `/v1/seller-actions/archive` | Перенести акцию в архив | `seller_actions_archive()` |
| ✓ | `/v1/seller-actions/change-activity` | Включить или выключить акцию | `seller_actions_change_activity()` |
| ✓ | `/v1/seller-actions/list` | Получить список акций | `seller_actions_list()` |
| ✓ | `/v1/seller-actions/voucher/get` | Получить файл с промокодами в формате CSV | `seller_actions_voucher_get()` |
</details>
<details>
<summary>Акции Ozon (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/actions/auto-add/products/list` | Получить список товаров из автодобавления в акцию | `actions_auto_add_products_list()` |
| ✓ | `/v1/actions/auto-add/products/candidates` | Получить список доступных товаров для автодобавления в акцию | `actions_auto_add_products_candidates()` |
| ✓ | `/v1/actions/auto-add/products/delete` | Удалить товары из автодобавления в акцию | `actions_auto_add_products_delete()` |
| ✓ | `/v1/actions/auto-add/products/update` | Добавить или обновить товары в автодобавлении в акцию | `actions_auto_add_products_update()` |
</details>
<details>
<summary>Работа с пуш-уведомлениями (7/7)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/notification/set` | Подключить URL-адрес для уведомлений | `notification_set()` |
| ✓ | `/v1/notification/update` | Изменить URL-адрес для уведомлений | `notification_update()` |
| ✓ | `/v1/notification/delete` | Удалить URL-адрес для уведомлений | `notification_delete()` |
| ✓ | `/v1/notification/check` | Проверить URL-адрес для уведомлений | `notification_check()` |
| ✓ | `/v1/notification/enable` | Включить или выключить уведомления на URL-адрес | `notification_enable()` |
| ✓ | `/v1/notification/list` | Получить информацию по подключённым URL-адресам | `notification_list()` |
| ✓ | `/v1/notification/push-type/list` | Получить типы пуш-уведомлений | `notification_push_type_list()` |
</details>
<details>
<summary>Работа с FBP-черновиками (0/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/warehouse/list` | Получить список партнёрских складов | `fbp_warehouse_list()` |
| ☐ | `/v1/fbp/draft/get` | Получить информацию о черновике поставки | `fbp_draft_get()` |
| ☐ | `/v1/fbp/draft/list` | Список черновиков поставки | `fbp_draft_list()` |
</details>
<details>
<summary>Работа с FBP-черновиками с доставкой direct (0/10)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/draft/direct/seller-dlv/create` | Создать черновик с доставкой силами продавца | `fbp_draft_direct_seller_dlv_create()` |
| ☐ | `/v1/fbp/draft/direct/seller-dlv/edit` | Обновить информацию о доставке силами продавца в черновике | `fbp_draft_direct_seller_dlv_edit()` |
| ☐ | `/v1/fbp/draft/direct/timeslot/edit` | Отредактировать таймслот в черновике | `fbp_draft_direct_timeslot_edit()` |
| ☐ | `/v1/fbp/draft/direct/timeslot/get` | Получить список таймслотов для прямой поставки | `fbp_draft_direct_timeslot_get()` |
| ☐ | `/v1/fbp/draft/direct/create` | Создать черновик заявки на поставку без указания способа доставки | `fbp_draft_direct_create()` |
| ☐ | `/v1/fbp/draft/direct/delete` | Удалить черновик заявки на поставку | `fbp_draft_direct_delete()` |
| ☐ | `/v1/fbp/draft/direct/product/validate` | Проверить список товаров для склада партнёра | `fbp_draft_direct_product_validate()` |
| ☐ | `/v1/fbp/draft/direct/registrate` | Перевести черновик в действующую поставку | `fbp_draft_direct_registrate()` |
| ☐ | `/v1/fbp/draft/direct/tpl-dlv/create` | Создать черновик заявки на доставку сторонней транспортной компанией | `fbp_draft_direct_tpl_dlv_create()` |
| ☐ | `/v1/fbp/draft/direct/tpl-dlv/edit` | Редактировать черновик поставки со способом доставки сторонней транспортной компанией | `fbp_draft_direct_tpl_dlv_edit()` |
</details>
<details>
<summary>Работа с FBP-черновиками c доставкой drop-off (0/8)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/draft/drop-off/create` | Создать черновик для доставки в drop-off пункт | `fbp_draft_drop_off_create()` |
| ☐ | `/v1/fbp/draft/drop-off/delete` | Удалить черновик для доставки в drop-off пункт | `fbp_draft_drop_off_delete()` |
| ☐ | `/v1/fbp/draft/drop-off/dlv/edit` | Отредактировать детали доставки для drop-off черновика | `fbp_draft_drop_off_dlv_edit()` |
| ☐ | `/v1/fbp/draft/drop-off/registrate` | Перевести черновик в действующую поставку | `fbp_draft_drop_off_registrate()` |
| ☐ | `/v1/fbp/draft/drop-off/province/list` | Получить список провинций | `fbp_draft_drop_off_province_list()` |
| ☐ | `/v1/fbp/draft/drop-off/point/list` | Получить список drop-off пунктов в провинции | `fbp_draft_drop_off_point_list()` |
| ☐ | `/v1/fbp/draft/drop-off/point/timetable` | Получить расписание работы drop-off пункта | `fbp_draft_drop_off_point_timetable()` |
| ☐ | `/v1/fbp/draft/drop-off/product/validate` | Проверить список товаров, которые склад партнёра может принять | `fbp_draft_drop_off_product_validate()` |
</details>
<details>
<summary>Работа с FBP-черновиками с доставкой pick-up (0/5)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/draft/pick-up/create` | Создать черновик заявки на pick-up поставку | `fbp_draft_pick_up_create()` |
| ☐ | `/v1/fbp/draft/pick-up/delete` | Отменить черновик заявки на pick-up поставку | `fbp_draft_pick_up_delete()` |
| ☐ | `/v1/fbp/draft/pick-up/dlv/edit` | Изменить черновик заявки на pick-up поставку | `fbp_draft_pick_up_dlv_edit()` |
| ☐ | `/v1/fbp/draft/pick-up/product/validate` | Провалидировать список товаров для pick-up поставки | `fbp_draft_pick_up_product_validate()` |
| ☐ | `/v1/fbp/draft/pick-up/registrate` | Перевести черновик в действующую поставку | `fbp_draft_pick_up_registrate()` |
</details>
<details>
<summary>Работа с FBP-поставками с доставкой direct (0/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/order/direct/cancel` | Отменить поставку | `fbp_order_direct_cancel()` |
| ☐ | `/v1/fbp/order/direct/seller-dlv/edit` | Обновить информацию о доставке силами продавца | `fbp_order_direct_seller_dlv_edit()` |
| ☐ | `/v1/fbp/order/direct/timeslot/edit` | Отредактировать таймслот в заявке на поставку | `fbp_order_direct_timeslot_edit()` |
| ☐ | `/v1/fbp/order/direct/timeslot/list` | Получить список таймслотов для поставки | `fbp_order_direct_timeslot_list()` |
</details>
<details>
<summary>Работа с FBP-поставками с доставкой drop-off (0/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/order/drop-off/cancel` | Отменить поставку drop-off | `fbp_order_drop_off_cancel()` |
| ☐ | `/v1/fbp/order/drop-off/dlv/edit` | Отредактировать информацию о поставке на drop-off пункт | `fbp_order_drop_off_dlv_edit()` |
| ☐ | `/v1/fbp/order/drop-off/timetable` | Получить график работы drop-off пункта | `fbp_order_drop_off_timetable()` |
</details>
<details>
<summary>Работа с FBP-поставками с доставкой pick-up (0/2)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/order/pick-up/cancel` | Отменить pick-up поставку | `fbp_order_pick_up_cancel()` |
| ☐ | `/v1/fbp/order/pick-up/dlv/edit` | Изменить данные о точке забора | `fbp_order_pick_up_dlv_edit()` |
</details>
<details>
<summary>Работа с созданной поставкой FBP (0/11)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/fbp/act-from/create` | Сгенерировать акт приёмки | `fbp_act_from_create()` |
| ☐ | `/v1/fbp/act-from/get` | Получить статус генерации акта приёмки | `fbp_act_from_get()` |
| ☐ | `/v1/fbp/act-to/create` | Сгенерировать транспортную накладную | `fbp_act_to_create()` |
| ☐ | `/v1/fbp/act-to/get` | Получить статус генерации транспортной накладной | `fbp_act_to_get()` |
| ☐ | `/v1/fbp/archive/get` | Получить информацию о завершённой поставке | `fbp_archive_get()` |
| ☐ | `/v1/fbp/archive/list` | Получить список завершённых поставок | `fbp_archive_list()` |
| ☐ | `/v1/fbp/label/create` | Cоздать задание на генерацию этикеток | `fbp_label_create()` |
| ☐ | `/v1/fbp/label/get` | Получить статус задания на генерацию этикеток | `fbp_label_get()` |
| ☐ | `/v1/fbp/order/get` | Получить информацию о конкретной поставке | `fbp_order_get()` |
| ☐ | `/v1/fbp/order/list` | Получить список поставок | `fbp_order_list()` |
| ☐ | `/v1/posting/fbp/list` | Получить список отправлений | `posting_fbp_list()` |
</details>
<details>
<summary>Работа с грузоместами FBS (13/13)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/carriage/container/create` | Создать грузоместо | `carriage_container_create()` |
| ✓ | `/v1/carriage/container/fill` | Наполнить грузоместо отправлениями | `carriage_container_fill()` |
| ✓ | `/v1/carriage/container/approve` | Подтвердить состав грузоместа | `carriage_container_approve()` |
| ✓ | `/v1/carriage/container/place-into` | Разместить коробки на палете | `carriage_container_place_into()` |
| ✓ | `/v1/carriage/container/remove-postings` | Убрать отправления из грузоместа | `carriage_container_remove_postings()` |
| ✓ | `/v1/carriage/container/remove-from` | Убрать коробки с палеты | `carriage_container_remove_from()` |
| ✓ | `/v1/carriage/container/cancel` | Отменить грузоместо | `carriage_container_cancel()` |
| ✓ | `/v1/carriage/container/list` | Получить список грузомест | `carriage_container_list()` |
| ✓ | `/v1/carriage/container/get` | Получить информацию о грузоместах | `carriage_container_get()` |
| ✓ | `/v1/carriage/container/status/get` | Получить статус грузомест FBS | `carriage_container_status_get()` |
| ✓ | `/v1/carriage/container/task/info` | Получить статус задачи грузового места | `carriage_container_task_info()` |
| ✓ | `/v1/carriage/container/document/get` | Получить документы по грузоместам — ТрН и лист отгрузки | `carriage_container_document_get()` |
| ✓ | `/v1/carriage/container/label/get` | Получить этикетку по грузоместам | `carriage_container_label_get()` |
</details>
<details>
<summary>Premium-методы (10/10)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/chat/send/message` | Отправить сообщение | `chat_send_message()` |
| ✓ | `/v1/chat/start` | Создать новый чат | `chat_start()` |
| ✓ | `/v2/chat/read` | Отметить сообщения как прочитанные | `chat_read()` |
| ✓ | `/v1/analytics/data` | Данные аналитики | `analytics_data()` |
| ✓ | `/v1/analytics/product-queries` | Получить информацию о запросах моих товаров | `analytics_product_queries()` |
| ✓ | `/v1/analytics/product-queries/details` | Получить детализацию запросов по товару | `analytics_product_queries_details()` |
| ✓ | `/v1/finance/realization/by-day` | Отчёт о реализации товаров за день | `finance_realization_by_day()` |
| ✓ | `/v1/search-queries/text` | Получить список поисковых запросов по тексту | `search_queries_text()` |
| ✓ | `/v1/search-queries/top` | Получить список популярных поисковых запросов | `search_queries_top()` |
| ✓ | `/v1/product/prices/details` | Получить подробную информацию о ценах товаров | `product_prices_details()` |
</details>
<details>
<summary>Причины отмены (3/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/cancel-reason/list` | Список причин отмен для заказа | `cancel_reason_list()` |
| ✓ | `/v1/cancel-reason/list-by-order` | Динамический список отмен для заказа | `cancel_reason_list_by_order()` |
| ✓ | `/v1/cancel-reason/list-by-posting` | Динамический список отмен для постинга из заказа | `cancel_reason_list_by_posting()` |
</details>
<details>
<summary>Доставка (5/5)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/delivery/check` | Проверка доступности доставки Ozon для покупателя | `delivery_check()` |
| ✓ | `/v2/delivery/checkout` | Получить доступные варианты доставки | `delivery_checkout()` |
| ✓ | `/v1/delivery/map` | Получить список точек самовывоза на карте | `delivery_map()` |
| ✓ | `/v1/delivery/point/info` | Получить информацию о выбранной точке самовывоза | `delivery_point_info()` |
| ✓ | `/v1/delivery/point/list` | Получить список всех точек самовывоза | `delivery_point_list()` |
</details>
<details>
<summary>Заказы (4/4)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/order/cancel` | Метод отмены заказа | `order_cancel()` |
| ✓ | `/v1/order/cancel/check` | Проверка доступности отмены | `order_cancel_check()` |
| ✓ | `/v1/order/cancel/status` | Статус отмены заказа | `order_cancel_status()` |
| ✓ | `/v2/order/create` | Создать заказ | `order_create()` |
</details>
<details>
<summary>Отправления (3/3)</summary>

| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/posting/cancel` | Метод отмены постинга из заказа | `posting_cancel()` |
| ✓ | `/v1/posting/cancel/status` | Статус отмены постинга из заказа | `posting_cancel_status()` |
| ✓ | `/v1/posting/marks` | Получить список кодов маркировок товаров | `posting_marks()` |
</details>

---

[MIT License](LICENSE)

---

*Проект не аффилирован с Ozon. Все торговые марки принадлежат их правообладателям.*