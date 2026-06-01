"""Общие сущности доставки FBP (детали способов поставки)."""
from typing import Optional

from pydantic import BaseModel, Field


class FbpTimeslot(BaseModel):
    """Временной интервал (таймслот) поставки FBP.

    Attributes:
        timeslot_start: Начало интервала
        timeslot_end: Конец интервала
    """

    timeslot_start: Optional[str] = Field(
        None, description="Начало временного интервала в формате RFC3339."
    )
    timeslot_end: Optional[str] = Field(
        None, description="Конец временного интервала в формате RFC3339."
    )


class FbpDirectBySellerDetails(BaseModel):
    """Детали доставки силами продавца (direct).

    Attributes:
        driver_name: Имя водителя
        vehicle_registration_number: Регистрационный номер транспортного средства
        vehicle_type: Тип транспортного средства
    """

    driver_name: Optional[str] = Field(
        None, description="Имя водителя."
    )
    vehicle_registration_number: Optional[str] = Field(
        None, description="Регистрационный номер транспортного средства."
    )
    vehicle_type: Optional[str] = Field(
        None, description="Тип транспортного средства."
    )


class FbpDirectByTplDetails(BaseModel):
    """Детали доставки сторонней транспортной компанией (direct).

    Attributes:
        tracking_number: Трек-номер
        transport_company_name: Название транспортной компании
    """

    tracking_number: Optional[str] = Field(
        None, description="Трек-номер отправления."
    )
    transport_company_name: Optional[str] = Field(
        None, description="Название транспортной компании."
    )


class FbpDirectTimeslotDetails(BaseModel):
    """Детали таймслота прямой поставки (direct).

    Attributes:
        timeslot: Временной интервал поставки
        timeslot_reservation_id: Идентификатор брони таймслота
    """

    timeslot: Optional[FbpTimeslot] = Field(
        None, description="Временной интервал поставки."
    )
    timeslot_reservation_id: Optional[str] = Field(
        None, description="Идентификатор брони таймслота."
    )


class FbpDirectDetails(BaseModel):
    """Детали прямой поставки (direct).

    Attributes:
        by_seller_details: Детали доставки силами продавца
        by_tpl_details: Детали доставки сторонней транспортной компанией
        timeslot_details: Детали таймслота поставки
    """

    by_seller_details: Optional[FbpDirectBySellerDetails] = Field(
        None, description="Детали доставки силами продавца."
    )
    by_tpl_details: Optional[FbpDirectByTplDetails] = Field(
        None, description="Детали доставки сторонней транспортной компанией."
    )
    timeslot_details: Optional[FbpDirectTimeslotDetails] = Field(
        None, description="Детали таймслота поставки."
    )


class FbpDropOffPointDetails(BaseModel):
    """Детали поставки в drop-off пункт.

    Attributes:
        id: Идентификатор drop-off пункта
        province_uuid: Идентификатор провинции
        timeslot: Временной интервал поставки
    """

    id: Optional[int] = Field(
        None, description="Идентификатор drop-off пункта."
    )
    province_uuid: Optional[str] = Field(
        None, description="Идентификатор провинции."
    )
    timeslot: Optional[FbpTimeslot] = Field(
        None, description="Временной интервал поставки."
    )


class FbpPickUpDetails(BaseModel):
    """Детали pick-up поставки (забор силами Ozon).

    Attributes:
        address: Адрес забора
        comment: Комментарий
        date: Дата забора
        sender_name: Имя отправителя
        sender_phone: Телефон отправителя
    """

    address: Optional[str] = Field(
        None, description="Адрес забора груза."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий к забору."
    )
    date: Optional[str] = Field(
        None, description="Дата забора в формате RFC3339."
    )
    sender_name: Optional[str] = Field(
        None, description="Имя отправителя."
    )
    sender_phone: Optional[str] = Field(
        None, description="Телефон отправителя."
    )


class FbpDeliveryDetails(BaseModel):
    """Детали доставки поставки FBP.

    Attributes:
        direct_details: Детали прямой поставки (direct)
        drop_off_point: Детали поставки в drop-off пункт
        pickup_details: Детали pick-up поставки
        supply_type: Тип поставки (`SUPPLY_TYPE_UNSPECIFIED`, `DIRECT_BY_SELLER`,
            `DIRECT_BY_TPL`, `DROP_OFF`, `PICK_UP`)
    """

    direct_details: Optional[FbpDirectDetails] = Field(
        None, description="Детали прямой поставки (direct)."
    )
    drop_off_point: Optional[FbpDropOffPointDetails] = Field(
        None, description="Детали поставки в drop-off пункт."
    )
    pickup_details: Optional[FbpPickUpDetails] = Field(
        None, description="Детали pick-up поставки."
    )
    supply_type: Optional[str] = Field(
        None,
        description="Тип поставки. Известные значения: `SUPPLY_TYPE_UNSPECIFIED`, "
                    "`DIRECT_BY_SELLER`, `DIRECT_BY_TPL`, `DROP_OFF`, `PICK_UP` "
                    "(набор открытый — тип `str`)."
    )
