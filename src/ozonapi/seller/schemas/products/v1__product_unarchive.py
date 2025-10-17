"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUnarchive"""
from .base import BaseProductProductIdListRequest, BaseSimpleBoolResponse


class ProductUnarchiveRequest(BaseProductProductIdListRequest):
    """Описывает схему запроса на извлечение товаров из архива.

    Attributes:
        product_id (list[int]): Список product_id для архивации (максимум 100 идентификаторов)
    """
    pass


class ProductUnarchiveResponse(BaseSimpleBoolResponse):
    """Описывает схему ответа на запрос об извлечение товаров из архива.

    Attributes:
        result (bool): Результат обработки запроса (true, если успешно)
    """
    pass