"""https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarValidateV5"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ProductExemplarBase, ProductExemplarMark


class FBSPostingProductExemplarValidateProduct(BaseModel):
    """Описывает свойства товара.

    Attributes:
        exemplars: Информация об экземплярах
        product_id: Идентификатор товара в системе Ozon
    """
    exemplars: Optional[list[ProductExemplarBase]] = Field(
        default_factory=list, description="Список экземпляров."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon."
    )


class FBSPostingProductExemplarValidateRequest(BaseModel):
    """Описывает схему запроса на валидацию кодов маркировки

    Attributes:
        posting_number: Номер отправления
        products: Список товаров
    """
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: Optional[list[FBSPostingProductExemplarValidateProduct]] = Field(
        ..., description="Список товаров."
    )


class FBSPostingProductExemplarValidateProductExemplarMarks(ProductExemplarMark):
    """Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок.

    Attributes:
        errors: Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок
        mark: Значение кода маркировки
        mark_type: Тип кода маркировки
        valid: Результат прохождения проверки (true, если контрольный идентификационный знак (КИЗ) и другие маркировки соответствуют требованиям)
    """
    errors: Optional[list[str]] = Field(
        default_factory=list, description="Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок."
    )
    valid: Optional[bool] = Field(
        None, description="Результат прохождения проверки (true, если контрольный идентификационный знак (КИЗ) и другие маркировки соответствуют требованиям)."
    )


class FBSPostingProductExemplarValidateProductExemplar(ProductExemplarBase):
    """Информация об экземпляре и результатах проверки.

    Attributes:
        gtd: Номер грузовой таможенной декларации (ГТД)
        marks: Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок
        rnpt: Регистрационный номер партии товара (РНПТ)
        weight: Фактический вес экземпляра
        errors: Ошибки валидации экземпляра
        valid: Результат прохождения проверки (true, если код экземпляра соответствует требованиям)
    """
    errors: Optional[list[str]] = Field(
        default_factory=list, description="Ошибки валидации экземпляра."
    )
    valid: Optional[bool] = Field(
        None, description="Результат прохождения проверки (true, если код экземпляра соответствует требованиям)."
    )
    marks: list[FBSPostingProductExemplarValidateProductExemplarMarks] = Field(
        default_factory=list, description="Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре и результатов проверки."
    )


class FBSPostingProductExemplarValidateResponseProduct(BaseModel):
    """Описывает информацию о товаре.

    Attributes:
        error: Код ошибки
        exemplars: Информация об экземплярах
        product_id: Идентификатор товара в системе Ozon
        valid: Результат прохождения проверки (true, если коды всех экземпляров соответствуют требованиям)
    """
    error: Optional[str] = Field(
        None, description="Код ошибки."
    )
    exemplars: Optional[list[FBSPostingProductExemplarValidateProductExemplar]] = Field(
        default_factory=list, description="Информация об экземплярах."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon."
    )
    valid: Optional[bool] = Field(
        None, description="Результат прохождения проверки (true, если коды всех экземпляров соответствуют требованиям)."
    )


class FBSPostingProductExemplarValidateResponse(BaseModel):
    """Описывает схему ответа на запрос на валидацию кодов маркировки.

    Attributes:
        products: Список товаров
    """
    products: Optional[list[FBSPostingProductExemplarValidateResponseProduct]] = Field(
        default_factory=list, description="Список товаров."
    )