from typing import Optional

from pydantic import Field, BaseModel

from .posting__mark import ProductExemplarMark, ProductExemplarMarkChecked


class ProductExemplarBase(BaseModel):
    """Описание экземпляра.

    Attributes:
        gtd: Номер грузовой таможенной декларации (ГТД)
        marks: Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре
        rnpt: Регистрационный номер партии товара (РНПТ)
        weight: Фактический вес экземпляра
    """
    gtd: Optional[str] = Field(
        None, description="Номер грузовой таможенной декларации (ГТД)."
    )
    marks: Optional[list[ProductExemplarMark]] = Field(
        default_factory=list, description="Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре."
    )
    rnpt: Optional[str] = Field(
        None, description="Регистрационный номер партии товара (РНПТ)."
    )
    weight: Optional[float] = Field(
        None, description="Фактический вес экземпляра."
    )

class ProductExemplar(ProductExemplarBase):
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
    is_gtd_absent: Optional[bool] = Field(
        True, description="Признак того, что не указан номер грузовой таможенной декларации (ГТД)."
    )
    is_rnpt_absent: Optional[bool] = Field(
        True, description="Признак того, что не указан регистрационный номер партии товара (РНПТ)."
    )


class ProductExemplarChecked(ProductExemplar):
    """Описание экземпляра.

    Attributes:
        exemplar_id: Идентификатор экземпляра
        gtd: Номер грузовой таможенной декларации (ГТД)
        gtd_check_status: Статус проверки грузовой таможенной декларации
        gtd_error_codes: Коды ошибок при проверке грузовой таможенной декларации
        is_gtd_absent: Признак того, что не указан номер грузовой таможенной декларации (ГТД)
        is_rnpt_absent: Признак того, что не указан регистрационный номер партии товара (РНПТ)
        marks: Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре
        rnpt: Регистрационный номер партии товара (РНПТ)
        rnpt_check_status: Статус проверки регистрационного номера партии товара
        rnpt_error_codes: Коды ошибок при проверке регистрационного номера партии товара
        weight: Фактический вес экземпляра
        weight_check_status: Статус проверки фактического веса
        weight_error_codes: Коды ошибок при проверке фактического веса
    """

    marks: Optional[list[ProductExemplarMarkChecked]] = Field(
        default_factory=list, description="Список контрольных идентификационных знаков (КИЗ) и других маркировок в одном экземпляре."
    )
    gtd_check_status: Optional[str] = Field(
        None, description="Статус проверки грузовой таможенной декларации."
    )
    gtd_error_codes: Optional[list[str]] = Field(
        default_factory=list, description="Коды ошибок при проверке грузовой таможенной декларации."
    )
    rnpt_check_status: Optional[str] = Field(
        None, description="Статус проверки регистрационного номера партии товара."
    )
    rnpt_error_codes: Optional[list[str]] = Field(
        default_factory=list, description="Коды ошибок при проверке регистрационного номера партии товара."
    )
    weight_check_status: Optional[str] = Field(
        None, description="Статус проверки фактического веса."
    )
    weight_error_codes: Optional[list[str]] = Field(
        default_factory=list, description="Коды ошибок при проверке фактического веса."
    )

