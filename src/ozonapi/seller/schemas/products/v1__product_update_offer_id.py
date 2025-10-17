"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateOfferID"""
from pydantic import BaseModel, Field


class ProductUpdateOfferIdRequestItem(BaseModel):
    """Описывает пару - текущий артикул / новый артикул.

    Attributes:
        offer_id: Текущий артикул
        new_offer_id: Новый артикул (максимум 50 символов)
    """
    offer_id: str = Field(
        ..., description="Текущий артикул."
    )
    new_offer_id: str = Field(
        ..., description="Новый артикул (максимум 50 символов).",
        max_length=50
    )


class ProductUpdateOfferIdRequest(BaseModel):
    """Описывает схему запроса на изменение offer_id, привязанных к товарам.

    Attributes:
        update_offer_id: Список пар текущий/новый артикул (максимум 250 пар)
    """
    update_offer_id: list[ProductUpdateOfferIdRequestItem] = Field(
        ..., description="Список пар текущий/новый артикул (максимум 250 пар).",
        max_length=250
    )


class ProductUpdateOfferIdError(BaseModel):
    """Список ошибок.

    Attributes:
        offer_id: Артикул, который не удалось изменить
        message: Сообщение об ошибке
    """
    offer_id: str = Field(..., description="Артикул, который не удалось изменить.")
    message: str = Field(..., description="Сообщение об ошибке.")


class ProductUpdateOfferIdResponse(BaseModel):
    """Описывает схему ответа на запрос об изменении offer_id.

    Attributes:
        errors: Информация об ошибках изменения offer_id
    """
    errors: list[ProductUpdateOfferIdError] = Field(
        default_factory=list, description="Информация об ошибках изменения offer_id."
    )