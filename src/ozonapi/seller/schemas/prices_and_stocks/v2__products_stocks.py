"""https://docs.ozon.com/api/seller/#operation/ProductAPI_ProductsStocksV2"""
from typing import Optional
from pydantic import BaseModel, Field, model_validator


class ProductsStocksItem(BaseModel):
    """Схема для элемента остатков товара на складе FBS или rFBS в запросе.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул (опционально)
        product_id: Идентификатор товара в системе Ozon — product_id (опционально)
        stock: Количество товара в наличии без учёта зарезервированных товаров (свободный остаток)
        warehouse_id: Идентификатор склада (можно получить методом warehouse_list())
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    stock: int = Field(
        ..., description="Количество товара в наличии без учёта зарезервированных товаров (свободный остаток).",
        ge=0
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада, полученный из метода warehouse_list()."
    )

    @model_validator(mode='after')
    def validate_offer_or_product_id(self) -> 'ProductsStocksItem':
        """Проверяет, что указан хотя бы один идентификатор товара."""
        if not self.offer_id and not self.product_id:
            raise ValueError("Должен быть указан хотя бы один из параметров: offer_id или product_id")
        return self


class ProductsStocksRequest(BaseModel):
    """Схема запроса на обновление остатков товаров на складах FBS и rFBS.

    Attributes:
        stocks: Массив информации об остатках товаров (максимум 100 элементов)
    """
    stocks: list[ProductsStocksItem] = Field(
        ..., description="Информация о товарах на складах.",
        min_length=1, max_length=100
    )


class ProductsStocksError(BaseModel):
    """Схема для ошибки при обновлении остатков.

    Attributes:
        code: Код ошибки
        message: Сообщение об ошибке
    """
    code: Optional[str] = Field(
        None, description="Код ошибки."
    )
    message: Optional[str] = Field(
        None, description="Причина ошибки."
    )


class ProductsStocksResultItem(BaseModel):
    """Схема для элемента результата обновления остатков.

    Attributes:
        warehouse_id: Идентификатор склада
        product_id: Идентификатор товара в системе Ozon
        offer_id: Идентификатор товара в системе продавца
        updated: Статус обновления
        errors: Массив ошибок
    """
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    updated: bool = Field(
        ..., description="Если запрос выполнен успешно и остатки обновлены — true."
    )
    errors: list[ProductsStocksError] = Field(
        default_factory=list, description="Массив ошибок, которые возникли при обработке запроса."
    )


class ProductsStocksResponse(BaseModel):
    """Схема ответа на запрос обновления остатков.

    Attributes:
        result: Массив результатов обработки запросов
    """
    result: list[ProductsStocksResultItem] = Field(
        ..., description="Список статусов и возможных ошибок."
    )