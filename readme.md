[![Tests](https://github.com/a-ulianov/OzonAPI/actions/workflows/test.yml/badge.svg)](https://github.com/a-ulianov/OzonAPI/actions/workflows/test.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=a-ulianov_OzonAPI&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=a-ulianov_OzonAPI)[![codecov](https://codecov.io/gh/a-ulianov/OzonAPI/branch/main/graph/badge.svg)](https://codecov.io/gh/a-ulianov/OzonAPI) 
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)


# OzonAPI

Асинхронный Python-клиент для работы с API маркетплейса Ozon. Проект предоставляет удобный интерфейс для взаимодействия с разделами API Ozon.

**✅ Актуально на 4-й квартал 2025 года.**
**🤝 Контрибуции приветствуются!**


## 🚀 Основные возможности

- **⚡ Асинхронный дизайн** - построен на `aiohttp` для высокопроизводительных операций
- **👍 Простое использование** - быстрое развертывание и интеграция с вашим проектом
- **📝 Отличная документация** - все методы содержат подробное описание и примеры
- **👥 Мульти-аккаунт** - одновременная работа с несколькими кабинетами продавца Ozon
- **🎯 Умное ограничение запросов** - автоматическое соблюдение лимитов API Ozon
- **➿ Гибкая настройка лимитов** - кастомные лимиты запросов для методов
- **🛡️ Валидация данных** - строгая типизация с Pydantic v2
- **🔄 Автоповторы** - интеллектуальные повторные попытки запросов при сбоях
- **📊 Детальное логирование** - асинхронная трассировка операций
- **🎪 Гибкая конфигурация** - настройка через классы, переменные окружения или .env файлы
- **🧹 Очистка ресурсов** - автоматический контроль посредством контекстных менеджеров
- **🧪 Полное покрытие тестами** - вся основная функциональность
- **✔️ Проверено в production** - тестируется на боевых кабинетах продавцов Ozon


🤝 Данный проект является форком с глубокой доработкой и актуализацией проекта [python-ozon-api](https://github.com/mephistofox/python-ozon-api) от [mephistofox](https://github.com/mephistofox):
- Изменена структура проекта
- Реализован кастомный ограничитель запросов для методов
- Реализована возможность одновременной работы с несколькими экземплярами менеджера API, в т.ч. для одного client_id
- Удалены устаревшие методы
- Актуализированы схемы Pydantic реализованных методов
- Добавлены новые методы
- Добавлено описание и примеры для методов и схем
- Реализована гибкая настройка конфигурации


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
        client_id="your_client_id",
        api_key="your_api_key"
    ) as api:
        # Получение списка товаров
        products = await api.product_list()
        print(f"Найдено товаров: {len(products.result.items)}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Настройка через конфигурационный класс

```python
import asyncio
from ozonapi import SellerAPI, SellerAPIConfig

async def main():
    # Создание кастомной конфигурации
    config = SellerAPIConfig(
        client_id="your_client_id",
        api_key="your_api_key",
        max_requests_per_second=30,
        request_timeout=60.0,
        max_retries=5
    )
    
    async with SellerAPI(config=config) as api:
        # Работа с товарами
        products = await api.product_list()
        # Работа с ценами
        prices = await api.product_info_prices()

asyncio.run(main())
```

### Настройка через .env файл

Создайте файл `.env` в корне проекта:

```env
OZON_SELLER_CLIENT_ID=your_client_id
OZON_SELLER_API_KEY=your_api_key
OZON_SELLER_MAX_REQUESTS_PER_SECOND=30
OZON_SELLER_REQUEST_TIMEOUT=60.0
OZON_SELLER_MAX_RETRIES=5
OZON_SELLER_BASE_URL=https://api-seller.ozon.ru
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
        print(f"Доступно складов: {len(warehouses.result)}")

asyncio.run(main())
```

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

Проект автоматически соблюдает лимиты API Ozon (50 запросов в секунду) с возможностью тонкой настройки:

```python
# Кастомные лимиты
config = SellerAPIConfig(
    max_requests_per_second=25,  # Безопасный запас
    retry_min_wait=2.0,
    retry_max_wait=10.0
)
```

### Обработка ошибок и повторные попытки

Автоматические повторы для временных сбоев с экспоненциальной задержкой:

```python
# Настройка стратегии повторов
config = SellerAPIConfig(
    max_retries=3,           # Максимум 3 попытки
    retry_min_wait=1.0,      # Минимальная задержка
    retry_max_wait=10.0      # Максимальная задержка
)
```

### Расширенное логирование

```python
# Настройка файлового логирования (core.py)
logger.add("ozon_api.log", rotation="10 MB", level="INFO")
```

## ⚠️ Важные примечания

### Производительность

Текущая реализация оптимизирована для однопоточного асинхронного использования. Для мультипроцессных сценариев требуется дополнительная настройка системы ограничения запросов.

### Лимиты API

Проект автоматически соблюдает [официальные лимиты Ozon API](https://docs.ozon.ru/api/seller/), но рекомендуется:
- Использовать консервативные настройки лимитов
- Мониторить статистику использования через встроенные методы

## 🔧 Разработка

### Установка

```bash
git clone https://github.com/a-ulianov/OzonAPI.git
cd OzonAPI
pip install -e
```

### Запуск тестов

```bash
pytest --cov=ozonapi --cov-report=html
```

## 🤝 Поддержка

- Документация: [GitHub Repository](https://github.com/a-ulianov/OzonAPI#readme)
- Issues: [GitHub Issues](https://github.com/a-ulianov/OzonAPI/issues)
- Changelog: [Releases](https://github.com/a-ulianov/OzonAPI/releases)


# Чек-лист реализации Python-интерфейса для API Ozon

## Атрибуты и характеристики Ozon
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/description-category/tree` | Дерево категорий и типов товаров | `description_category_tree()` |
| ✓ | `/v1/description-category/attribute` | Список характеристик категории | `description_category_attribute()` |
| ✓ | `/v1/description-category/attribute/values` | Справочник значений характеристики | `description_category_attribute_values()` |
| ✓ | `/v1/description-category/attribute/values/search` | Поиск по справочным значениям характеристики | `description_category_attribute_values_search()` |

## Загрузка и обновление товаров
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v3/product/import` | Создать или обновить товар | `product_import()` |
| ✓ | `/v1/product/import/info` | Узнать статус добавления или обновления товара | `product_import_info()` |
| ✓ | `/v1/product/import-by-sku` | Создать товар по SKU | `product_import_by_sku()` |
| ✓ | `/v1/product/attributes/update` | Обновить характеристики товара | `product_attributes_update()` |
| ☐ | `/v1/product/pictures/import` | Загрузить или обновить изображения товара | `product_pictures_import()` |
| ✓ | `/v3/product/list` | Список товаров | `product_list()` |
| ✓ | `/v1/product/rating-by-sku` | Получить контент-рейтинг товаров по SKU | `product_rating_by_sku()` |
| ✓ | `/v3/product/info/list` | Получить информацию о товарах по идентификаторам | `product_info_list()` |
| ✓ | `/v4/product/info/attributes` | Получить описание характеристик товара | `product_info_attributes()` |
| ✓ | `/v1/product/info/description` | Получить описание товара | `product_info_description()` |
| ☐ | `/v4/product/info/limit` | Лимиты на ассортимент, создание и обновление товаров | `product_info_limit()` |
| ✓ | `/v1/product/update/offer-id` | Изменить артикулы товаров из системы продавца | `product_update_offer_id()` |
| ✓ | `/v1/product/archive` | Перенести товар в архив | `product_archive()` |
| ✓ | `/v1/product/unarchive` | Вернуть товар из архива | `product_unarchive()` |
| ✓ | `/v2/products/delete` | Удалить товар без SKU из архива | `products_delete()` |
| ✓ | `/v1/product/info/subscription` | Количество подписавшихся на товар пользователей | `product_info_subscription()` |
| ✓ | `/v1/product/related-sku/get` | Получить связанные SKU | `product_related_sku_get()` |
| ✓ | `/v2/product/pictures/info` | Получить изображения товаров | `product_pictures_info()` |

## Штрихкоды товаров
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/barcode/add` | Привязать штрихкод к товару | `barcode_add()` |
| ✓ | `/v1/barcode/generate` | Создать штрихкод для товара | `barcode_generate()` |

## Цены и остатки товаров
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/products/stocks` | Обновить количество товаров на складах | `products_stocks()` |
| ✓ | `/v4/product/info/stocks` | Информация о количестве товаров | `product_info_stocks()` |
| ✓ | `/v1/product/info/stocks-by-warehouse/fbs` | Информация об остатках на складах продавца (FBS и rFBS) | `product_info_stocks_by_warehouse_fbs()` |
| ✓ | `/v1/product/import/prices` | Обновить цену | `product_import_prices()` |
| ☐ | `/v1/product/action/timer/update` | Обновление таймера актуальности минимальной цены | `product_action_timer_update()` |
| ☐ | `/v1/product/action/timer/status` | Получить статус установленного таймера | `product_action_timer_status()` |
| ✓ | `/v5/product/info/prices` | Получить информацию о цене товара | `product_info_prices()` |
| ☐ | `/v1/product/info/discounted` | Узнать информацию об уценке и основном товаре по SKU уценённого товара | `product_info_discounted()` |
| ☐ | `/v1/product/update/discount` | Установить скидку на уценённый товар | `product_update_discount()` |

## Акции
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/actions` | Список акций | `actions()` |
| ☐ | `/v1/actions/candidates` | Список доступных для акции товаров | `actions_candidates()` |
| ☐ | `/v1/actions/products` | Список участвующих в акции товаров | `actions_products()` |
| ☐ | `/v1/actions/products/activate` | Добавить товар в акцию | `actions_products_activate()` |
| ☐ | `/v1/actions/products/deactivate` | Удалить товары из акции | `actions_products_deactivate()` |
| ☐ | `/v1/actions/discounts-task/list` | Список заявок на скидку | `actions_discounts_task_list()` |
| ☐ | `/v1/actions/discounts-task/approve` | Согласовать заявку на скидку | `actions_discounts_task_approve()` |
| ☐ | `/v1/actions/discounts-task/decline` | Отклонить заявку на скидку | `actions_discounts_task_decline()` |

## Стратегии ценообразования
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/pricing-strategy/competitors/list` | Список конкурентов | `pricing_strategy_competitors_list()` |
| ☐ | `/v1/pricing-strategy/list` | Список стратегий | `pricing_strategy_list()` |
| ☐ | `/v1/pricing-strategy/create` | Создать стратегию | `pricing_strategy_create()` |
| ☐ | `/v1/pricing-strategy/info` | Информация о стратегии | `pricing_strategy_info()` |
| ☐ | `/v1/pricing-strategy/update` | Обновить стратегию | `pricing_strategy_update()` |
| ☐ | `/v1/pricing-strategy/products/add` | Добавить товары в стратегию | `pricing_strategy_products_add()` |
| ☐ | `/v1/pricing-strategy/strategy-ids-by-product-ids` | Список идентификаторов стратегий | `pricing_strategy_strategy_ids_by_product_ids()` |
| ☐ | `/v1/pricing-strategy/products/list` | Список товаров в стратегии | `pricing_strategy_products_list()` |
| ☐ | `/v1/pricing-strategy/product/info` | Цена товара у конкурента | `pricing_strategy_product_info()` |
| ☐ | `/v1/pricing-strategy/products/delete` | Удалить товары из стратегии | `pricing_strategy_products_delete()` |
| ☐ | `/v1/pricing-strategy/status` | Изменить статус стратегии | `pricing_strategy_status()` |
| ☐ | `/v1/pricing-strategy/delete` | Удалить стратегию | `pricing_strategy_delete()` |

## Сертификаты брендов
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/brand/company-certification/list` | Список сертифицируемых брендов | `brand_company_certification_list()` |

## Сертификаты качества
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/product/certificate/accordance-types` | Список типов соответствия требований (версия 1) | `product_certificate_accordance_types()` |
| ☐ | `/v2/product/certificate/accordance-types/list` | Список типов соответствия требований (версия 2) | `product_certificate_accordance_types_list()` |
| ☐ | `/v1/product/certificate/types` | Справочник типов документов | `product_certificate_types()` |
| ☐ | `/v2/product/certification/list` | Список сертифицируемых категорий | `product_certification_list()` |
| ☐ | `/v1/product/certificate/create` | Добавить сертификаты для товаров | `product_certificate_create()` |
| ☐ | `/v1/product/certificate/bind` | Привязать сертификат к товару | `product_certificate_bind()` |
| ☐ | `/v1/product/certificate/delete` | Удалить сертификат | `product_certificate_delete()` |
| ☐ | `/v1/product/certificate/info` | Информация о сертификате | `product_certificate_info()` |
| ☐ | `/v1/product/certificate/list` | Список сертификатов | `product_certificate_list()` |
| ☐ | `/v1/product/certificate/product_status/list` | Список возможных статусов товаров | `product_certificate_product_status_list()` |
| ☐ | `/v1/product/certificate/products/list` | Список товаров, привязанных к сертификату | `product_certificate_products_list()` |
| ☐ | `/v1/product/certificate/unbind` | Отвязать товар от сертификата | `product_certificate_unbind()` |
| ☐ | `/v1/product/certificate/rejection_reasons/list` | Возможные причины отклонения сертификата | `product_certificate_rejection_reasons_list()` |
| ☐ | `/v1/product/certificate/status/list` | Возможные статусы сертификатов | `product_certificate_status_list()` |

## Склады
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v1/warehouse/list` | Список складов | `warehouse_list()` |
| ✓ | `/v1/delivery-method/list` | Список методов доставки склада | `delivery_method_list()` |

## Обработка заказов FBS и rFBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ✓ | `/v3/posting/fbs/unfulfilled/list` | Список необработанных отправлений | `posting_fbs_unfulfilled_list()` |
| ☐ | `/v3/posting/fbs/list` | Список отправлений | `posting_fbs_list()` |
| ☐ | `/v3/posting/fbs/get` | Получить информацию об отправлении по идентификатору | `posting_fbs_get()` |
| ☐ | `/v2/posting/fbs/get-by-barcode` | Получить информацию об отправлении по штрихкоду | `posting_fbs_get_by_barcode()` |
| ☐ | `/v3/posting/multiboxqty/set` | Указать количество коробок для многокоробочных отправлений | `posting_multiboxqty_set()` |
| ☐ | `/v2/posting/fbs/product/change` | Добавить вес для весовых товаров в отправлении | `posting_fbs_product_change()` |
| ☐ | `/v2/posting/fbs/product/country/list` | Список доступных стран-изготовителей | `posting_fbs_product_country_list()` |
| ☐ | `/v2/posting/fbs/product/country/set` | Добавить информацию о стране-изготовителе товара | `posting_fbs_product_country_set()` |
| ☐ | `/v1/posting/fbs/restrictions` | Получить ограничения пункта приёма | `posting_fbs_restrictions()` |
| ☐ | `/v2/posting/fbs/package-label` | Напечатать этикетку | `posting_fbs_package_label()` |
| ☐ | `/v2/posting/fbs/package-label/create` | Создать задание на формирование этикеток | `posting_fbs_package_label_create()` |
| ☐ | `/v1/posting/fbs/package-label/get` | Получить файл с этикетками | `posting_fbs_package_label_get()` |
| ☐ | `/v1/posting/fbs/cancel-reason` | Причины отмены отправления | `posting_fbs_cancel_reason()` |
| ☐ | `/v2/posting/fbs/cancel-reason/list` | Причины отмены отправлений | `posting_fbs_cancel_reason_list()` |
| ☐ | `/v2/posting/fbs/product/cancel` | Отменить отправку некоторых товаров в отправлении | `posting_fbs_product_cancel()` |
| ☐ | `/v2/posting/fbs/cancel` | Отменить отправление | `posting_fbs_cancel()` |
| ☐ | `/v2/posting/fbs/arbitration` | Открыть спор по отправлению | `posting_fbs_arbitration()` |
| ☐ | `/v2/posting/fbs/awaiting-delivery` | Передать отправление к отгрузке | `posting_fbs_awaiting_delivery()` |
| ☐ | `/v1/posting/fbs/pick-up-code/verify` | Проверить код курьера | `posting_fbs_pick_up_code_verify()` |
| ☐ | `/v1/posting/global/etgb` | Таможенные декларации ETGB | `posting_global_etgb()` |
| ☐ | `/v1/posting/unpaid-legal/product/list` | Список неоплаченных товаров, заказанных юридическими лицами | `posting_unpaid_legal_product_list()` |

## Полигоны
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/polygon/create` | Создайте полигон доставки | `polygon_create()` |
| ☐ | `/v1/polygon/bind` | Свяжите метод доставки с полигоном доставки | `polygon_bind()` |

## Доставка FBO
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/posting/fbo/list` | Список отправлений | `posting_fbo_list()` |
| ☐ | `/v2/posting/fbo/get` | Информация об отправлении | `posting_fbo_get()` |
| ☐ | `/v1/posting/fbo/cancel-reason/list` | Причины отмены отправлений по схеме FBO | `posting_fbo_cancel_reason_list()` |
| ☐ | `/v1/supply-order/status/counter` | Количество заявок по статусам | `supply_order_status_counter()` |
| ☐ | `/v1/supply-order/bundle` | Состав поставки или заявки на поставку | `supply_order_bundle()` |
| ☐ | `/v2/supply-order/list` | Список заявок на поставку на склад Ozon | `supply_order_list()` |
| ☐ | `/v2/supply-order/get` | Информация о заявке на поставку | `supply_order_get()` |
| ☐ | `/v1/supply-order/timeslot/get` | Интервалы поставки | `supply_order_timeslot_get()` |
| ☐ | `/v1/supply-order/timeslot/update` | Обновить интервал поставки | `supply_order_timeslot_update()` |
| ☐ | `/v1/supply-order/timeslot/status` | Статус интервала поставки | `supply_order_timeslot_status()` |
| ☐ | `/v1/supply-order/pass/create` | Указать данные о водителе и автомобиле | `supply_order_pass_create()` |
| ☐ | `/v1/supply-order/pass/status` | Статус ввода данных о водителе и автомобиле | `supply_order_pass_status()` |
| ☐ | `/v1/supplier/available_warehouses` | Загруженность складов Ozon | `supplier_available_warehouses()` |

## Создание и управление заявками на поставку FBO
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/cluster/list` | Информация о кластерах и их складах | `cluster_list()` |
| ☐ | `/v1/warehouse/fbo/list` | Поиск точек для отгрузки поставки | `warehouse_fbo_list()` |
| ☐ | `/v1/draft/create` | Создать черновик заявки на поставку | `draft_create()` |
| ☐ | `/v1/draft/create/info` | Информация о черновике заявки на поставку | `draft_create_info()` |
| ☐ | `/v1/draft/timeslot/info` | Доступные таймслоты | `draft_timeslot_info()` |
| ☐ | `/v1/draft/supply/create` | Создать заявку на поставку по черновику | `draft_supply_create()` |
| ☐ | `/v1/draft/supply/create/status` | Информация о создании заявки на поставку | `draft_supply_create_status()` |
| ☐ | `/v1/cargoes/create` | Установка грузомест | `cargoes_create()` |
| ☐ | `/v2/cargoes/create/info` | Получить информацию по установке грузомест | `cargoes_create_info()` |
| ☐ | `/v1/cargoes/delete` | Удалить грузоместо в заявке на поставку | `cargoes_delete()` |
| ☐ | `/v1/cargoes/delete/status` | Информация о статусе удаления грузоместа | `cargoes_delete_status()` |
| ☐ | `/v1/cargoes/rules/get` | Чек-лист по установке грузомест FBO | `cargoes_rules_get()` |
| ☐ | `/v1/cargoes-label/create` | Сгенерировать этикетки для грузомест | `cargoes_label_create()` |
| ☐ | `/v1/cargoes-label/get` | Получить идентификатор этикетки для грузомест | `cargoes_label_get()` |
| ☐ | `/v1/cargoes-label/file/{file_guid}` | Получить PDF с этикетками грузовых мест | `cargoes_label_file()` |
| ☐ | `/v1/supply-order/cancel` | Отменить заявку на поставку | `supply_order_cancel()` |
| ☐ | `/v1/supply-order/cancel/status` | Получить статус отмены заявки на поставку | `supply_order_cancel_status()` |
| ☐ | `/v1/supply-order/content/update` | Редактирование товарного состава | `supply_order_content_update()` |
| ☐ | `/v1/supply-order/content/update/status` | Информация о статусе редактирования товарного состава | `supply_order_content_update_status()` |

## Управление кодами маркировки и сборкой заказов для FBS/rFBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v6/fbs/posting/product/exemplar/create-or-get` | Получить данные созданных экземпляров | `fbs_posting_product_exemplar_create_or_get()` |
| ☐ | `/v5/fbs/posting/product/exemplar/validate` | Валидация кодов маркировки | `fbs_posting_product_exemplar_validate()` |
| ☐ | `/v6/fbs/posting/product/exemplar/set` | Проверить и сохранить данные экземпляров | `fbs_posting_product_exemplar_set()` |
| ☐ | `/v5/fbs/posting/product/exemplar/status` | Получить статус добавления экземпляров | `fbs_posting_product_exemplar_status()` |
| ☐ | `/v4/posting/fbs/ship` | Собрать заказ (версия 4) | `posting_fbs_ship()` |
| ☐ | `/v4/posting/fbs/ship/package` | Частичная сборка отправления (версия 4) | `posting_fbs_ship_package()` |
| ☐ | `/v1/fbs/posting/product/exemplar/update` | Обновить данные экземпляров | `fbs_posting_product_exemplar_update()` |

## Доставка FBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/carriage/create` | Создание отгрузки | `carriage_create()` |
| ☐ | `/v1/carriage/approve` | Подтверждение отгрузки | `carriage_approve()` |
| ☐ | `/v1/carriage/set-postings` | Изменение состава отгрузки | `carriage_set_postings()` |
| ☐ | `/v1/carriage/cancel` | Удаление отгрузки | `carriage_cancel()` |
| ☐ | `/v1/carriage/delivery/list` | Список методов доставки и отгрузок | `carriage_delivery_list()` |
| ☐ | `/v2/posting/fbs/act/create` | Подтвердить отгрузку и создать документы | `posting_fbs_act_create()` |
| ☐ | `/v1/posting/carriage-available/list` | Список доступных перевозок | `posting_carriage_available_list()` |
| ☐ | `/v1/carriage/get` | Информация о перевозке | `carriage_get()` |
| ☐ | `/v1/posting/fbs/split` | Разделить заказ на отправления без сборки | `posting_fbs_split()` |
| ☐ | `/v2/posting/fbs/act/get-postings` | Список отправлений в акте | `posting_fbs_act_get_postings()` |
| ☐ | `/v2/posting/fbs/act/get-container-labels` | Этикетки для грузового места | `posting_fbs_act_get_container_labels()` |
| ☐ | `/v2/posting/fbs/act/get-barcode` | Штрихкод для отгрузки отправления | `posting_fbs_act_get_barcode()` |
| ☐ | `/v2/posting/fbs/act/get-barcode/text` | Значение штрихкода для отгрузки отправления | `posting_fbs_act_get_barcode_text()` |
| ☐ | `/v2/posting/fbs/digital/act/check-status` | Статус формирования накладной | `posting_fbs_digital_act_check_status()` |
| ☐ | `/v2/posting/fbs/act/get-pdf` | Получить PDF c документами | `posting_fbs_act_get_pdf()` |
| ☐ | `/v2/posting/fbs/act/list` | Список актов по отгрузкам | `posting_fbs_act_list()` |
| ☐ | `/v2/posting/fbs/digital/act/get-pdf` | Получить лист отгрузки по перевозке | `posting_fbs_digital_act_get_pdf()` |
| ☐ | `/v2/posting/fbs/act/check-status` | Статус отгрузки и документов | `posting_fbs_act_check_status()` |

## Доставка rFBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/fbs/posting/tracking-number/set` | Добавить трек-номера | `fbs_posting_tracking_number_set()` |
| ☐ | `/v2/fbs/posting/sent-by-seller` | Изменить статус на «Отправлено продавцом» | `fbs_posting_sent_by_seller()` |
| ☐ | `/v2/fbs/posting/delivering` | Изменить статус на «Доставляется» | `fbs_posting_delivering()` |
| ☐ | `/v2/fbs/posting/last-mile` | Изменить статус на «Последняя миля» | `fbs_posting_last_mile()` |
| ☐ | `/v2/fbs/posting/delivered` | Изменить статус на «Доставлено» | `fbs_posting_delivered()` |
| ☐ | `/v1/posting/fbs/timeslot/change-restrictions` | Доступные даты для переноса доставки | `posting_fbs_timeslot_change_restrictions()` |
| ☐ | `/v1/posting/fbs/timeslot/set` | Перенести дату доставки | `posting_fbs_timeslot_set()` |
| ☐ | `/v1/posting/cutoff/set` | Уточнить дату отгрузки отправления | `posting_cutoff_set()` |

## Пропуски
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/pass/list` | Список пропусков | `pass_list()` |
| ☐ | `/v1/carriage/pass/create` | Создать пропуск | `carriage_pass_create()` |
| ☐ | `/v1/carriage/pass/update` | Обновить пропуск | `carriage_pass_update()` |
| ☐ | `/v1/carriage/pass/delete` | Удалить пропуск | `carriage_pass_delete()` |
| ☐ | `/v1/return/pass/create` | Создать пропуск для возврата | `return_pass_create()` |
| ☐ | `/v1/return/pass/update` | Обновить пропуск для возврата | `return_pass_update()` |
| ☐ | `/v1/return/pass/delete` | Удалить пропуск для возврата | `return_pass_delete()` |

## Возвраты товаров FBO и FBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/returns/list` | Информация о возвратах FBO и FBS | `returns_list()` |

## Возвраты товаров rFBS
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/returns/rfbs/list` | Список заявок на возврат | `returns_rfbs_list()` |
| ☐ | `/v2/returns/rfbs/get` | Информация о заявке на возврат | `returns_rfbs_get()` |
| ☐ | `/v2/returns/rfbs/reject` | Отклонить заявку на возврат | `returns_rfbs_reject()` |
| ☐ | `/v2/returns/rfbs/compensate` | Вернуть часть стоимости товара | `returns_rfbs_compensate()` |
| ☐ | `/v2/returns/rfbs/verify` | Одобрить заявку на возврат | `returns_rfbs_verify()` |
| ☐ | `/v2/returns/rfbs/receive-return` | Подтвердить получение товара на проверку | `returns_rfbs_receive_return()` |
| ☐ | `/v2/returns/rfbs/return-money` | Вернуть деньги покупателю | `returns_rfbs_return_money()` |
| ☐ | `/v1/returns/rfbs/action/set` | Передать доступные действия для rFBS возвратов | `returns_rfbs_action_set()` |

## Возвратные отгрузки
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/returns/company/fbs/info` | Количество возвратов FBS | `returns_company_fbs_info()` |
| ☐ | `/v1/return/giveout/is-enabled` | Проверить возможность получения возвратных отгрузок по штрихкоду | `return_giveout_is_enabled()` |
| ☐ | `/v1/return/giveout/list` | Список возвратных отгрузки | `return_giveout_list()` |
| ☐ | `/v1/return/giveout/info` | Информация о возвратной отгрузке | `return_giveout_info()` |
| ☐ | `/v1/return/giveout/barcode` | Значение штрихкода для возвратных отгрузок | `return_giveout_barcode()` |
| ☐ | `/v1/return/giveout/get-pdf` | Штрихкод для получения возвратной отгрузки в формате PDF | `return_giveout_get_pdf()` |
| ☐ | `/v1/return/giveout/get-png` | Штрихкод для получения возвратной отгрузки в формате PNG | `return_giveout_get_png()` |
| ☐ | `/v1/return/giveout/barcode-reset` | Сгенерировать новый штрихкод | `return_giveout_barcode_reset()` |

## Отмены заказов
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/conditional-cancellation/list` | Получить список заявок на отмену rFBS | `conditional_cancellation_list()` |
| ☐ | `/v2/conditional-cancellation/approve` | Подтвердить заявку на отмену rFBS | `conditional_cancellation_approve()` |
| ☐ | `/v2/conditional-cancellation/reject` | Отклонить заявку на отмену rFBS | `conditional_cancellation_reject()` |

## Чаты с покупателями
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/chat/send/file` | Отправить файл | `chat_send_file()` |
| ☐ | `/v3/chat/list` | Список чатов | `chat_list()` |
| ☐ | `/v2/chat/history` | История чата | `chat_history()` |

## Накладные
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/invoice/create-or-update` | Создать или изменить счёт-фактуру | `invoice_create_or_update()` |
| ☐ | `/v1/invoice/file/upload` | Загрузка счёта-фактуры | `invoice_file_upload()` |
| ☐ | `/v2/invoice/get` | Получить информацию о счёте-фактуре | `invoice_get()` |
| ☐ | `/v1/invoice/delete` | Удалить ссылку на счёт-фактуру | `invoice_delete()` |

## Отчёты
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/report/info` | Информация об отчёте | `report_info()` |
| ☐ | `/v1/report/list` | Список отчётов | `report_list()` |
| ☐ | `/v1/report/products/create` | Отчёт по товарам | `report_products_create()` |
| ☐ | `/v2/report/returns/create` | Отчёт о возвратах | `report_returns_create()` |
| ☐ | `/v1/report/postings/create` | Отчёт об отправлениях | `report_postings_create()` |
| ☐ | `/v1/finance/cash-flow-statement/list` | Финансовый отчёт | `finance_cash_flow_statement_list()` |
| ☐ | `/v1/report/discounted/create` | Отчёт об уценённых товарах | `report_discounted_create()` |
| ☐ | `/v1/report/warehouse/stock` | Отчёт об остатках на FBS-складе | `report_warehouse_stock()` |

## Аналитические отчёты
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/analytics/stock_on_warehouses` | Отчёт по остаткам и товарам | `analytics_stock_on_warehouses()` |
| ☐ | `/v1/analytics/turnover/stocks` | Оборачиваемость товара | `analytics_turnover_stocks()` |

## Финансовые отчёты
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v2/finance/realization` | Отчёт о реализации товаров (версия 2) | `finance_realization()` |
| ☐ | `/v1/finance/realization/posting` | Позаказный отчёт о реализации товаров | `finance_realization_posting()` |
| ☐ | `/v3/finance/transaction/list` | Список транзакций | `finance_transaction_list()` |
| ☐ | `/v3/finance/transaction/totals` | Суммы транзакций | `finance_transaction_totals()` |
| ☐ | `/v1/finance/document-b2b-sales` | Реестр продаж юридическим лицам | `finance_document_b2b_sales()` |
| ☐ | `/v1/finance/document-b2b-sales/json` | Реестр продаж юридическим лицам в JSON-формате | `finance_document_b2b_sales_json()` |
| ☐ | `/v1/finance/mutual-settlement` | Отчёт о взаиморасчётах | `finance_mutual_settlement()` |
| ☐ | `/v1/finance/products/buyout` | Отчёт о выкупах | `finance_products_buyout()` |
| ☐ | `/v1/finance/order/acceptance` | Отчёт о принятии заказа | `finance_order_acceptance()` |
| ☐ | `/v1/finance/order/acceptance/act` | Акт об оказании услуг | `finance_order_acceptance_act()` |
| ☐ | `/v1/finance/order/acceptance/act/upload` | Загрузить подписанный акт | `finance_order_acceptance_act_upload()` |
| ☐ | `/v1/finance/order/acceptance/act/status` | Статус акта | `finance_order_acceptance_act_status()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm` | Подтвердить акт | `finance_order_acceptance_act_confirm()` |
| ☐ | `/v1/finance/order/acceptance/act/reject` | Отклонить акт | `finance_order_acceptance_act_reject()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject` | Отменить отклонение акта | `finance_order_acceptance_act_confirm_reject()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/status` | Статус подтверждения акта | `finance_order_acceptance_act_confirm_status()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject/status` | Статус отмены отклонения акта | `finance_order_acceptance_act_confirm_reject_status()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject/cancel` | Отменить отмену отклонения акта | `finance_order_acceptance_act_confirm_reject_cancel()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject/cancel/status` | Статус отмены отмены отклонения акта | `finance_order_acceptance_act_confirm_reject_cancel_status()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject/cancel/revert` | Отменить отмену отмены отклонения акта | `finance_order_acceptance_act_confirm_reject_cancel_revert()` |
| ☐ | `/v1/finance/order/acceptance/act/confirm/reject/cancel/revert/status` | Статус отмены отмены отмены отклонения акта | `finance_order_acceptance_act_confirm_reject_cancel_revert_status()` |

## Управление компанией
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/company/list` | Список компаний | `company_list()` |

## Управление API-ключами
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/api-key/list` | Список API-ключей | `api_key_list()` |
| ☐ | `/v1/api-key/create` | Создать API-ключ | `api_key_create()` |
| ☐ | `/v1/api-key/delete` | Удалить API-ключ | `api_key_delete()` |

## Управление уведомлениями
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|---|---|---|---|
| ☐ | `/v1/notification/settings` | Настройки уведомлений | `notification_settings()` |
| ☐ | `/v1/notification/settings/update` | Обновить настройки уведомлений | `notification_settings_update()` |

## Логистика
| ✓ | Адрес метода Ozon | Описание метода | Python-метод |
|--|---|---|---|
| ☐ | `/v1/logistic/order/status` | Получить статус заказа в логистике | `logistic_order_status()` |
| ☐ | `/v1/logistic/order/status/history` | Получить историю статусов заказа в логистике | `logistic_order_status_history()` |
| ☐ | `/v1/logistic/order/tracking` | Получить информацию об отслеживании заказа | `logistic_order_tracking()` |
| ☐ | `/v1/logistic/order/cancel` | Отменить заказ в логистике | `logistic_order_cancel()` |
| ☐ | `/v1/logistic/order/create` | Создать заказ в логистике | `logistic_order_create()` |
| ☐ | `/v1/logistic/order/update` | Обновить заказ в логистике | `logistic_order_update()` |
| ☐ | `/v1/logistic/order/info` | Получить информацию о заказе в логистике | `logistic_order_info()` |
| ☐ | `/v1/logistic/order/list` | Получить список заказов в логистике | `logistic_order_list()` |
| ☐ | `/v1/logistic/city/list` | Получить список городов | `logistic_city_list()` |
| ☐ | `/v1/logistic/city/info` | Получить информацию о городе | `logistic_city_info()` |
| ☐ | `/v1/logistic/point/list` | Получить список пунктов выдачи | `logistic_point_list()` |
| ☐ | `/v1/logistic/point/info` | Получить информацию о пункте выдачи | `logistic_point_info()` |
| ☐ | `/v1/logistic/tariff/list` | Получить список тарифов | `logistic_tariff_list()` |
| ☐ | `/v1/logistic/tariff/info` | Получить информацию о тарифе | `logistic_tariff_info()` |
| ☐ | `/v1/logistic/tariff/calculate` | Рассчитать стоимость доставки | `logistic_tariff_calculate()` |
| ☐ | `/v1/logistic/address/list` | Получить список адресов | `logistic_address_list()` |
| ☐ | `/v1/logistic/address/create` | Создать адрес | `logistic_address_create()` |
| ☐ | `/v1/logistic/address/update` | Обновить адрес | `logistic_address_update()` |
| ☐ | `/v1/logistic/address/delete` | Удалить адрес | `logistic_address_delete()` |
| ☐ | `/v1/logistic/address/info` | Получить информацию об адресе | `logistic_address_info()` |

## Примечания
- ✓ - метод реализован
- ☐ - метод не реализован


[MIT License](LICENSE)

---

*Проект не аффилирован с Ozon. Все торговые марки принадлежат их правообладателям.*
