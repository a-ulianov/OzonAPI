"""https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyCarriagePostingList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import AssemblyProduct


class AssemblyCarriagePostingListFilter(BaseModel):
    """Фильтр для получения списка отправлений в отгрузке.

    Attributes:
        carriage_id: Идентификатор перевозки
        delivery_method_id: Идентификатор способа доставки
        cutoff_from: Начало периода времени сборки заказа
        cutoff_to: Конец периода времени сборки заказа
    """
    carriage_id: Optional[int] = Field(
        None, description="Идентификатор перевозки."
    )
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор способа доставки."
    )
    cutoff_from: Optional[str] = Field(
        None, description="Начало периода времени, до которого продавцу нужно собрать заказ."
    )
    cutoff_to: Optional[str] = Field(
        None, description="Конец периода времени, до которого продавцу нужно собрать заказ."
    )


class AssemblyCarriagePostingListRequest(BaseModel):
    """Описывает схему запроса на получение списка отправлений в отгрузке.

    Attributes:
        filter: Фильтр для поиска отправлений
        limit: Количество значений на странице
        cursor: Указатель для выборки следующих данных
    """
    filter: AssemblyCarriagePostingListFilter = Field(
        ..., description="Фильтр для поиска отправлений."
    )
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )


class AssemblyCarriagePostingListPosting(BaseModel):
    """Отправление в отгрузке.

    Attributes:
        posting_number: Номер отправления
        assembly_code: Код листа подбора
        can_print_label: Признак возможности печати этикетки
        products: Список товаров
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    assembly_code: Optional[str] = Field(
        None, description="Код листа подбора."
    )
    can_print_label: Optional[bool] = Field(
        None, description="`true`, если можно распечатать этикетку."
    )
    products: Optional[list[AssemblyProduct]] = Field(
        None, description="Список товаров."
    )


class AssemblyCarriagePostingListResponse(BaseModel):
    """Описывает схему ответа на запрос списка отправлений в отгрузке.

    Attributes:
        postings: Список отправлений
        can_print_mass_label: Признак возможности массовой печати этикеток
        cursor: Указатель для выборки следующих данных
    """
    postings: Optional[list[AssemblyCarriagePostingListPosting]] = Field(
        None, description="Список отправлений."
    )
    can_print_mass_label: Optional[bool] = Field(
        None, description="`true`, если можно распечатать этикетки массово."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
