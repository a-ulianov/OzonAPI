"""https://docs.ozon.ru/api/seller/?#operation/PostingAPI_SetCountryProductFbsPostingV2"""
from pydantic import BaseModel, Field


class PostingFBSProductCountrySetRequest(BaseModel):
    """Описывает схему запроса на добавление информации о стране-изготовителе товара.

    Attributes:
        posting_number: Номер отправления
        product_id: Идентификатор товара в системе продавца — product_id
        country_iso_code: Двухбуквенный код добавляемой страны по стандарту ISO_3166-1 (можно получить методом posting_fbs_product_country_list())
    """
    posting_number: str = Field(
        ..., title="Номер отправления."
    )
    product_id: int = Field(
        ..., title="Идентификатор товара в системе продавца."
    )
    country_iso_code: str = Field(
        ..., title="Двухбуквенный код добавляемой страны по стандарту ISO_3166-1 (можно получить методом posting_fbs_product_country_list())."
    )


class PostingFBSProductCountrySetResponse(BaseModel):
    """Описывает схему ответа на запрос на добавление информации о стране-изготовителе товара.

    Attributes:
        product_id: Идентификатор товара в системе продавца — product_id
        is_gtd_needed: Признак того, что необходимо передать номер грузовой таможенной декларации (ГТД) для продукта и отправления
    """
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — product_id."
    )
    is_gtd_needed: bool = Field(
        ..., description="Признак того, что необходимо передать номер грузовой таможенной декларации (ГТД) для продукта и отправления."
    )