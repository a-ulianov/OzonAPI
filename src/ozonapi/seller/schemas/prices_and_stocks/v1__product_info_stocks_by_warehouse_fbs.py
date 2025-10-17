"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductStocksByWarehouseFbs"""
from pydantic import Field, BaseModel


class ProductInfoStocksByWarehouseFBSRequest(BaseModel):
    """Описывает схему запроса информации об остатках на складах продавца (FBS и rFBS).

    Attributes:
        sku: Идентификаторы товаров в системе Ozon — SKU.
    """
    sku: list[int] = Field(
        default_factory=list, description="Идентификаторы товаров в системе Ozon — SKU."
    )


class ProductInfoStocksByWarehouseFBSItem(BaseModel):
    """Данные об остатках определенного товара по схемам FBS и rFBS.

    Attributes:
        sku: Идентификатор товара в системе Ozon
        present: Общее количество товара на складе
        product_id: Идентификатор товара в системе продавца
        reserved: Количество зарезервированных товаров
        warehouse_id: Идентификатор склада
        warehouse_name: Название склада
    """
    sku: int = Field(
        None, description="Идентификатор товара в системе Ozon — SKU."
    )
    present: int = Field(
        ..., description="Общее количество товара на складе."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    reserved: int = Field(
        ..., description="Количество зарезервированных товаров на складе."
    )
    warehouse_id: int = Field(
        ..., description="Идентификатор склада."
    )
    warehouse_name: str = Field(
        ..., description="Название склада."
    )


class ProductInfoStocksByWarehouseFBSResponse(BaseModel):
    """Описывает схему ответа на запрос информации о количестве остатков товаров по схемам FBS и rFBS.

    Attributes:
        result: Массив данных об остатках товаров по схемам FBS и rFBS
    """
    result: list[ProductInfoStocksByWarehouseFBSItem] = Field(
        ..., description="Массив данных об остатках товаров по схемам FBS и rFBS."
    )