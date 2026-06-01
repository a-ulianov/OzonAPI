"""Схемы метода cargoes_label_get (идентификатор этикетки грузомест, v1)."""
from typing import Optional

from pydantic import BaseModel, Field

from .v1__cargoes_label_create import CargoesLabelErrors


class CargoesLabelGetRequest(BaseModel):
    """Параметры запроса идентификатора этикетки грузомест.

    Attributes:
        operation_id: Идентификатор операции генерации этикеток
    """
    operation_id: str = Field(
        ..., description="Идентификатор операции генерации этикеток."
    )


class CargoesLabelGetResult(BaseModel):
    """Результат генерации этикеток грузомест.

    Attributes:
        file_guid: Идентификатор для получения PDF-файла с этикетками
        file_url: Ссылка на PDF-файл с этикетками
    """
    file_guid: Optional[str] = Field(
        None, description="Идентификатор для получения PDF-файла с этикетками."
    )
    file_url: Optional[str] = Field(
        None, description="Ссылка на PDF-файл с этикетками."
    )


class CargoesLabelGetResponse(BaseModel):
    """Ответ с идентификатором этикетки грузомест.

    Attributes:
        result: Результат генерации этикеток
        status: Статус генерации этикеток
        errors: Ошибки операции
    """
    result: Optional[CargoesLabelGetResult] = Field(
        None, description="Результат генерации этикеток."
    )
    status: Optional[str] = Field(
        None, description="Статус генерации этикеток."
    )
    errors: Optional[CargoesLabelErrors] = Field(
        None, description="Ошибки операции."
    )
