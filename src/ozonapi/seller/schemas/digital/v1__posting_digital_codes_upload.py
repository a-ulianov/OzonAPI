"""Схемы метода posting_digital_codes_upload (загрузка кодов цифровых товаров, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class PostingDigitalCodesUploadExemplar(BaseModel):
    """Информация о кодах цифрового товара по SKU.

    Attributes:
        exemplar_keys: Список кодов цифрового товара (количество должно совпадать с `exemplar_qty`)
        exemplar_qty: Количество кодов, которые вы передаёте покупателю
        not_available_exemplar_qty: Количество кодов, которые вы не можете передать
        sku: Идентификатор товара в системе Ozon — SKU
    """
    exemplar_keys: Optional[list[str]] = Field(
        None,
        description="Список кодов цифрового товара. Количество кодов должно "
                    "совпадать с `exemplar_qty`."
    )
    exemplar_qty: int = Field(
        ..., description="Количество кодов цифрового товара, которые вы передаёте покупателю."
    )
    not_available_exemplar_qty: int = Field(
        ..., description="Количество кодов цифрового товара, которые вы не можете передать."
    )
    sku: int = Field(..., description="Идентификатор товара в системе Ozon — SKU.")


class PostingDigitalCodesUploadRequest(BaseModel):
    """Параметры запроса загрузки кодов цифровых товаров.

    Attributes:
        exemplars_by_sku: Коды цифровых товаров по SKU
        posting_number: Номер отправления
    """
    exemplars_by_sku: list[PostingDigitalCodesUploadExemplar] = Field(
        ..., description="Коды цифровых товаров по SKU."
    )
    posting_number: str = Field(..., description="Номер отправления.")


class PostingDigitalCodesUploadExemplarError(BaseModel):
    """Ошибка по коду цифрового товара.

    Attributes:
        key: Код цифрового товара
        message: Текст ошибки
    """
    key: str = Field("", description="Код цифрового товара.")
    message: str = Field("", description="Текст ошибки.")


class PostingDigitalCodesUploadResultExemplar(BaseModel):
    """Результат загрузки кодов по SKU.

    Attributes:
        failed_exemplars: Коды, которые не удалось загрузить
        received_qty: Количество принятых кодов
        rejected_qty: Количество отклонённых кодов
        sku: Идентификатор товара в системе Ozon — SKU
    """
    failed_exemplars: list[PostingDigitalCodesUploadExemplarError] = Field(
        default_factory=list, description="Коды, которые не удалось загрузить."
    )
    received_qty: int = Field(0, description="Количество принятых кодов.")
    rejected_qty: int = Field(0, description="Количество отклонённых кодов.")
    sku: int = Field(0, description="Идентификатор товара в системе Ozon — SKU.")


class PostingDigitalCodesUploadResponse(BaseModel):
    """Ответ на загрузку кодов цифровых товаров.

    Attributes:
        exemplars_by_sku: Результаты загрузки кодов по SKU
    """
    exemplars_by_sku: list[PostingDigitalCodesUploadResultExemplar] = Field(
        default_factory=list, description="Результаты загрузки кодов по SKU."
    )
