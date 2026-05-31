"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsCompanyFbsInfo"""
from typing import Optional, Union

from pydantic import BaseModel, Field


class ReturnsCompanyFbsInfoFilter(BaseModel):
    """Фильтр для получения количества возвратов FBS.

    Attributes:
        place_id: Фильтр по идентификатору drop-off пункта
    """
    place_id: Optional[int] = Field(
        None, description="Фильтр по идентификатору drop-off пункта."
    )


class ReturnsCompanyFbsInfoPagination(BaseModel):
    """Пагинация для получения количества возвратов FBS.

    Attributes:
        limit: Количество drop-off пунктов на странице
        last_id: Идентификатор последнего drop-off пункта на странице
    """
    limit: Optional[int] = Field(
        None, description="Количество drop-off пунктов на странице."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего drop-off пункта на странице."
    )


class ReturnsCompanyFbsInfoRequest(BaseModel):
    """Описывает схему запроса на получение количества возвратов FBS.

    Attributes:
        pagination: Пагинация
        filter: Фильтр для поиска
    """
    pagination: ReturnsCompanyFbsInfoPagination = Field(
        ..., description="Пагинация."
    )
    filter: Optional[ReturnsCompanyFbsInfoFilter] = Field(
        None, description="Фильтр для поиска."
    )


class ReturnsCompanyFbsInfoPassInfo(BaseModel):
    """Информация о пропусках на drop-off пункт.

    Attributes:
        count: Количество пропусков на drop-off пункт
        is_required: Признак необходимости пропуска
    """
    count: Optional[int] = Field(
        None, description="Количество пропусков на drop-off пункт."
    )
    is_required: Optional[bool] = Field(
        None, description="Признак, нужен ли пропуск на drop-off пункт."
    )


class ReturnsCompanyFbsInfoDropOffPoint(BaseModel):
    """Информация о drop-off пункте.

    Attributes:
        id: Идентификатор drop-off пункта
        name: Название drop-off пункта
        address: Адрес drop-off пункта
        box_count: Количество коробок в drop-off пункте
        returns_count: Количество возвратов в drop-off пункте
        place_id: Идентификатор склада, на который приедет отгрузка
        pass_info: Информация о пропусках
        utc_offset: Смещение часового пояса времени отгрузки
        warehouses_ids: Идентификаторы складов продавца
    """
    id: Optional[int] = Field(
        None, description="Идентификатор drop-off пункта."
    )
    name: Optional[str] = Field(
        None, description="Название drop-off пункта."
    )
    address: Optional[str] = Field(
        None, description="Адрес drop-off пункта."
    )
    box_count: Optional[int] = Field(
        None, description="Количество коробок в drop-off пункте."
    )
    returns_count: Optional[int] = Field(
        None, description="Количество возвратов в drop-off пункте."
    )
    place_id: Optional[int] = Field(
        None, description="Идентификатор склада, на который приедет отгрузка."
    )
    pass_info: Optional[ReturnsCompanyFbsInfoPassInfo] = Field(
        None, description="Информация о пропусках."
    )
    utc_offset: Optional[str] = Field(
        None, description="Смещение часового пояса времени отгрузки."
    )
    warehouses_ids: Optional[list[Union[int, str]]] = Field(
        None, description="Идентификаторы складов продавца."
    )


class ReturnsCompanyFbsInfoResponse(BaseModel):
    """Описывает схему ответа на запрос количества возвратов FBS.

    Attributes:
        drop_off_points: Информация о drop-off пунктах
        has_next: Признак наличия следующей страницы
    """
    drop_off_points: Optional[list[ReturnsCompanyFbsInfoDropOffPoint]] = Field(
        None, description="Информация о drop-off пунктах."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если есть ещё пункты."
    )
