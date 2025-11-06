from typing import Optional

from pydantic import BaseModel, Field

from .financial_data_product import PostingFinancialDataProduct


class PostingFinancialData(BaseModel):
    """Данные о стоимости товара, размере скидки, выплате и комиссии.

    Attributes:
        cluster_from: Код региона отправки заказа
        cluster_to: Код региона доставки заказа
        products: Список товаров в заказе
    """
    cluster_from: Optional[str] = Field(
        None, description="Код региона, откуда отправляется заказ."
    )
    cluster_to: Optional[str] = Field(
        None, description="Код региона, куда доставляется заказ."
    )
    products: Optional[list[PostingFinancialDataProduct]] = Field(
        default_factory=list, description="Список товаров в заказе."
    )
