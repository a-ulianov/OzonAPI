"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_PostingFBSPackageLabel"""
from pydantic import BaseModel, Field


class PostingFBSPackageLabelRequest(BaseModel):
    """Описывает схему запроса на печать этикетки.

    Attributes:
        posting_number: Список идентификаторов отправлений
    """
    posting_number: list[str] = Field(
        ..., description = "Список идентификаторов отправлений.",
        max_length=20
    )


class PostingFBSPackageLabelResponse(BaseModel):
    """Описывает схему ответа на запрос о печати этикеток.

    Attributes:
        file_content: Содержание файла в бинарном виде
        file_name: Название файла
        content_type: Тип файла
    """
    file_content: str = Field(
        ..., description="Содержание файла в бинарном виде."
    )
    file_name: str = Field(
        ..., description="Название файла."
    )
    content_type: str = Field(
        ..., description="Тип файла."
    )