"""Общая модель сертификата."""
from typing import Optional

from pydantic import BaseModel, Field


class Certificate(BaseModel):
    """Информация о сертификате.

    Attributes:
        certificate_id: Идентификатор
        certificate_number: Номер
        certificate_name: Название
        type_code: Тип
        status_code: Статус
        accordance_type_code: Тип соответствия требованиям
        rejection_reason_code: Причина отклонения сертификата
        verification_comment: Комментарий модератора
        issue_date: Дата создания
        expire_date: Дата окончания действия
        products_count: Количество товаров, привязанных к сертификату
    """
    certificate_id: Optional[int] = Field(
        None, description="Идентификатор."
    )
    certificate_number: Optional[str] = Field(
        None, description="Номер."
    )
    certificate_name: Optional[str] = Field(
        None, description="Название."
    )
    type_code: Optional[str] = Field(
        None, description="Тип."
    )
    status_code: Optional[str] = Field(
        None, description="Статус."
    )
    accordance_type_code: Optional[str] = Field(
        None, description="Тип соответствия требованиям."
    )
    rejection_reason_code: Optional[str] = Field(
        None, description="Причина отклонения сертификата."
    )
    verification_comment: Optional[str] = Field(
        None, description="Комментарий модератора."
    )
    issue_date: Optional[str] = Field(
        None, description="Дата создания."
    )
    expire_date: Optional[str] = Field(
        None, description="Дата окончания действия."
    )
    products_count: Optional[int] = Field(
        None, description="Количество товаров, привязанных к сертификату."
    )
