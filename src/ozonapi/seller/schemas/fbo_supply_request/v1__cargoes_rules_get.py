"""Схемы метода cargoes_rules_get (чек-лист по установке грузомест FBO, v1)."""
from typing import Optional

from pydantic import BaseModel, Field


class CargoesRulesGetRequest(BaseModel):
    """Параметры запроса чек-листа по установке грузомест.

    Attributes:
        supply_ids: Идентификаторы поставок
    """
    supply_ids: Optional[list[str]] = Field(
        None, description="Идентификаторы поставок."
    )


class CargoesRulesCargoCountPerType(BaseModel):
    """Количество грузомест по типу.

    Attributes:
        count: Количество грузомест
        type: Тип грузоместа
    """
    count: Optional[int] = Field(None, description="Количество грузомест.")
    type: Optional[str] = Field(None, description="Тип грузоместа.")


class CargoesRulesPresentsRule(BaseModel):
    """Правило наличия грузомест.

    Attributes:
        cargo_count_per_type: Количество грузомест по типам
        count: Общее количество грузомест
        satisfied: Правило выполнено
    """
    cargo_count_per_type: Optional[list[CargoesRulesCargoCountPerType]] = Field(
        None, description="Количество грузомест по типам."
    )
    count: Optional[int] = Field(None, description="Общее количество грузомест.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesEditDeadlineExpireRule(BaseModel):
    """Правило срока редактирования грузомест.

    Attributes:
        is_applicable: Правило применимо
        is_required: Правило обязательно
        satisfied: Правило выполнено
    """
    is_applicable: Optional[bool] = Field(None, description="Правило применимо.")
    is_required: Optional[bool] = Field(None, description="Правило обязательно.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesExpireDatesPresentedRule(BaseModel):
    """Правило указания сроков годности товаров.

    Attributes:
        count_sku_with_expiration: Количество SKU со сроком годности
        count_sku_with_expiration_filled: Количество SKU с заполненным сроком годности
        is_applicable: Правило применимо
        is_required: Правило обязательно
        satisfied: Правило выполнено
    """
    count_sku_with_expiration: Optional[int] = Field(
        None, description="Количество SKU со сроком годности."
    )
    count_sku_with_expiration_filled: Optional[int] = Field(
        None, description="Количество SKU с заполненным сроком годности."
    )
    is_applicable: Optional[bool] = Field(None, description="Правило применимо.")
    is_required: Optional[bool] = Field(None, description="Правило обязательно.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesIsValidDistributionRule(BaseModel):
    """Правило корректного распределения товаров по грузоместам.

    Attributes:
        count_distributed_sku: Количество распределённых SKU
        count_sku_total: Общее количество SKU
        is_applicable: Правило применимо
        percents_int: Процент распределения
        satisfied: Правило выполнено
    """
    count_distributed_sku: Optional[int] = Field(
        None, description="Количество распределённых SKU."
    )
    count_sku_total: Optional[int] = Field(
        None, description="Общее количество SKU."
    )
    is_applicable: Optional[bool] = Field(None, description="Правило применимо.")
    percents_int: Optional[int] = Field(None, description="Процент распределения.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesPackageUnitsWithDistributionRule(BaseModel):
    """Правило распределения упаковочных единиц по грузоместам.

    Attributes:
        count_all: Общее количество упаковочных единиц
        count_with_distribution: Количество распределённых упаковочных единиц
        is_applicable: Правило применимо
        is_required: Правило обязательно
        satisfied: Правило выполнено
    """
    count_all: Optional[int] = Field(
        None, description="Общее количество упаковочных единиц."
    )
    count_with_distribution: Optional[int] = Field(
        None, description="Количество распределённых упаковочных единиц."
    )
    is_applicable: Optional[bool] = Field(None, description="Правило применимо.")
    is_required: Optional[bool] = Field(None, description="Правило обязательно.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesPlacementZonesRule(BaseModel):
    """Правило размещения грузомест в монозоне.

    Attributes:
        count_cargoes_all: Общее количество грузомест
        count_cargoes_with_mono_placement_zone: Количество грузомест с монозоной размещения
        is_applicable: Правило применимо
        satisfied: Правило выполнено
    """
    count_cargoes_all: Optional[int] = Field(
        None, description="Общее количество грузомест."
    )
    count_cargoes_with_mono_placement_zone: Optional[int] = Field(
        None, description="Количество грузомест с монозоной размещения."
    )
    is_applicable: Optional[bool] = Field(None, description="Правило применимо.")
    satisfied: Optional[bool] = Field(None, description="Правило выполнено.")


class CargoesRulesSupplyCheck(BaseModel):
    """Чек-лист по установке грузомест для поставки.

    Attributes:
        cargoes_presents_rule: Правило наличия грузомест
        edit_deadline_expire_rule: Правило срока редактирования
        expire_dates_presented_rule: Правило указания сроков годности
        is_valid_distribution_rule: Правило корректного распределения товаров
        package_units_with_distribution_rule: Правило распределения упаковочных единиц
        placement_zones_rule: Правило размещения в монозоне
        supply_id: Идентификатор поставки
    """
    cargoes_presents_rule: Optional[CargoesRulesPresentsRule] = Field(
        None, description="Правило наличия грузомест."
    )
    edit_deadline_expire_rule: Optional[CargoesRulesEditDeadlineExpireRule] = Field(
        None, description="Правило срока редактирования."
    )
    expire_dates_presented_rule: Optional[
        CargoesRulesExpireDatesPresentedRule
    ] = Field(None, description="Правило указания сроков годности.")
    is_valid_distribution_rule: Optional[
        CargoesRulesIsValidDistributionRule
    ] = Field(None, description="Правило корректного распределения товаров.")
    package_units_with_distribution_rule: Optional[
        CargoesRulesPackageUnitsWithDistributionRule
    ] = Field(None, description="Правило распределения упаковочных единиц.")
    placement_zones_rule: Optional[CargoesRulesPlacementZonesRule] = Field(
        None, description="Правило размещения в монозоне."
    )
    supply_id: Optional[int] = Field(None, description="Идентификатор поставки.")


class CargoesRulesGetResponse(BaseModel):
    """Ответ с чек-листом по установке грузомест.

    Attributes:
        supply_check_lists: Чек-листы по поставкам
    """
    supply_check_lists: Optional[list[CargoesRulesSupplyCheck]] = Field(
        None, description="Чек-листы по поставкам."
    )
