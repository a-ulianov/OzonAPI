"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarSetV6"""
from typing import Optional

from pydantic import BaseModel, Field

from src.ozonapi.seller.common.enumerations.postings import PaymentTypeGroupName, MarkType


class FBSPostingProductExemplarSetExemplarMark(BaseModel):
    """Контрольный идентификационный знак (КИЗ) или другая маркировка.

    Attributes:
        mark: Значение кода маркировки
        mark_type: Тип кода маркировки
    """
    mark: Optional[str] = Field(
        None, description="Значение кода маркировки."
    )
    mark_type: Optional[MarkType] = Field(
        None, description="Тип кода маркировки."
    )


class FBSPostingProductExemplarSetExemplar(BaseModel):
    """Описание экземпляра.

    Attributes:
        exemplar_id: Идентификатор экземпляра
        gtd: Номер грузовой таможенной декларации (ГТД)
        is_gtd_absent: Признак того, что не указан номер грузовой таможенной декларации (ГТД)
        is_rnpt_absent: Признак того, что не указан регистрационный номер партии товара (РНПТ)
        marks: Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре
        rnpt: Регистрационный номер партии товара (РНПТ)
        weight: Фактический вес экземпляра
    """
    exemplar_id: Optional[int] = Field(
        None, title="Идентификатор экземпляра."
    )
    gtd: Optional[str] = Field(
        None, description="Номер грузовой таможенной декларации (ГТД)."
    )
    is_gtd_absent: Optional[bool] = Field(
        True, description="Признак того, что не указан номер грузовой таможенной декларации (ГТД)."
    )
    is_rnpt_absent: Optional[bool] = Field(
        True, description="Признак того, что не указан регистрационный номер партии товара (РНПТ)."
    )
    marks: Optional[list[FBSPostingProductExemplarSetExemplarMark]] = Field(
        default_factory=list, description="Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре."
    )
    rnpt: Optional[str] = Field(
        None, description="Регистрационный номер партии товара (РНПТ)."
    )
    weight: Optional[float] = Field(
        None, description="Фактический вес экземпляра."
    )


class FBSPostingProductExemplarSetProduct(BaseModel):
    """Описание товара.

    Attributes:
        exemplars: Информация об экземплярах
        product_id: Идентификатор товара в системе Ozon
    """
    exemplars: list[FBSPostingProductExemplarSetExemplar] = Field(
        ..., description="Информация об экземплярах."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU."
    )


class FBSPostingProductExemplarSetRequest(BaseModel):
    """Описывает схему запроса на проверку и сохранение данных об экземплярах.

    Attributes:
        multi_box_qty: Количество коробок, в которые упакован товар
        posting_number: Номер отправления
        products: Список товаров
    """
    multi_box_qty: int = Field(
        ..., description="Количество коробок, в которые упакован товар.")
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[FBSPostingProductExemplarSetProduct] = Field(
        ..., description="Список товаров."
    )


class FBSPostingProductExemplarSetResponseDetails(BaseModel):
    """Дополнительная информация об ошибке.

    Attributes:
        type_url: Тип протокола передачи данных
        value: Значение ошибки
    """

    model_config = {'populate_by_name': True}

    type_url: Optional[str] = Field(
        None, description="Тип протокола передачи данных.",
        alias="typeUrl",
    )
    value: str = Field(
        None, description="Значение ошибки."
    )


class FBSPostingProductExemplarSetResponse(BaseModel):
    """Описывает схему ответа на запрос на проверку и сохранение данных об экземплярах.

    Attributes:
        code: Код ошибки
        details: Дополнительная информация об ошибке
        message: Описание ошибки
    """
    code: Optional[int] = Field(
        None, description="Код ошибки."
    )
    details: Optional[list[FBSPostingProductExemplarSetResponseDetails]] = Field(
        default_factory=list, description="Дополнительная информация об ошибке."
    )
    message: Optional[str] = Field(
        None, description="Описание ошибки."
    )
