"""https://docs.ozon.com/api/seller/?#operation/SupplyOrderTimeslotList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import SupplyOrderTimeslot


class SupplyOrderTimeslotListLimitExceeded(BaseModel):
    """Описывает информацию о превышении лимита изменений интервала поставки.

    Attributes:
        changes_limit: Остаток доступных изменений интервала поставки
    """
    changes_limit: Optional[int] = Field(
        None, description="Остаток доступных изменений интервала поставки."
    )


class SupplyOrderTimeslotListChangeForbidden(BaseModel):
    """Описывает причины, по которым нельзя изменить интервал поставки.

    Attributes:
        error_reasons: Причины запрета изменения интервала поставки (строками)
    """
    error_reasons: Optional[list[str]] = Field(
        default_factory=list,
        description=(
            "Причины, по которым нельзя изменить интервал поставки: "
            "`INVALID_ORDER_STATE` — неверный статус заявки на поставку; "
            "`IS_VIRTUAL` — заявка на поставку виртуальная; "
            "`SET_TIMESLOT_DEADLINE_EXCEED` — заявка на поставку просрочена; "
            "`ORDER_DOES_NOT_BELONG_TO_COMPANY` — заявка на поставку не принадлежит продавцу."
        ),
    )


class SupplyOrderTimeslotListLimitations(BaseModel):
    """Описывает ограничения на обновления интервала поставки.

    Attributes:
        changes_count: Количество изменений интервала поставки
        changes_limit: Остаток доступных изменений интервала поставки
    """
    changes_count: Optional[int] = Field(
        None, description="Количество изменений интервала поставки."
    )
    changes_limit: Optional[int] = Field(
        None, description="Остаток доступных изменений интервала поставки."
    )


class SupplyOrderTimeslotListTimezone(BaseModel):
    """Описывает часовой пояс интервалов поставки.

    Attributes:
        iana_name: Название часового пояса (IANA)
        offset: Смещение часового пояса от UTC-0 в секундах
    """
    iana_name: Optional[str] = Field(
        None, description="Название часового пояса."
    )
    offset: Optional[int] = Field(
        None, description="Смещение часового пояса от UTC-0 в секундах."
    )


class SupplyOrderTimeslotListTimeslotsInfo(BaseModel):
    """Описывает информацию об интервалах поставки.

    Attributes:
        limitations: Ограничения на обновления интервала поставки
        timeslots: Список интервалов поставки
        timezone: Часовой пояс интервалов
    """
    limitations: Optional[SupplyOrderTimeslotListLimitations] = Field(
        None, description="Ограничения на обновления интервала поставки."
    )
    timeslots: Optional[list[SupplyOrderTimeslot]] = Field(
        default_factory=list, description="Список интервалов поставки."
    )
    timezone: Optional[SupplyOrderTimeslotListTimezone] = Field(
        None, description="Часовой пояс интервалов."
    )


class SupplyOrderTimeslotListRequest(BaseModel):
    """Описывает схему запроса на получение списка доступных интервалов поставки.

    Attributes:
        order_id: Идентификатор заявки на поставку
    """
    order_id: int = Field(
        ..., description="Идентификатор заявки на поставку."
    )


class SupplyOrderTimeslotListResponse(BaseModel):
    """Описывает схему ответа на запрос списка доступных интервалов поставки.

    Attributes:
        limit_exceeded: Информация о превышении лимита изменений интервала поставки
        timeslot_change_forbidden: Информация о причинах запрета изменения интервала поставки
        timeslots_info: Информация об интервалах поставки
    """
    limit_exceeded: Optional[SupplyOrderTimeslotListLimitExceeded] = Field(
        None, description="Информация о превышении лимита изменений интервала поставки."
    )
    timeslot_change_forbidden: Optional[SupplyOrderTimeslotListChangeForbidden] = Field(
        None, description="Информация о причинах, по которым нельзя изменить интервал поставки."
    )
    timeslots_info: Optional[SupplyOrderTimeslotListTimeslotsInfo] = Field(
        None, description="Информация об интервалах поставки."
    )
