from typing import Optional

from pydantic import BaseModel, Field

from .posting__exemplar import ProductExemplar


class PostingProduct(BaseModel):
    """Информация о товаре и его экземплярах.

    Attributes:
        exemplars: Информация об экземплярах
        has_imei: Признак наличия IMEI
        is_gtd_needed: Признак того, что необходимо передать номер грузовой таможенной декларации (ГТД) для продукта и отправления
        is_jw_uin_needed: Признак того, что необходимо передать уникальный идентификационный номер ювелирного изделия (УИН)
        is_mandatory_mark_needed: Признак того, что необходимо передать маркировку «Честный ЗНАК»
        is_mandatory_mark_possible: Признак того, что возможно заполнить маркировку «Честный ЗНАК»
        is_rnpt_needed: Признак того, что необходимо передать номер партии товара (РНПТ)
        product_id: Идентификатор товара в системе Ozon — SKU
        quantity: Количество экземпляров
        is_weight_needed: `True`, если товар весовой
        weight_max: Максимальный вес экземпляра
        weight_min: Минимальный вес экземпляра
    """
    exemplars: Optional[list[ProductExemplar]] = Field(
        default_factory=list, description="Информация об экземплярах."
    )
    has_imei: Optional[bool] = Field(
        None, description="Признак наличия IMEI."
    )
    is_gtd_needed: Optional[bool] = Field(
        None, description="Признак того, что необходимо передать номер грузовой таможенной декларации (ГТД) для продукта и отправления."
    )
    is_jw_uin_needed: Optional[bool] = Field(
        None, description="Признак того, что необходимо передать уникальный идентификационный номер ювелирного изделия (УИН)."
    )
    is_mandatory_mark_needed: Optional[bool] = Field(
        None, description="Признак того, что необходимо передать маркировку «Честный ЗНАК»."
    )
    is_mandatory_mark_possible: Optional[bool] = Field(
        None, description="Признак того, что возможно заполнить маркировку «Честный ЗНАК»"
    )
    is_rnpt_needed: Optional[bool] = Field(
        None, description="Признак того, что необходимо передать номер партии товара (РНПТ)"
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе Ozon — SKU"
    )
    quantity: Optional[int] = Field(
        None, description="Количество экземпляров."
    )
    is_weight_needed: Optional[bool] = Field(
        None, description="true, если товар весовой."
    )
    weight_max: Optional[float] = Field(
        None, description="Максимальный вес экземпляра."
    )
    weight_min: Optional[float] = Field(
        None, description="Минимальный вес экземпляра."
    )