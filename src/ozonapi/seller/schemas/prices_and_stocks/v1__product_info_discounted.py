"""https://docs.ozon.ru/api/seller/#operation/ProductAPI_GetProductInfoDiscounted"""
from pydantic import BaseModel, Field


class ProductInfoDiscountedRequest(BaseModel):
    """Схема запроса на получение информации об уценённых товарах.

    Attributes:
        discounted_skus: Список SKU уценённых товаров
    """
    discounted_skus: list[str] = Field(
        ..., description="Список SKU уценённых товаров.",
        min_length=1
    )


class ProductInfoDiscountedItem(BaseModel):
    """Схема информации об уценке и основном товаре по SKU уценённого товара.

    Attributes:
        comment_reason_damaged: Комментарий к причине повреждения
        condition: Состояние товара — новый или Б/У
        condition_estimation: Состояние товара по шкале от 1 до 7
        defects: Дефекты товара
        discounted_sku: SKU уценённого товара
        mechanical_damage: Описание механического повреждения
        package_damage: Описание повреждения упаковки
        packaging_violation: Признак нарушения целостности упаковки
        reason_damaged: Причина повреждения
        repair: Признак, что товар отремонтирован
        shortage: Признак, что товар некомплектный
        sku: SKU основного товара
        warranty_type: Наличие у товара действующей гарантии
    """
    comment_reason_damaged: str = Field(
        ..., description="Комментарий к причине повреждения."
    )
    condition: str = Field(
        ..., description="Состояние товара — новый или Б/У."
    )
    condition_estimation: str = Field(
        ..., description="Состояние товара по шкале от 1 до 7: 1 — удовлетворительное, "
                         "2 — хорошее, 3 — очень хорошее, 4 — отличное, 5–7 — как новый."
    )
    defects: str = Field(
        ..., description="Дефекты товара."
    )
    discounted_sku: int = Field(
        ..., description="SKU уценённого товара."
    )
    mechanical_damage: str = Field(
        ..., description="Описание механического повреждения."
    )
    package_damage: str = Field(
        ..., description="Описание повреждения упаковки."
    )
    packaging_violation: str = Field(
        ..., description="Признак нарушения целостности упаковки."
    )
    reason_damaged: str = Field(
        ..., description="Причина повреждения."
    )
    repair: str = Field(
        ..., description="Признак, что товар отремонтирован."
    )
    shortage: str = Field(
        ..., description="Признак, что товар некомплектный."
    )
    sku: int = Field(
        ..., description="SKU основного товара."
    )
    warranty_type: str = Field(
        ..., description="Наличие у товара действующей гарантии."
    )


class ProductInfoDiscountedResponse(BaseModel):
    """Схема ответа на запрос информации об уценённых товарах.

    Attributes:
        items: Информация об уценке и основном товаре
    """
    items: list[ProductInfoDiscountedItem] = Field(
        ..., description="Информация об уценке и основном товаре."
    )
