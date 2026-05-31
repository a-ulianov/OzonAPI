"""https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerList"""
from typing import Any, Optional

from pydantic import BaseModel, Field


class CarriageContainerListFilter(BaseModel):
    """Фильтр для получения списка грузомест.

    Attributes:
        warehouse_id: Идентификатор склада продавца
        cargo_type: Тип грузоместа (`box` — коробка, `pallet` — палета)
        sort_type: Тип сортировки грузоместа (`sort` / `non_sort`)
        statuses: Статусы грузоместа
        created_from: Дата начала периода создания грузоместа
        created_to: Дата окончания периода создания грузоместа
    """
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада продавца."
    )
    cargo_type: Optional[str] = Field(
        None, description="Тип грузоместа: `box` — коробка, `pallet` — палета."
    )
    sort_type: Optional[str] = Field(
        None, description="Тип сортировки грузоместа: `sort` — сортируемый, `non_sort` — несортируемый."
    )
    statuses: Optional[list[str]] = Field(
        None, description="Статусы грузоместа."
    )
    created_from: Optional[str] = Field(
        None, description="Дата начала периода создания грузоместа."
    )
    created_to: Optional[str] = Field(
        None, description="Дата окончания периода создания грузоместа."
    )


class CarriageContainerListRequest(BaseModel):
    """Описывает схему запроса на получение списка грузомест.

    Attributes:
        filter: Фильтр для поиска грузомест
        limit: Количество значений в ответе
        cursor: Указатель для выборки следующих данных
        sort_dir: Направление сортировки (`ASC` / `DESC`)
    """
    filter: Optional[CarriageContainerListFilter] = Field(
        None, description="Фильтр для поиска грузомест."
    )
    limit: Optional[int] = Field(
        None, description="Количество значений в ответе."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )


class CarriageContainerListContainer(BaseModel):
    """Информация о грузоместе в списке.

    Attributes:
        container_id: Идентификатор грузоместа
        container_number: Порядковый номер грузоместа
        cargo_type: Тип грузоместа
        sort_type: Тип сортировки грузоместа
        status: Статус грузоместа
        available_actions: Доступные действия с грузоместом
        count_of_postings: Количество отправлений в грузоместе
        weight: Суммарный вес отправлений в грузоместе, кг
        related_containers: Дочерние грузоместа
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
    related_containers: Optional[list[Any]] = Field(
        None, description="Дочерние грузоместа."
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


class CarriageContainerListResponse(BaseModel):
    """Описывает схему ответа на запрос списка грузомест.

    Attributes:
        containers: Информация о грузоместах
        cursor: Указатель для выборки следующих данных
    """
    containers: Optional[list[CarriageContainerListContainer]] = Field(
        None, description="Информация о грузоместах."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
