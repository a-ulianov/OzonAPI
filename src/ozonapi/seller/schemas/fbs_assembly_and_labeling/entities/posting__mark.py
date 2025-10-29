from typing import Optional

from pydantic import Field, BaseModel

from ....common.enumerations.postings import MarkType


class ProductExemplarMark(BaseModel):
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


class ProductExemplarMarkChecked(ProductExemplarMark):
    """Контрольный идентификационный знак (КИЗ) или другая маркировка с информацией о проверке.

     Attributes:
        check_status: Статус проверки
        error_codes: Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок
        mark: Значение кода маркировки
        mark_type: Тип кода маркировки
    """
    check_status: Optional[str] = Field(
        None, description="Статус проверки."
    )
    error_codes: Optional[list[str]] = Field(
        default_factory=list, description="Ошибки при проверке контрольных идентификационных знаков (КИЗ) и других маркировок."
    )
