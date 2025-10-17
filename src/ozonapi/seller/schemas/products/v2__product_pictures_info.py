"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductInfoPicturesV2"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductPicturesInfoRequest(BaseModel):
    """Схема запроса для получения информации об изображениях товаров.

    Attributes:
        product_id: Список идентификаторов товаров
    """
    product_id: list[int] = Field(
        ..., description="Список идентификаторов товаров в системе продавца — product_id.",
        min_length=1, max_length=1000,
    )


class ProductPicturesInfoError(BaseModel):
    """Схема ошибки при получении информации об изображениях товара.

    Attributes:
        url: Ссылка на изображение
        message: Описание ошибки
    """
    url: int = Field(
        ..., description="Ссылка на изображение."
    )
    message: str = Field(
        ..., description="Описание ошибки."
    )


class ProductPicturesInfoItem(BaseModel):
    """Схема с информацией об изображениях одного товара.

    Attributes:
        product_id: Идентификатор товара в системе продавца
        primary_photo: Ссылка на главное изображение
        photo: Ссылки на фотографии товара
        color_photo: Ссылки на загруженные образцы цвета
        photo_360: Ссылки на изображения 360
        errors: Список ошибок по изображениям товара
    """
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — product_id."
    )
    primary_photo: list[str] = Field(
        default_factory=list, description="Ссылка на главное изображение."
    )
    photo: list[str] = Field(
        default_factory=list, description="Ссылки на фотографии товара."
    )
    color_photo: list[str] = Field(
        default_factory=list, description="Ссылки на загруженные образцы цвета."
    )
    photo_360: list[str] = Field(
        default_factory=list, description="Ссылки на изображения 360."
    )
    errors: Optional[list[ProductPicturesInfoError]] = Field(
        default_factory=list, description="Список ошибок по изображениям товара."
    )


class ProductPicturesInfoResponse(BaseModel):
    """Схема ответа с информацией об изображениях товаров и ошибках.

    Attributes:
        items: Изображения товаров
    """
    items: list[ProductPicturesInfoItem] = Field(
        default_factory=list, description="Изображения товаров."
    )