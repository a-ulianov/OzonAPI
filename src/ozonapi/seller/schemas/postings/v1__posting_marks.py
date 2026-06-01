"""Схемы метода posting_marks (маркировки экземпляров из отправления, v1)."""
from pydantic import BaseModel, Field


class PostingMarksIssuedExemplar(BaseModel):
    """Экземпляр с полученными маркировками.

    Attributes:
        exemplar_id: Идентификатор экземпляра
        mandatory_marks: Коды маркировки экземпляра
        posting_number: Номер отправления
        sku: Идентификатор товара в системе Ozon — SKU
    """
    exemplar_id: int = Field(0, description="Идентификатор экземпляра.")
    mandatory_marks: list[str] = Field(
        default_factory=list, description="Коды маркировки экземпляра."
    )
    posting_number: str = Field("", description="Номер отправления.")
    sku: int = Field(0, description="Идентификатор товара в системе Ozon — SKU.")


class PostingMarksNonIssuedExemplar(BaseModel):
    """Экземпляр без полученных маркировок.

    Attributes:
        exemplar_id: Идентификатор экземпляра
        posting_number: Номер отправления
        sku: Идентификатор товара в системе Ozon — SKU
    """
    exemplar_id: int = Field(0, description="Идентификатор экземпляра.")
    posting_number: str = Field("", description="Номер отправления.")
    sku: int = Field(0, description="Идентификатор товара в системе Ozon — SKU.")


class PostingMarksRequest(BaseModel):
    """Параметры запроса маркировок экземпляров.

    Attributes:
        posting_numbers: Номера отправлений
    """
    posting_numbers: list[str] = Field(..., description="Номера отправлений.")


class PostingMarksResponse(BaseModel):
    """Ответ с маркировками экземпляров из отправления.

    Attributes:
        invalid_postings: Номера отправлений с ошибками
        issued_exemplars: Экземпляры с полученными маркировками
        non_issued_exemplars: Экземпляры без полученных маркировок
    """
    invalid_postings: list[str] = Field(
        default_factory=list, description="Номера отправлений с ошибками."
    )
    issued_exemplars: list[PostingMarksIssuedExemplar] = Field(
        default_factory=list, description="Экземпляры с полученными маркировками."
    )
    non_issued_exemplars: list[PostingMarksNonIssuedExemplar] = Field(
        default_factory=list, description="Экземпляры без полученных маркировок."
    )
