"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerGet"""
from typing import Optional

from pydantic import BaseModel, Field


class CarriageContainerGetProduct(BaseModel):
    """Товар в отправлении грузоместа.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        name: Название товара
        offer_id: Идентификатор товара в системе продавца — артикул
        quantity: Количество экземпляров
        picture_url: Ссылка на изображение товара
        product_color: Цвет товара
        product_size_manufacturer: Размер производителя
        product_size_russian: Российский размер
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    quantity: Optional[int] = Field(
        None, description="Количество экземпляров."
    )
    picture_url: Optional[str] = Field(
        None, description="Ссылка на изображение товара."
    )
    product_color: Optional[str] = Field(
        None, description="Цвет товара."
    )
    product_size_manufacturer: Optional[str] = Field(
        None, description="Размер производителя."
    )
    product_size_russian: Optional[str] = Field(
        None, description="Российский размер."
    )


class CarriageContainerGetPosting(BaseModel):
    """Отправление в грузоместе.

    Attributes:
        posting_number: Номер отправления
        sort_type: Тип сортировки грузоместа
        weight: Вес отправления, кг
        in_process_at: Дата и время начала обработки отправления
        available_actions: Доступные действия с отправлением
        products: Список товаров
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    sort_type: Optional[str] = Field(
        None, description="Тип сортировки грузоместа."
    )
    weight: Optional[float] = Field(
        None, description="Вес отправления, кг."
    )
    in_process_at: Optional[str] = Field(
        None, description="Дата и время начала обработки отправления."
    )
    available_actions: Optional[list[str]] = Field(
        None, description="Доступные действия с отправлением."
    )
    products: Optional[list[CarriageContainerGetProduct]] = Field(
        None, description="Список товаров."
    )


class CarriageContainerGetRequest(BaseModel):
    """Описывает схему запроса на получение информации о грузоместе.

    Attributes:
        container_id: Идентификатор грузоместа
    """
    container_id: int = Field(
        ..., description="Идентификатор грузоместа."
    )


class CarriageContainerGetResponse(BaseModel):
    """Описывает схему ответа на запрос информации о грузоместе.

    Attributes:
        container_id: Идентификатор грузоместа
        container_number: Порядковый номер грузоместа
        parent_container_id: Идентификатор родительского грузоместа
        cargo_type: Тип грузоместа
        sort_type: Тип сортировки грузоместа
        status: Статус грузоместа
        available_actions: Доступные действия с грузоместом
        count_of_postings: Количество отправлений в грузоместе
        weight: Суммарный вес отправлений в грузоместе, кг
        postings: Список отправлений
        related_container_ids: Идентификаторы дочерних грузомест
        created_at: Дата создания грузоместа в UTC
        warehouse_date: Дата создания грузоместа в часовом поясе склада
        warehouse_id: Идентификатор склада продавца
        warehouse_name: Название склада
    """
    container_id: Optional[int] = Field(
        None, description="Идентификатор грузоместа."
    )
    container_number: Optional[int] = Field(
        None, description="Порядковый номер грузоместа."
    )
    parent_container_id: Optional[int] = Field(
        None, description="Идентификатор родительского грузоместа."
    )
    cargo_type: Optional[str] = Field(
        None, description="Тип грузоместа."
    )
    sort_type: Optional[str] = Field(
        None, description="Тип сортировки грузоместа."
    )
    status: Optional[str] = Field(
        None, description="Статус грузоместа."
    )
    available_actions: Optional[list[str]] = Field(
        None, description="Доступные действия с грузоместом."
    )
    count_of_postings: Optional[int] = Field(
        None, description="Количество отправлений в грузоместе."
    )
    weight: Optional[float] = Field(
        None, description="Суммарный вес отправлений в грузоместе, кг."
    )
    postings: Optional[list[CarriageContainerGetPosting]] = Field(
        None, description="Список отправлений."
    )
    related_container_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы дочерних грузомест."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания грузоместа в UTC."
    )
    warehouse_date: Optional[str] = Field(
        None, description="Дата создания грузоместа в часовом поясе склада."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )
    warehouse_name: Optional[str] = Field(
        None, description="Название склада."
    )
