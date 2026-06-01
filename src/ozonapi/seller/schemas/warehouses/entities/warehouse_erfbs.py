"""Общие сущности методов создания и управления складами rFBS Express (/v1/warehouse/erfbs/*)."""
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from ....common.enumerations.warehouses import (
    WarehouseERFBSReturnMethod,
    WarehouseWorkingDayV2,
)


class WarehouseERFBSOperationResponse(BaseModel):
    """Ответ асинхронной операции со складом rFBS Express.

    Attributes:
        operation_id: Идентификатор операции
    """
    operation_id: Optional[str] = Field(None, description="Идентификатор операции.")


class WarehouseERFBSHoliday(BaseModel):
    """Выходной день склада rFBS Express.

    Attributes:
        day: День
        from_: Начало периода
        to_: Конец периода
    """
    model_config = ConfigDict(populate_by_name=True)

    day: Optional[str] = Field(None, description="День.")
    from_: Optional[str] = Field(None, alias="from", description="Начало периода.")
    to_: Optional[str] = Field(None, alias="to", description="Конец периода.")


class WarehouseERFBSWorkingDay(BaseModel):
    """Рабочий день склада rFBS Express.

    Attributes:
        day: День недели
        from_: Начало рабочего дня
        to_: Конец рабочего дня
    """
    model_config = ConfigDict(populate_by_name=True)

    day: Optional[WarehouseWorkingDayV2] = Field(None, description="День недели.")
    from_: Optional[str] = Field(None, alias="from", description="Начало рабочего дня.")
    to_: Optional[str] = Field(None, alias="to", description="Конец рабочего дня.")


class WarehouseERFBSTimetable(BaseModel):
    """Расписание работы склада rFBS Express.

    Attributes:
        holidays: Выходные дни
        working_days: Рабочие дни
    """
    holidays: Optional[list[WarehouseERFBSHoliday]] = Field(
        None, description="Выходные дни."
    )
    working_days: Optional[list[WarehouseERFBSWorkingDay]] = Field(
        None, description="Рабочие дни."
    )


class WarehouseERFBSReturnSettings(BaseModel):
    """Настройки возврата склада rFBS Express.

    Attributes:
        contact_days: Количество дней для связи
        post_office_zipcode: Индекс почтового отделения
        return_method: Способ возврата
        transport_company_name: Название транспортной компании
    """
    contact_days: Optional[int] = Field(
        None, description="Количество дней для связи."
    )
    post_office_zipcode: Optional[str] = Field(
        None, description="Индекс почтового отделения."
    )
    return_method: Optional[WarehouseERFBSReturnMethod] = Field(
        None, description="Способ возврата."
    )
    transport_company_name: Optional[str] = Field(
        None, description="Название транспортной компании."
    )


class WarehouseERFBSDeliveryCosts(BaseModel):
    """Стоимость доставки склада rFBS Express.

    Attributes:
        max_amount: Максимальная стоимость
        min_amount: Минимальная стоимость
        percent: Процент от стоимости заказа
    """
    max_amount: Optional[int] = Field(None, description="Максимальная стоимость.")
    min_amount: Optional[int] = Field(None, description="Минимальная стоимость.")
    percent: Optional[float] = Field(None, description="Процент от стоимости заказа.")


class WarehouseERFBSDeliveryPolygon(BaseModel):
    """Полигон доставки склада rFBS Express.

    Attributes:
        id: Идентификатор полигона
        time: Время доставки в минутах (допустимо: 15, 30, 45, 60, 90, 120, 150)
    """
    id: Optional[int] = Field(None, description="Идентификатор полигона.")
    time: Optional[int] = Field(
        None, description="Время доставки в минутах (допустимо: 15, 30, 45, 60, 90, 120, 150)."
    )
