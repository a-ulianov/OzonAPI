"""https://docs.ozon.com/api/seller/?__rr=1#operation/PostingAPI_FbsPostingProductExemplarSetV6"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import ProductExemplar


class FBSPostingProductExemplarSetExemplar(ProductExemplar):
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
    pass


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
