"""https://docs.ozon.ru/api/seller/#operation/ReportAPI_CreateCompanyPostingsReport"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import CreateReportResult


class ReportPostingsCreateFilter(BaseModel):
    """Фильтр для отчёта об отправлениях.

    Attributes:
        sku: Идентификаторы товаров в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца
        title: Название товара
        delivery_schema: Схема работы (FBO / FBS)
        statuses: Числовые статусы
        status_alias: Текстовые статусы
        cancel_reason_id: Идентификаторы причин отмены
        warehouse_id: Идентификаторы складов
        delivery_method_id: Идентификаторы способов доставки
        is_express: Признак экспресс-доставки
        processed_at_from: Начало периода обработки
        processed_at_to: Конец периода обработки
    """
    sku: Optional[list[int]] = Field(
        None, description="Идентификаторы товаров в системе Ozon — SKU."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца."
    )
    title: Optional[str] = Field(
        None, description="Название товара."
    )
    delivery_schema: Optional[list[str]] = Field(
        None, description="Схема работы — FBO или FBS."
    )
    statuses: Optional[list[int]] = Field(
        None, description="Числовые статусы."
    )
    status_alias: Optional[list[str]] = Field(
        None, description="Текстовые статусы."
    )
    cancel_reason_id: Optional[list[int]] = Field(
        None, description="Идентификаторы причин отмены."
    )
    warehouse_id: Optional[list[int]] = Field(
        None, description="Идентификаторы складов."
    )
    delivery_method_id: Optional[list[int]] = Field(
        None, description="Идентификаторы способов доставки."
    )
    is_express: Optional[bool] = Field(
        None, description="Признак экспресс-доставки."
    )
    processed_at_from: Optional[str] = Field(
        None, description="Начало периода обработки заказа."
    )
    processed_at_to: Optional[str] = Field(
        None, description="Конец периода обработки заказа."
    )


class ReportPostingsCreateWith(BaseModel):
    """Дополнительные данные для отчёта об отправлениях.

    Attributes:
        additional_data: Добавить дополнительные данные
        analytics_data: Добавить аналитические данные
        customer_data: Добавить данные о покупателе
        jewelry_codes: Добавить ювелирные коды
    """
    additional_data: Optional[bool] = Field(
        None, description="`true`, чтобы добавить дополнительные данные."
    )
    analytics_data: Optional[bool] = Field(
        None, description="`true`, чтобы добавить аналитические данные."
    )
    customer_data: Optional[bool] = Field(
        None, description="`true`, чтобы добавить данные о покупателе."
    )
    jewelry_codes: Optional[bool] = Field(
        None, description="`true`, чтобы добавить ювелирные коды."
    )


class ReportPostingsCreateRequest(BaseModel):
    """Описывает схему запроса на создание отчёта об отправлениях.

    Attributes:
        filter: Фильтр
        with_: Дополнительные данные (сериализуется как `with`)
        language: Язык отчёта
    """
    model_config = {'populate_by_name': True}

    filter: ReportPostingsCreateFilter = Field(
        ..., description="Фильтр."
    )
    with_: Optional[ReportPostingsCreateWith] = Field(
        None, alias="with", description="Дополнительные данные."
    )
    language: Optional[str] = Field(
        None, description="Язык отчёта."
    )


class ReportPostingsCreateResponse(BaseModel):
    """Описывает схему ответа на запрос создания отчёта об отправлениях.

    Attributes:
        result: Результат создания отчёта
    """
    result: Optional[CreateReportResult] = Field(
        None, description="Результат создания отчёта."
    )
