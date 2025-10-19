from pydantic import BaseModel, Field


class PostingFBSLegalInfo(BaseModel):
    """Юридическая информация о покупателе.

    Attributes:
        company_name: Название компании
        inn: ИНН
        kpp: КПП
    """
    company_name: str = Field(
        ..., description="Название компании."
    )
    inn: str = Field(
        ..., description="ИНН."
    )
    kpp: str = Field(
        ..., description="КПП."
    )