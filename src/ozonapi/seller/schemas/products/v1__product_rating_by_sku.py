"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductRatingBySku"""
from pydantic import BaseModel, Field


class ProductRatingBySkuItemGroupCondition(BaseModel):
    """Список условий, увеличивающих контент-рейтинг товара.

    Attributes:
        cost: Количество баллов контент-рейтинга, которое даёт выполнение условия
        description: Описание условия
        fulfilled: Признак, что условие выполнено
        key: Идентификатор условия
    """
    cost: float = Field(
        ..., description="Количество баллов контент-рейтинга, которое даёт выполнение условия."
    )
    description: str = Field(
        ..., description="Описание условия."
    )
    fulfilled: bool = Field(
        ..., description="Признак, что условие выполнено."
    )
    key: str = Field(
        ..., description="Идентификатор условия."
    )


class ProductRatingBySkuItemGroupImproveAttribute(BaseModel):
    """Атрибуты, заполнение которых может увеличить контент-рейтинг товара.

    Attributes:
        id: Идентификатор атрибута
        name: Название атрибута
    """
    id: int = Field(
        ..., description="Идентификатор атрибута."
    )
    name: str = Field(
        ..., description="Название атрибута."
    )


class ProductRatingBySkuItemGroup(BaseModel):
    """Информация о характеристиках, из которых складывается контент-рейтинг.

    Attributes:
        conditions: Список условий, увеличивающих контент-рейтинг товара
        improve_at_least: Количество атрибутов, которые нужно заполнить для получения максимального балла в этой группе характеристик
        improve_attributes: Cписок атрибутов, заполнение которых может увеличить контент-рейтинг товара
        key: Идентификатор группы
        name: Название группы
        rating: Рейтинг в группе
        weight: Процент влияния характеристик группы на контент-рейтинг
    """
    conditions: list[ProductRatingBySkuItemGroupCondition] = Field(
        default_factory=list, description="Список условий, увеличивающих контент-рейтинг товара."
    )
    improve_at_least: int = Field(
        ..., description="Количество атрибутов, которые нужно заполнить для получения максимального балла в этой группе характеристик."
    )
    improve_attributes: list[ProductRatingBySkuItemGroupImproveAttribute] = Field(
        default_factory=list, description="Cписок атрибутов, заполнение которых может увеличить контент-рейтинг товара."
    )
    key: str = Field(
        ..., description="Идентификатор группы."
    )
    name: str = Field(
        ..., description="Название группы."
    )
    rating: float = Field(
        ..., description="Рейтинг в группе."
    )
    weight: float = Field(
        ..., description="Процент влияния характеристик группы на контент-рейтинг."
    )


class ProductRatingBySkuItem(BaseModel):
    """Информация о рейтинге товара.

    Attributes:
        sku: Идентификатор товара на Ozon
        rating: Контент-рейтинг товара: от 0 до 100
        groups: Группы характеристик, из которых складывается контент-рейтинг
    """
    sku: int = Field(
        ..., description="Идентификатор товара на Ozon.",
    )
    rating: float = Field(
        ..., description="Контент-рейтинг товара: от 0 до 100.",
    )
    groups: list[ProductRatingBySkuItemGroup] = Field(
        default_factory=list, description="Группы характеристик, из которых складывается контент-рейтинг.",
    )


class ProductRatingBySkuRequest(BaseModel):
    """Описание схемы запроса для получения контент-рейтинга товаров, а также рекомендаций по его увеличению.

    Attributes:
        skus: Идентификаторы товаров в системе Ozon — SKU, для которых нужно вернуть контент-рейтинг
    """
    skus: list[int] = Field(
        ..., description="Список идентификаторов товаров в системе Ozon — SKU, для которых нужно вернуть контент-рейтинг."
    )


class ProductRatingBySkuResponse(BaseModel):
    """Описание схемы ответа на запрос для получения контент-рейтинга товаров, а также рекомендаций по его увеличению.

    Attributes:
        products: Список с информацией о контент-рейтинге товаров
    """
    products: list[ProductRatingBySkuItem] = Field(
        ..., description="Список с информацией о контент-рейтинге товаров."
    )
