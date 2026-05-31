"""https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsGetV2"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ReturnsRfbsProduct


class ReturnsRfbsGetRequest(BaseModel):
    """Описывает схему запроса на получение информации о заявке на возврат rFBS.

    Attributes:
        return_id: Идентификатор заявки на возврат
    """
    return_id: int = Field(
        ..., description="Идентификатор заявки на возврат."
    )


class ReturnsRfbsGetAvailableAction(BaseModel):
    """Доступное действие с заявкой.

    Attributes:
        id: Идентификатор действия
        name: Название действия
    """
    id: Optional[int] = Field(
        None, description="Идентификатор действия."
    )
    name: Optional[str] = Field(
        None, description="Название действия."
    )


class ReturnsRfbsGetClientReturnMethodType(BaseModel):
    """Способ возврата товара покупателем.

    Attributes:
        id: Идентификатор
        name: Название
    """
    id: Optional[int] = Field(
        None, description="Идентификатор."
    )
    name: Optional[str] = Field(
        None, description="Название."
    )


class ReturnsRfbsGetRejectionReason(BaseModel):
    """Причина отклонения заявки.

    Attributes:
        id: Идентификатор причины
        name: Описание причины
        hint: Подсказка о дальнейших действиях с возвратом
        is_comment_required: Признак обязательности комментария
    """
    id: Optional[int] = Field(
        None, description="Идентификатор причины."
    )
    name: Optional[str] = Field(
        None, description="Описание причины."
    )
    hint: Optional[str] = Field(
        None, description="Подсказка о дальнейших действиях с возвратом."
    )
    is_comment_required: Optional[bool] = Field(
        None, description="Признак, нужно ли прикладывать комментарий."
    )


class ReturnsRfbsGetReturnReason(BaseModel):
    """Причина возврата.

    Attributes:
        id: Идентификатор причины
        name: Описание причины
        is_defect: Признак бракованного товара
    """
    id: Optional[int] = Field(
        None, description="Идентификатор причины."
    )
    name: Optional[str] = Field(
        None, description="Описание причины."
    )
    is_defect: Optional[bool] = Field(
        None, description="Признак, является ли товар бракованным."
    )


class ReturnsRfbsGetState(BaseModel):
    """Статус заявки на возврат.

    Attributes:
        state: Статус
        state_name: Название статуса на русском
    """
    state: Optional[str] = Field(
        None, description="Статус."
    )
    state_name: Optional[str] = Field(
        None, description="Название статуса на русском."
    )


class ReturnsRfbsGetReturn(BaseModel):
    """Информация о заявке на возврат rFBS.

    Attributes:
        return_number: Номер заявки на возврат
        client_name: Имя покупателя
        client_photo: Ссылки на фотографии товара
        comment: Комментарий покупателя
        created_at: Дата создания заявки
        order_number: Номер заказа
        posting_number: Номер отправления
        product: Информация о товаре
        available_actions: Доступные действия с заявкой
        client_return_method_type: Способ возврата товара покупателем
        return_method_description: Способ возврата товара
        return_reason: Причина возврата
        rejection_reason: Причины отклонения заявки
        rejection_comment: Комментарий об отклонении заявки
        ru_post_tracking_number: Трек-номер почтового отправления
        state: Статус заявки
        warehouse_id: Идентификатор склада
    """
    return_number: Optional[str] = Field(
        None, description="Номер заявки на возврат."
    )
    client_name: Optional[str] = Field(
        None, description="Имя покупателя."
    )
    client_photo: Optional[list[str]] = Field(
        None, description="Ссылки на фотографии товара."
    )
    comment: Optional[str] = Field(
        None, description="Комментарий покупателя."
    )
    created_at: Optional[str] = Field(
        None, description="Дата создания заявки."
    )
    order_number: Optional[str] = Field(
        None, description="Номер заказа."
    )
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    product: Optional[ReturnsRfbsProduct] = Field(
        None, description="Информация о товаре."
    )
    available_actions: Optional[list[ReturnsRfbsGetAvailableAction]] = Field(
        None, description="Доступные действия с заявкой."
    )
    client_return_method_type: Optional[ReturnsRfbsGetClientReturnMethodType] = Field(
        None, description="Способ возврата товара покупателем."
    )
    return_method_description: Optional[str] = Field(
        None, description="Способ возврата товара."
    )
    return_reason: Optional[ReturnsRfbsGetReturnReason] = Field(
        None, description="Причина возврата."
    )
    rejection_reason: Optional[list[ReturnsRfbsGetRejectionReason]] = Field(
        None, description="Причины отклонения заявки."
    )
    rejection_comment: Optional[str] = Field(
        None, description="Комментарий об отклонении заявки."
    )
    ru_post_tracking_number: Optional[str] = Field(
        None, description="Трек-номер почтового отправления."
    )
    state: Optional[ReturnsRfbsGetState] = Field(
        None, description="Статус заявки."
    )
    warehouse_id: Optional[int] = Field(
        None, description="Идентификатор склада."
    )


class ReturnsRfbsGetResponse(BaseModel):
    """Описывает схему ответа на запрос информации о заявке на возврат rFBS.

    Attributes:
        returns: Информация о заявке на возврат
    """
    returns: Optional[ReturnsRfbsGetReturn] = Field(
        None, description="Информация о заявке на возврат."
    )
