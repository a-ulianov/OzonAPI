"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ImportProductsBySKU"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.prices import VAT


class ProductImportBySkuRequestItem(BaseModel):
    """Информация о товаре.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU, карточку которого необходимо дублировать
        name: Название товара (опционально, до 500 символов)
        offer_id: Идентификатор товара в системе продавца - артикул (опционально, до 50 символов)
        old_price: Цена до скидок, будет зачеркнута на карточке товара (опционально)
        price: Цена товара с учётом скидок, отображается на карточке товара (опционально, если на товар нет скидок, укажите значение old_price в этом параметре)
        vat: НДС (опционально, допустимые значения: `0`, `0.05`, `0.07`, `0.1`, `0.2`, `0.22`)
        currency_code: Переданное значение должно совпадать с валютой, которая установлена в настройках личного кабинета (опционально, по умолчанию передаётся RUB — российский рубль)
    """
    name: Optional[str] = Field(
        None, description="Название товара. До 500 символов.", title="Название",
        max_length=500,
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул. Максимальная длина строки — 50 символов.",
        max_length=50,
    )
    old_price: Optional[str] = Field(
        None, description="Цена до скидок (будет зачеркнута на карточке товара). Указывается в рублях. Разделитель дробной части — точка, до двух знаков после точки.",
    )
    price: Optional[str] = Field(
        None, description="Цена товара с учётом скидок, отображается на карточке товара. Если на товар нет скидок, укажите значение old_price в этом параметре.",
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU.",
    )
    vat: Optional[VAT] = Field(
        None, description="Ставка НДС на товар.",
    )
    currency_code: Optional[CurrencyCode] = Field(
        CurrencyCode.RUB, description="Переданное значение должно совпадать с валютой, которая установлена в настройках личного кабинета. По умолчанию передаётся RUB — российский рубль.",
    )


class ProductImportBySkuRequest(BaseModel):
    """Описывает схему запроса на создание копии товарной карточки по SKU.

    Attributes:
        items: Массив с информацией о товарах (максимум 1000 элементов)
    """
    items: list[ProductImportBySkuRequestItem] = Field(
        ..., description="Массив с информацией о товарах (максимум 1000 элементов).",
        max_length=1000,
    )


class ProductImportBySkuResponse(BaseModel):
    """Описывает схему ответа на запрос о создании копии товарной карточки по SKU.

    Attributes:
        task_id: Код задачи на импорт товаров
        unmatched_sku_list: Неупорядоченный список идентификаторов товаров в системе продавца — product_id
    """
    task_id: int = Field(
        ..., description="Код задачи на импорт товаров."
    )
    unmatched_sku_list: list[int] = Field(
        ..., description="Список идентификаторов товаров в системе продавца — product_id."
    )