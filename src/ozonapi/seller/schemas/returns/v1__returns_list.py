"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_GetReturnsList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ReturnsMoney, ReturnsPlace, ReturnsStatus, ReturnsTimeRange


class ReturnsListFilter(BaseModel):
    """Фильтр для получения списка возвратов FBO и FBS.

    Attributes:
        logistic_return_date: Фильтр по дате возврата
        storage_tariffication_start_date: Фильтр по дате старта тарификации за хранение
        visual_status_change_moment: Фильтр по дате изменения статуса возврата
        order_id: Фильтр по идентификатору заказа
        posting_numbers: Фильтр по номерам отправлений
        product_name: Фильтр по названию товара
        offer_id: Фильтр по артикулу товара
        visual_status_name: Фильтр по статусу возврата
        warehouse_id: Фильтр по идентификатору склада
        barcode: Фильтр по штрихкоду возвратной этикетки
        return_schema: Фильтр по схеме доставки (`FBS` или `FBO`)
        compensation_status_id: Фильтр по статусу компенсации
    """
    logistic_return_date: Optional[ReturnsTimeRange] = Field(
        None, description="Фильтр по дате возврата."
    )
    storage_tariffication_start_date: Optional[ReturnsTimeRange] = Field(
        None, description="Фильтр по дате старта тарификации за хранение."
    )
    visual_status_change_moment: Optional[ReturnsTimeRange] = Field(
        None, description="Фильтр по дате изменения статуса возврата."
    )
    order_id: Optional[int] = Field(
        None, description="Фильтр по идентификатору заказа."
    )
    posting_numbers: Optional[list[str]] = Field(
        None, description="Фильтр по номерам отправлений."
    )
    product_name: Optional[str] = Field(
        None, description="Фильтр по названию товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Фильтр по артикулу товара."
    )
    visual_status_name: Optional[str] = Field(
        None, description="Фильтр по статусу возврата."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Фильтр по идентификатору склада."
    )
    barcode: Optional[str] = Field(
        None, description="Фильтр по штрихкоду возвратной этикетки."
    )
    return_schema: Optional[str] = Field(
        None, description="Фильтр по схеме доставки: `FBS` или `FBO`."
    )
    compensation_status_id: Optional[int] = Field(
        None, description="Фильтр по статусу компенсации."
    )


class ReturnsListRequest(BaseModel):
    """Описывает схему запроса на получение списка возвратов FBO и FBS.

    Attributes:
        limit: Количество подгружаемых возвратов
        filter: Фильтр для поиска возвратов
        last_id: Идентификатор последнего подгруженного возврата
    """
    limit: int = Field(
        ..., description="Количество подгружаемых возвратов."
    )
    filter: Optional[ReturnsListFilter] = Field(
        None, description="Фильтр для поиска возвратов."
    )
    last_id: Optional[int] = Field(
        None, description="Идентификатор последнего подгруженного возврата."
    )


class ReturnsListExemplar(BaseModel):
    """Экземпляр товара в возврате.

    Attributes:
        id: Идентификатор экземпляра
    """
    id: Optional[int] = Field(
        None, description="Идентификатор экземпляра."
    )


class ReturnsListStorage(BaseModel):
    """Информация о хранении возврата.

    Attributes:
        sum: Стоимость хранения
        tariffication_first_date: Первый день тарификации за хранение
        tariffication_start_date: Дата старта тарификации за хранение
        arrived_moment: Дата готовности возврата к выдаче
        days: Сколько дней возврат ожидает выдачи
        utilization_sum: Стоимость утилизации
        utilization_forecast_date: Планируемая дата утилизации
    """
    sum: Optional[ReturnsMoney] = Field(
        None, description="Стоимость хранения."
    )
    tariffication_first_date: Optional[str] = Field(
        None, description="Первый день тарификации за хранение."
    )
    tariffication_start_date: Optional[str] = Field(
        None, description="Дата старта тарификации за хранение."
    )
    arrived_moment: Optional[str] = Field(
        None, description="Дата, когда возврат был готов к выдаче."
    )
    days: Optional[int] = Field(
        None, description="Сколько дней возврат ожидает выдачи продавцу."
    )
    utilization_sum: Optional[ReturnsMoney] = Field(
        None, description="Стоимость утилизации."
    )
    utilization_forecast_date: Optional[str] = Field(
        None, description="Планируемая дата утилизации."
    )


class ReturnsListProduct(BaseModel):
    """Информация о товаре в возврате.

    Attributes:
        sku: Идентификатор товара в системе Ozon — SKU
        offer_id: Идентификатор товара в системе продавца — артикул
        name: Название товара
        price: Стоимость товара
        price_without_commission: Стоимость товара без комиссии
        commission_percent: Процент комиссии
        commission: Размер комиссии
        quantity: Количество товара
    """
    sku: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    name: Optional[str] = Field(
        None, description="Название товара."
    )
    price: Optional[ReturnsMoney] = Field(
        None, description="Стоимость товара."
    )
    price_without_commission: Optional[ReturnsMoney] = Field(
        None, description="Стоимость товара без комиссии."
    )
    commission_percent: Optional[float] = Field(
        None, description="Процент комиссии."
    )
    commission: Optional[ReturnsMoney] = Field(
        None, description="Размер комиссии."
    )
    quantity: Optional[int] = Field(
        None, description="Количество товара."
    )


