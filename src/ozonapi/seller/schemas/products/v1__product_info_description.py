"""https://docs.ozon.ru/api/seller/?#operation/ProductAPI_GetProductInfoDescription"""
from typing import Optional

from pydantic import BaseModel, Field, model_validator


class ProductInfoDescriptionRequest(BaseModel):
    """Описывает схему запроса на получение описания товара.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул (опционально, если указан product_id)
        product_id: Идентификатор товара в системе продавца — product_id (опционально, если указан offer_id)
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе продавца — product_id."
    )

    @model_validator(mode='after')
    def validate_product_identifier(self) -> 'ProductInfoDescriptionRequest':
        if not self.offer_id and not self.product_id:
            raise ValueError(
                "Должен быть использован один из идентификаторов: offer_id или product_id."
            )

        return self


class ProductInfoDescriptionResult(BaseModel):
    """Информация о товаре с описанием.

    Attributes:
        description: Описание товара
        id: Идентификатор товара (product_id)
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
    """
    description: str = Field(
        ..., description="Описание товара."
    )
    id: int = Field(
        ..., description="Идентификатор товара (product_id)."
    )
    name: str = Field(
        ..., description="Название товара."
    )
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )


class ProductInfoDescriptionResponse(BaseModel):
    """Описывает схему ответа на запрос о получении описания товара.

    Attributes:
        result: Объект с информацией о товаре и описанием
    """
    result: ProductInfoDescriptionResult = Field(
        ..., description="Объект с информацией о товаре и описанием."
    )