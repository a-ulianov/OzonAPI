"""https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductImportPictures"""
from typing import Optional

from pydantic import BaseModel, Field


class ProductPicturesImportRequest(BaseModel):
    """Описывает схему запроса на добавление или обновление изображений в товарной карточке.

    Attributes:
        color_image: Маркетинговый цвет (опционально)
        images: Массив ссылок на изображения (опционально, до 30 штук; изображения в массиве расположены в порядке их расположения на сайте; первое изображение в массиве будет главным)
        images360: УСТАРЕЛО — Ozon удалил поле из запроса метода (live-спецификация от 2026-07-11); сохранено для обратной совместимости, но API его больше не принимает и игнорирует
        product_id: Идентификатор товара в системе продавца — product_id
    """
    color_image: Optional[str] = Field(
        None, description="Маркетинговый цвет."
    )
    images: Optional[list[str]] = Field(
        default_factory=list, description="""
        Массив ссылок на изображения (до 30 штук; изображения в массиве расположены в порядке их
        расположения на сайте; первое изображение в массиве будет главным).
        """,
        max_length=30,
    )
    images360: Optional[list[str]] = Field(
        default_factory=list, description=(
            "УСТАРЕЛО. Ozon удалил это поле из запроса метода "
            "(live-спецификация от 2026-07-11): API его больше не принимает и игнорирует. "
            "Поле сохранено для обратной совместимости и будет удалено в будущем "
            "мажорном релизе. Массив изображений 360 (до 70 штук)."
        ),
        max_length=70,
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца."
    )


class ProductPicturesImportPicture(BaseModel):
    """Описывает схему результата добавления изображения.

    Attributes:
          is_360: Признак, что картинка — изображение 360
          is_color: Признак, что картинка — образец цвета
          is_primary: Признак, что картинка — главное изображение
          product_id: Идентификатор товара в системе продавца
          state: Статус загрузки изображения
          url: Адрес ссылки на изображение в общедоступном облачном хранилище (формат изображения по ссылке — JPG или PNG)
    """
    is_360: Optional[bool] = Field(
        None, description="Признак, что картинка — изображение 360."
    )
    is_color: Optional[bool] = Field(
        None, description="Признак, что картинка — образец цвета."
    )
    is_primary: Optional[bool] = Field(
        None, description="Признак, что картинка — главное изображение."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    state: str = Field(
        ..., description="Статус загрузки изображения."
    )
    url: Optional[str] = Field(
        None, description="Адрес ссылки на изображение в общедоступном облачном хранилище (формат изображения по ссылке — JPG или PNG)."
    )


class ProductPicturesImportResult(BaseModel):
    """Описывает схему результата добавление изображений.

    Attributes:
        pictures: Массив признаков загруженного контента, статусов и ссылок на изображения
    """
    pictures: list[ProductPicturesImportPicture] = Field(
        default_factory=list, description="Массив признаков загруженного контента, статусов и ссылок на изображения."
    )


class ProductPicturesImportResponse(BaseModel):
    """Описывает схему ответа на запрос на добавление или обновление изображений в товарной карточке.

    Attributes:
        result: Результат работы метода
    """
    result: ProductPicturesImportResult = Field(
        ..., description="Результат работы метода."
    )