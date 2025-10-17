"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetImportProductsInfo"""
from pydantic import BaseModel, Field

from ...common.enumerations.products import ProductHandlingStatus


class ProductImportInfoRequest(BaseModel):
    """Описывает схему запроса, позволяющего получить статус создания или обновления карточки товара.

    Attributes:
        task_id: Код задачи на импорт товаров (можно получить с помощью метода product_import())
    """
    task_id: int = Field(
        ..., description="Код задачи на импорт товаров. Можно получить с помощью метода product_import().",
    )


class ProductImportInfoItemError(BaseModel):
    """Описывает схему ошибок, возникающих при добавлении или обновлении товара.

    Attributes:
        code: Код ошибки
        message: Техническое описание ошибки
        state: Состояние товара, в котором произошла ошибка
        level: Уровень ошибки
        description: Описание ошибки
        field: Поле, в котором произошла ошибка
        attribute_id: Атрибут, в котором произошла ошибка
        attribute_name: Название атрибута, в котором произошла ошибка
    """
    code: str = Field(
        ..., description="Код ошибки."
    )
    message: str = Field(
        ..., description="Техническое описание ошибки."
    )
    state: str = Field(
        ..., description="Состояние товара, в котором произошла ошибка."
    )
    level: str = Field(
        ..., description="Уровень ошибки."
    )
    description: str = Field(
        ..., description="Описание ошибки."
    )
    field: str = Field(
        ..., description="Поле, в котором произошла ошибка."
    )
    attribute_id: int = Field(
        ..., description="Атрибут, в котором произошла ошибка."
    )
    attribute_name: str = Field(
        ..., description="Название атрибута, в котором произошла ошибка."
    )


class ProductImportInfoItem(BaseModel):
    """Информация о результате обработки товара.

    Attributes:
        offer_id: Идентификатор товара в системе продавца — артикул
        product_id: Идентификатор товара в системе продавца
        status: Статус создания или обновления товара (информация о товаре обрабатывается очередями)
        errors: Массив ошибок, возникших при добавлении или обновлении товара
    """
    offer_id: str = Field(
        ..., description="Идентификатор товара в системе продавца — артикул."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    status: ProductHandlingStatus = Field(
        ..., description="Статус создания или обновления товара. Информация о товаре обрабатывается очередями."
    )
    errors: list[ProductImportInfoItemError] = Field(
        default_factory=list, description="Массив ошибок."
    )


class ProductImportInfoResult(BaseModel):
    """Информация об обработанных товарных карточках и их количестве.

    Attributes:
        items: Массив с информацией об обработанных товарах
        total: Общее количество обработанных товаров
    """
    items: list[ProductImportInfoItem] = Field(
        ..., description="Массив с информацией об обработанных товарах."
    )
    total: int = Field(
        ..., description="Общее количество обработанных товаров."
    )


class ProductImportInfoResponse(BaseModel):
    """Описывает схему ответа на запрос, позволяющий получить статус создания или обновления карточки товара.

    Attributes:
        result: Информация о результате выполнения запроса
    """
    result: ProductImportInfoResult = Field(
        ..., description="Информация о результате выполнения запроса."
    )