"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetLabelBatch"""
from typing import Optional

from pydantic import BaseModel, Field

from ...common.enumerations.postings import LabelFormingStatus


class PostingFBSPackageLabelGetRequest(BaseModel):
    """Описывает схему запроса на получение файла с этикетками.

    Attributes:
        task_id: Номер задания на формирование этикеток из ответа метода posting_fbs_package_label_create()
    """
    task_id: int = Field(
        ..., description="Номер задания на формирование этикеток из ответа метода posting_fbs_package_label_create()."
    )


class PostingFBSPackageLabelGetUnprintedPosting(BaseModel):
    """Информация об ошибке, из-за которой не получилось напечатать этикетки.

    Attributes:
        msg: Причина ошибки
        posting_number: Номер отправления
    """
    msg: Optional[str] = Field(
        None, description="Причина ошибки."
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )


class PostingFBSPackageLabelGetResult(BaseModel):
    """Описывает схему с информацией о сформированных этикетках.

    Attributes:
        error: Код ошибки
        file_url: Ссылка на файл с этикетками
        printed_postings_count: Количество напечатанных этикеток
        status: Статус формирования этикеток
        unprinted_postings: Информация об ошибках, из-за которых не получилось напечатать этикетки
        unprinted_postings_count: Количество этикеток, которые не получилось напечатать
    """
    error: Optional[str] = Field(
        None, description="Код ошибки."
    )
    file_url: Optional[str] = Field(
        None, description="Ссылка на файл с этикетками."
    )
    printed_postings_count: Optional[int] = Field(
        None, description="Количество напечатанных этикеток."
    )
    status: Optional[LabelFormingStatus | str] = Field(
        None, description="Статус формирования этикеток."
    )
    unprinted_postings: Optional[list[PostingFBSPackageLabelGetUnprintedPosting]] = Field(
        default_factory=list, description="Список ошибок, из-за которых не получилось напечатать этикетки."
    )
    unprinted_postings_count: Optional[int] = Field(
        None, description="Количество этикеток, которые не получилось напечатать."
    )


class PostingFBSPackageLabelGetResponse(BaseModel):
    """Описывает схему ответа на запрос о получении файла с этикетками.

    Attributes:
        result: Результат работы метода
    """
    result: PostingFBSPackageLabelGetResult = Field(
        ..., description="Результат работы метода."
    )