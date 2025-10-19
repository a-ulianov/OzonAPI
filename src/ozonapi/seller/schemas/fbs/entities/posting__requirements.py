from pydantic import Field, BaseModel


class PostingFBSRequirements(BaseModel):
    """Список продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД),
    регистрационный номер партии товара (РНПТ), маркировку «Честный ЗНАК», другие маркировки или вес,
    чтобы перевести отправление в следующий статус.

    Attributes:
        products_requiring_change_country: Список SKU для изменения страны-изготовителя
        products_requiring_gtd: Список SKU для передачи номеров ГТД
        products_requiring_country: Список SKU для передачи информации о стране-изготовителе
        products_requiring_mandatory_mark: Список SKU для передачи маркировки «Честный ЗНАК»
        products_requiring_jw_uin: Список товаров для передачи УИН ювелирного изделия
        products_requiring_rnpt: Список SKU для передачи РНПТ
        products_requiring_weight: Список товаров для передачи веса
        products_requiring_imei: Список идентификаторов товаров для передачи IMEI
    """
    products_requiring_change_country: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно изменить страну-изготовитель."
    )
    products_requiring_gtd: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать номера таможенной декларации (ГТД)."
    )
    products_requiring_country: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать информацию о стране-изготовителе."
    )
    products_requiring_mandatory_mark: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать маркировку «Честный ЗНАК»."
    )
    products_requiring_jw_uin: list[int] = Field(
        default_factory=list, description="Список товаров, для которых нужно передать уникальный идентификационный номер (УИН) ювелирного изделия."
    )
    products_requiring_rnpt: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров (SKU), для которых нужно передать регистрационный номер партии товара (РНПТ)."
    )
    products_requiring_weight: list[int] = Field(
        default_factory=list, description="Список товаров, для которых нужно передать вес."
    )
    products_requiring_imei: list[int] = Field(
        default_factory=list, description="Список идентификаторов товаров, для которых нужно передать IMEI."
    )
