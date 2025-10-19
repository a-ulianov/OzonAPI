from pydantic import Field, BaseModel

from .posting__financial_data_products import PostingFBSFinancialDataProducts


class PostingFBSFinancialData(BaseModel):
    """Данные о стоимости товара, размере скидки, выплате и комиссии.

    Attributes:
        cluster_from: Код региона отправки заказа
        cluster_to: Код региона доставки заказа
        products: Список товаров в заказе
    """
    cluster_from: str = Field(
        ..., description="Код региона, откуда отправляется заказ."
    )
    cluster_to: str = Field(
        ..., description="Код региона, куда доставляется заказ."
    )
    products: list[PostingFBSFinancialDataProducts] = Field(
        ..., description="Список товаров в заказе."
    )