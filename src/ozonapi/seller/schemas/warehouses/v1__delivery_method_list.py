"""Схемы метода delivery_method_list (список методов доставки, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class DeliveryMethodListV1Filter(BaseModel):
    """Фильтр списка методов доставки (v1).

    Attributes:
        provider_id: Идентификатор службы доставки
        status: Статус метода доставки
        warehouse_id: Идентификатор склада
    """
    provider_id: Optional[int] = Field(
        None, description="Идентификатор службы доставки."
    )
    status: Optional[str] = Field(None, description="Статус метода доставки.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class DeliveryMethodListV1Request(BaseModel):
    """Параметры запроса списка методов доставки (v1).

    Attributes:
        filter: Фильтр выборки
        limit: Количество значений в ответе
        offset: Смещение выборки
    """
    filter: Optional[DeliveryMethodListV1Filter] = Field(
        None, description="Фильтр выборки."
    )
    limit: Optional[int] = Field(None, description="Количество значений в ответе.")
    offset: Optional[int] = Field(None, description="Смещение выборки.")


class DeliveryMethodListV1Item(BaseModel):
    """Метод доставки склада (v1).

    Attributes:
        company_id: Идентификатор продавца
        created_at: Дата создания
        cutoff: Время отгрузки
        id: Идентификатор метода доставки
        name: Название метода доставки
        provider_id: Идентификатор службы доставки
        sla_cut_in: Время на сборку заказа
        status: Статус метода доставки
        template_id: Идентификатор шаблона
        updated_at: Дата обновления
        warehouse_id: Идентификатор склада
    """
    company_id: Optional[int] = Field(None, description="Идентификатор продавца.")
    created_at: Optional[str] = Field(None, description="Дата создания.")
    cutoff: Optional[str] = Field(None, description="Время отгрузки.")
    id: Optional[int] = Field(None, description="Идентификатор метода доставки.")
    name: Optional[str] = Field(None, description="Название метода доставки.")
    provider_id: Optional[int] = Field(
        None, description="Идентификатор службы доставки."
    )
    sla_cut_in: Optional[int] = Field(None, description="Время на сборку заказа.")
    status: Optional[str] = Field(None, description="Статус метода доставки.")
    template_id: Optional[int] = Field(None, description="Идентификатор шаблона.")
    updated_at: Optional[str] = Field(None, description="Дата обновления.")
    warehouse_id: Optional[int] = Field(None, description="Идентификатор склада.")


class DeliveryMethodListV1Response(BaseModel):
    """Ответ со списком методов доставки (v1).

    Attributes:
        has_next: Признак наличия следующей страницы
        result: Список методов доставки
    """
    has_next: Optional[bool] = Field(
        None, description="Признак наличия следующей страницы."
    )
    result: Optional[list[DeliveryMethodListV1Item]] = Field(
        None, description="Список методов доставки."
    )
