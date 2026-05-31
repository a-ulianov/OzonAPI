"""https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyFbsPostingList"""
from typing import Optional

from pydantic import BaseModel, Field

from .entities import AssemblyProduct


class AssemblyFbsPostingListFilter(BaseModel):
    """Фильтр для получения списка отправлений.

    Attributes:
        delivery_method_id: Идентификатор способа доставки
        cutoff_from: Начало периода времени сборки заказа
        cutoff_to: Конец периода времени сборки заказа
    """
    delivery_method_id: Optional[int] = Field(
        None, description="Идентификатор способа доставки."
    )
    cutoff_from: Optional[str] = Field(
        None, description="Начало периода времени, до которого продавцу нужно собрать заказ."
    )
    cutoff_to: Optional[str] = Field(
        None, description="Конец периода времени, до которого продавцу нужно собрать заказ."
    )


class AssemblyFbsPostingListRequest(BaseModel):
    """Описывает схему запроса на получение списка отправлений.

    Attributes:
        filter: Фильтр для поиска отправлений
        limit: Количество значений на странице
        sort_dir: Направление сортировки (`ASC` или `DESC`)
        cursor: Указатель для выборки следующих данных
    """
    filter: AssemblyFbsPostingListFilter = Field(
        ..., description="Фильтр для поиска отправлений."
    )
    limit: int = Field(
        ..., description="Количество значений на странице."
    )
    sort_dir: Optional[str] = Field(
        None, description="Направление сортировки: `ASC` — по возрастанию, `DESC` — по убыванию."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )


class AssemblyFbsPostingListPosting(BaseModel):
    """Отправление в списке.

    Attributes:
        posting_number: Номер отправления
        assembly_code: Код листа подбора
        products: Список товаров
    """
    posting_number: Optional[str] = Field(
        None, description="Номер отправления."
    )
    assembly_code: Optional[str] = Field(
        None, description="Код листа подбора."
    )
    products: Optional[list[AssemblyProduct]] = Field(
        None, description="Список товаров."
    )


class AssemblyFbsPostingListResponse(BaseModel):
    """Описывает схему ответа на запрос списка отправлений.

    Attributes:
        postings: Список отправлений
        cutoff: Время, до которого продавцу нужно собрать заказ
        cursor: Указатель для выборки следующих данных
    """
    postings: Optional[list[AssemblyFbsPostingListPosting]] = Field(
        None, description="Список отправлений."
    )
    cutoff: Optional[str] = Field(
        None, description="Время, до которого продавцу нужно собрать заказ."
    )
    cursor: Optional[str] = Field(
        None, description="Указатель для выборки следующих данных."
    )
