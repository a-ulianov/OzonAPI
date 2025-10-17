"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductArchive"""
from .base import BaseProductProductIdListRequest, BaseSimpleBoolResponse


class ProductArchiveRequest(BaseProductProductIdListRequest):
    """Описывает схему запроса на перенос товаров в архив.

    Attributes:
        product_id (list[int]): Список product_id для архивации (максимум 100 идентификаторов)
    """
    pass


class ProductArchiveResponse(BaseSimpleBoolResponse):
    """Описывает схему ответа на запрос о перемещение товаров в архив.

    Attributes:
        result (bool): Результат обработки запроса (true, если успешно)
    """
    pass