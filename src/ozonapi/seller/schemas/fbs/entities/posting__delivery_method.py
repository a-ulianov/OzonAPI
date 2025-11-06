from pydantic import Field

from ...entities.postings import PostingDeliveryMethod


class PostingFBSDeliveryMethod(PostingDeliveryMethod):
    """Метод доставки.

    Attributes:
        id: Идентификатор способа доставки
        name: Название способа доставки
        tpl_provider: Служба доставки
        tpl_provider_id: Идентификатор службы доставки
        warehouse: Название склада
        warehouse_id: Идентификатор склада
    """
    tpl_provider: str = Field(
        ..., description="Служба доставки."
    )
    tpl_provider_id: int = Field(
        ..., description="Идентификатор службы доставки."
    )
    warehouse: str = Field(
        ..., description="Название склада."
    )