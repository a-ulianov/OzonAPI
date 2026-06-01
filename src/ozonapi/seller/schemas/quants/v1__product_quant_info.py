"""Схемы метода product_quant_info (информация об эконом-товаре, v1)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class ProductQuantInfoRequest(BaseModel):
    """Параметры запроса информации об эконом-товарах.

    Attributes:
        quant_code: Список идентификаторов квантов (от 1 до 1000)
    """
    quant_code: list[str] = Field(
        ..., description="Список идентификаторов квантов (от 1 до 1000)."
    )


class ProductQuantInfoBarcode(BaseModel):
    """Информация о штрихкоде кванта.

    Attributes:
        barcode: Штрихкод
        error: Ошибка получения штрихкода
        status: Статус штрихкода
    """
    barcode: Optional[str] = Field(None, description="Штрихкод.")
    error: Optional[str] = Field(None, description="Ошибка получения штрихкода.")
    status: Optional[str] = Field(None, description="Статус штрихкода.")


class ProductQuantInfoDimensions(BaseModel):
    """Габариты кванта.

    Attributes:
        depth: Глубина, мм
        height: Высота, мм
        weight: Вес, г
        width: Ширина, мм
    """
    depth: Optional[int] = Field(None, description="Глубина, мм.")
    height: Optional[int] = Field(None, description="Высота, мм.")
    weight: Optional[int] = Field(None, description="Вес, г.")
    width: Optional[int] = Field(None, description="Ширина, мм.")


class ProductQuantInfoMarketingPrice(BaseModel):
    """Маркетинговая цена кванта.

    Attributes:
        price: Цена продажи
        seller_price: Цена, которую указал продавец
    """
    price: Optional[str] = Field(None, description="Цена продажи.")
    seller_price: Optional[str] = Field(
        None, description="Цена, которую указал продавец."
    )


class ProductQuantInfoStatuses(BaseModel):
    """Статус кванта.

    Attributes:
        state_description: Описание статуса
        state_name: Название статуса
        state_sys_name: Системное название статуса
        state_tooltip: Подсказка о текущем состоянии товара
    """
    state_description: Optional[str] = Field(None, description="Описание статуса.")
    state_name: Optional[str] = Field(None, description="Название статуса.")
    state_sys_name: Optional[str] = Field(None, description="Системное название статуса.")
    state_tooltip: Optional[str] = Field(
        None, description="Подсказка о текущем состоянии товара."
    )


class ProductQuantInfoQuant(BaseModel):
    """Квант эконом-товара.

    Notes:
        • Размер кванта приходит в поле `quant_sice` (опечатка в API Ozon); доступен
          через атрибут `quant_size`.

    Attributes:
        barcodes_extended: Информация о штрихкодах
        dimensions: Габариты кванта
        marketing_price: Маркетинговая цена
        min_price: Минимальная цена, указанная продавцом
        old_price: Зачёркнутая цена, указанная продавцом
        price: Цена продажи, указанная продавцом
        quant_code: Идентификатор эконом-товара
        quant_size: Размер кванта
        shipment_type: Тип доставки товара
        sku: Идентификатор товара в системе Ozon — SKU
        statuses: Статус кванта
    """
    model_config = ConfigDict(populate_by_name=True)

    barcodes_extended: list[ProductQuantInfoBarcode] = Field(
        default_factory=list, description="Информация о штрихкодах."
    )
    dimensions: Optional[ProductQuantInfoDimensions] = Field(
        None, description="Габариты кванта."
    )
    marketing_price: Optional[ProductQuantInfoMarketingPrice] = Field(
        None, description="Маркетинговая цена."
    )
    min_price: Optional[str] = Field(
        None, description="Минимальная цена, указанная продавцом."
    )
    old_price: Optional[str] = Field(
        None, description="Зачёркнутая цена, указанная продавцом."
    )
    price: Optional[str] = Field(None, description="Цена продажи, указанная продавцом.")
    quant_code: Optional[str] = Field(None, description="Идентификатор эконом-товара.")
    quant_size: Optional[int] = Field(
        None, alias="quant_sice", description="Размер кванта."
    )
    shipment_type: Optional[str] = Field(None, description="Тип доставки товара.")
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    statuses: Optional[ProductQuantInfoStatuses] = Field(
        None, description="Статус кванта."
    )


class ProductQuantInfoQuantInfo(BaseModel):
    """Информация о квантах товара.

    Attributes:
        quants: Список квантов
    """
    quants: list[ProductQuantInfoQuant] = Field(
        default_factory=list, description="Список квантов."
    )


class ProductQuantInfoItem(BaseModel):
    """Эконом-товар с информацией о квантах.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе Ozon — product_id
        quant_info: Информация о квантах
    """
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    quant_info: Optional[ProductQuantInfoQuantInfo] = Field(
        None, description="Информация о квантах."
    )


class ProductQuantInfoResponse(BaseModel):
    """Ответ с информацией об эконом-товарах.

    Attributes:
        items: Список эконом-товаров
    """
    items: list[ProductQuantInfoItem] = Field(
        default_factory=list, description="Список эконом-товаров."
    )
