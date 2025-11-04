"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_CreateLabelBatchV2"""
from pydantic import BaseModel, Field

from ...common.enumerations.postings import LabelType


class PostingFBSPackageLabelCreateRequest(BaseModel):
    """Описывает схему запроса на формирование этикеток.

    Attributes:
        posting_number: Список идентификаторов отправлений
    """
    posting_number: list[str] = Field(
        ..., description = "Список идентификаторов отправлений."
    )


class PostingFBSPackageLabelCreateTask(BaseModel):
    """Описывает схему задачи на формирование этикетки.

    Attributes:
        task_id: Идентификатор задания на формирование этикеток (в зависимости от типа этикетки передайте значение в метод posting_fbs_package_label_get())
        task_type: Тип задания на формирование этикеток
    """
    task_id: int = Field(
        ..., description="Идентификатор задания на формирование этикеток (в зависимости от типа этикетки передайте значение в метод posting_fbs_package_label_get())."
    )
    task_type: LabelType = Field(
        ..., description="Тип задания на формирование этикеток"
    )


class PostingFBSPackageLabelCreateResult(BaseModel):
    """Список заданий на формирование этикеток.

    Attributes:
        tasks: Список заданий на формирование этикеток
    """
    tasks: list[PostingFBSPackageLabelCreateTask] = Field(
        ..., description = "Список заданий на формирование этикеток."
    )


class PostingFBSPackageLabelCreateResponse(BaseModel):
    """Описывает схему ответа на запрос о формировании этикеток.

    Attributes:
        result: Результат работы метода
    """
    result: PostingFBSPackageLabelCreateResult = Field(
        ..., description = "Результат работы метода."
    )