class ReturnsListLogistic(BaseModel):
    """Логистическая информация о возврате.

    Attributes:
        technical_return_moment: Дата постановки на технический возврат
        final_moment: Дата прибытия возврата на фулфилмент
        cancelled_with_compensation_moment: Дата компенсации возврата
        return_date: Дата возврата товара покупателем
        barcode: Штрихкод этикетки возврата
    """
    technical_return_moment: Optional[str] = Field(
        None, description="Дата, когда заказ поставили на технический возврат."
    )
    final_moment: Optional[str] = Field(
        None, description="Дата, когда возврат прибыл на фулфилмент."
    )
    cancelled_with_compensation_moment: Optional[str] = Field(
        None, description="Дата, когда продавцу компенсировали возврат."
    )
    return_date: Optional[str] = Field(
        None, description="Дата, когда покупатель вернул товар."
    )
    barcode: Optional[str] = Field(
        None, description="Штрихкод этикетки возврата."
    )


class ReturnsListVisual(BaseModel):
    """Визуальный статус возврата.

    Attributes:
        status: Статус возврата
        change_moment: Дата изменения статуса возврата
    """
    status: Optional[ReturnsStatus] = Field(
        None, description="Статус возврата."
    )
    change_moment: Optional[str] = Field(
        None, description="Дата изменения статуса возврата."
    )


class ReturnsListAdditionalInfo(BaseModel):
    """Дополнительная информация о возврате.

    Attributes:
        is_opened: Признак вскрытия возврата
        is_super_econom: Признак товара «Суперэконом»
    """
    is_opened: Optional[bool] = Field(
        None, description="`true`, если возврат вскрыт."
    )
    is_super_econom: Optional[bool] = Field(
        None, description="`true`, если возврат относится к товарам «Суперэконом»."
    )


class ReturnsListCompensation(BaseModel):
    """Статус компенсации возврата.

    Attributes:
        status: Статус компенсации
        change_moment: Дата изменения статуса компенсации
    """
    status: Optional[ReturnsStatus] = Field(
        None, description="Статус компенсации."
    )
    change_moment: Optional[str] = Field(
        None, description="Дата изменения статуса компенсации."
    )


class ReturnsListItem(BaseModel):
    """Информация о возврате.

    Attributes:
        id: Идентификатор возврата
        company_id: Идентификатор продавца
        exemplars: Информация об экземплярах
        return_reason_name: Причина возврата или отмены
        type: Тип возврата
        schema_: Схема возврата (`FBS` / `FBO`)
        order_id: Идентификатор заказа
        order_number: Номер заказа
        place: Текущий склад
        target_place: Целевой склад
        storage: Информация о хранении
        product: Информация о товаре
        logistic: Логистическая информация
        visual: Визуальный статус
        additional_info: Дополнительная информация
        source_id: Предыдущий идентификатор возврата
        posting_number: Номер отправления
        clearing_id: Штрихкод изначального отправления
        return_clearing_id: Возвратный штрихкод изначального отправления
        compensation_status: Статус компенсации
    """
    model_config = {'populate_by_name': True}

    id: Optional[int] = Field(
        None, description="Идентификатор возврата."
    )
    company_id: Optional[int] = Field(
        None, description="Идентификатор продавца."
    )
    exemplars: Optional[list[ReturnsListExemplar]] = Field(
        None, description="Информация об экземплярах."
    )
    return_reason_name: Optional[str] = Field(
        None, description="Причина возврата или отмены."
    )
    type: Optional[str] = Field(
        None, description="Тип возврата."
    )
    schema_: Optional[str] = Field(
        None, alias="schema", description="Схема возврата: `FBS`, `FBO`."
    )
    order_id: Optional[int] = Field(
        None, description="Идентификатор заказа."
    )
    order_number: Optional[str] = Field(
        None, description="Номер заказа."
    )
    place: Optional[ReturnsPlace] = Field(
        None, description="Текущий склад."
    )
    target_place: Optional[ReturnsPlace] = Field(
        None, description="Целевой склад."
    )
    storage: Optional[ReturnsListStorage] = Field(
        None, description="Информация о хранении."
    )
    product: Optional[ReturnsListProduct] = Field(
        None, description="Информация о товаре."
    )
    logistic: Optional[ReturnsListLogistic] = Field(
        None, description="Логистическая информация."
    )
    visual: Optional[ReturnsListVisual] = Field(
        None, description="Визуальный статус."
    )
    additional_info: Optional[ReturnsListAdditionalInfo] = Field(
        None, description="Дополнительная информация."
    )
    source_id: Optional[int] = Field(
        None, description="Предыдущий идентификатор возврата."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    clearing_id: Optional[int] = Field(
        None, description="Штрихкод изначального отправления."
    )
    return_clearing_id: Optional[int] = Field(
        None, description="Возвратный штрихкод изначального отправления."
    )
    compensation_status: Optional[ReturnsListCompensation] = Field(
        None, description="Статус компенсации."
    )


class ReturnsListResponse(BaseModel):
    """Описывает схему ответа на запрос списка возвратов FBO и FBS.

    Attributes:
        returns: Информация о возвратах
        has_next: Признак наличия следующей страницы
    """
    returns: Optional[list[ReturnsListItem]] = Field(
        None, description="Информация о возвратах."
    )
    has_next: Optional[bool] = Field(
        None, description="`true`, если у продавца есть другие возвраты."
    )
