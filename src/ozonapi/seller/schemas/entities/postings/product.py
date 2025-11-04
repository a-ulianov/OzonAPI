from pydantic import BaseModel, Field

from ....common.enumerations.localization import CurrencyCode


class PostingProduct(BaseModel):
    """Информация о товаре в отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
    """
    name: str = Field(
        ..., description="Название товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    price: float = Field(
        ..., description="Цена товара."
    )
    quantity: int = Field(
        ..., description="Количество товара в отправлении."
    )
    sku: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class PostingProductWithCurrencyCode(PostingProduct):
    """Информация о товаре в отправлении.

    Attributes:
        name: Название товара
        offer_id: Идентификатор товара в системе продавца
        price: Цена товара
        quantity: Количество товара в отправлении
        sku: Идентификатор товара в системе Ozon
        currency_code: Валюта цен
    """
    currency_code: CurrencyCode = Field(
        ..., description="Валюта ваших цен. Совпадает с валютой, которая установлена в настройках личного кабинета."
    )
