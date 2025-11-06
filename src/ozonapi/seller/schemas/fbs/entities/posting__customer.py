from pydantic import Field

from ...entities.postings import PostingAddressee
from .posting__customer_address import PostingFBSCustomerAddress


class PostingFBSCustomer(PostingAddressee):
    """Данные о покупателе.

    Attributes:
        address: Информация об адресе доставки
        customer_id: Идентификатор покупателя
        name: Имя покупателя
        phone: Всегда возвращает пустую строку (получить подменный номер телефона posting_fbs_get())
    """
    address: PostingFBSCustomerAddress = Field(
        ..., description="Информация об адресе доставки."
    )
    customer_id: int = Field(
        ..., description="Идентификатор покупателя."
    )