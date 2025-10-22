"""https://docs.ozon.com/api/seller/#operation/ProductAPI_ImportProductsPrices"""
from typing import Optional
from pydantic import BaseModel, Field, model_validator

from ...common.enumerations.localization import CurrencyCode
from ...common.enumerations.prices import PricingStrategy, VAT


class ProductImportPricesItem(BaseModel):
    """Схема для элемента цены товара при импорте.

    Attributes:
        auto_action_enabled: Признак автоприменения акций (опционально)
        auto_add_to_ozon_actions_list_enabled: Признак автодобавления товара в акции (опционально)
        currency_code: Валюта цен (опционально)
        manage_elastic_boosting_through_price: true, если товар участвует в эластичном бустинге, false, если не участвует (опционально, если ничего не передать, изменений в статусе участия не будет)
        min_price: Минимальная цена товара (опционально)
        min_price_for_auto_actions_enabled: Признак включения минимальной цены для автодействий (опционально)
        net_price: Себестоимость товара (опционально)
        offer_id: Идентификатор товара в системе продавца — артикул (опционально)
        old_price: Цена до учёта скидок (опционально)
        price: Цена товара с учётом скидок (опционально)
        price_strategy_enabled: Признак включения стратегии цены (опционально)
        product_id: Идентификатор товара в системе Ozon — product_id (опционально)
        quant_size: Размер квантования (опционально)
        vat: Ставка НДС для товара (опционально)
    """
    auto_action_enabled: Optional[PricingStrategy] = Field(
        PricingStrategy.UNKNOWN, description="Атрибут для включения и выключения автоматического применения к товару доступных акций Ozon."
    )
    auto_add_to_ozon_actions_list_enabled: Optional[PricingStrategy] = Field(
        PricingStrategy.UNKNOWN, description="Атрибут для включения и выключения автодобавления товара в акции."
    )
    currency_code: Optional[CurrencyCode] = Field(
        CurrencyCode.RUB, description="Валюта цен. Совпадает с валютой, которая установлена в настройках личного кабинета."
    )
    manage_elastic_boosting_through_price: Optional[bool] = Field(
        None, description="true, если товар участвует в эластичном бустинге, false, если не участвует (если ничего не передать, изменений в статусе участия не будет)."
    )
    min_price: Optional[str] = Field(
        None, description="Минимальная цена товара."
    )
    min_price_for_auto_actions_enabled: Optional[bool] = Field(
        None, description="true, если Ozon учитывает минимальную цену при добавлении в акции. Если ничего не передать, изменений в статусе учёта цены не будет."
    )
    net_price: Optional[str] = Field(
        None, description="Себестоимость товара."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    old_price: Optional[str] = Field(
        None,
        description="Цена до учёта скидок. На карточке товара отображается зачёркнутой. Чтобы сбросить, укажите 0."
    )
    price: Optional[str] = Field(
        None, description="Цена товара с учётом скидок — это значение показывается на карточке товара."
    )
    price_strategy_enabled: Optional[PricingStrategy] = Field(
        PricingStrategy.UNKNOWN, description="Атрибут для автоприменения стратегий цены."
    )
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    quant_size: Optional[int] = Field(
        None, description="""
        Используйте параметр, если у обычного и эконом-товара совпадает артикул — offer_id = quant_id.
        Чтобы обновить цену:
        - обычного товара — передайте значение 1;
        - эконом-товара — передайте размер его кванта.
        Если у обычного и эконом-товара разные артикулы, не передавайте параметр.
        """
    )
    vat: Optional[VAT] = Field(
        None, description="Ставка НДС для товара."
    )

    @model_validator(mode='after')
    def validate_offer_or_product_id(self) -> 'ProductImportPricesItem':
        """Проверяет, что указан хотя бы один идентификатор товара."""
        if not self.offer_id and not self.product_id:
            raise ValueError("Должен быть указан хотя бы один из параметров: offer_id или product_id")
        return self

    @model_validator(mode='after')
    def validate_prices_format(self) -> 'ProductImportPricesItem':
        """Проверяет корректность формата цен."""
        prices: list[str] = [self.min_price, self.net_price, self.old_price, self.price]
        for price in prices:
            if price is not None:
                try:
                    price = float(price)
                except ValueError:
                    raise ValueError(f"В товаре {self.offer_id or self.product_id} неправильный формат цены '{price}'.")
        return self

    @model_validator(mode='after')
    def validate_price_difference(self) -> 'ProductImportPricesItem':
        """Проверяет разницу между old_price и price."""
        if self.old_price is not None and self.price is not None:
            try:
                old_price_val = float(self.old_price)
                price_val = float(self.price)

            except ValueError:
                raise ValueError(f"Неправильный формат цены для товара {self.offer_id or self.product_id}.")

            else:
                if old_price_val > 0:
                    if old_price_val <= price_val:
                        raise ValueError("old_price должен быть больше price")

                    if self.currency_code == CurrencyCode.RUB:
                        if price_val < 400 and (old_price_val - price_val) < 20:
                            raise ValueError(
                                f"В товаре {self.offer_id or self.product_id} для price < 400 руб. разница между "
                                "ней и old_price должна быть не менее 20 руб."
                            )

                        if price_val > 10000 and (old_price_val - price_val) < 500:
                            raise ValueError(
                                f"В товаре {self.offer_id or self.product_id} для price > 10 000 руб. разница между "
                                "ней и old_price должна быть не менее 500 руб."
                            )

                        if 400 <= price_val <= 10000 and (price_val / old_price_val) > .95:
                            raise ValueError(
                                f"В товаре {self.offer_id or self.product_id} для price от 400 до 10 000 руб. "
                                "разница между ней и old_price должна быть не менее 5%."
                            )
        return self


class ProductImportPricesRequest(BaseModel):
    """Схема запроса на импорт цен товаров.

    Attributes:
        prices: Массив информации о ценах товаров (максимум 1000 элементов)
    """
    prices: list[ProductImportPricesItem] = Field(
        ..., description="Информация о ценах товаров.",
        min_length=1, max_length=1000
    )


class ProductImportPricesError(BaseModel):
    """Схема для ошибки при импорте цен.

    Attributes:
        code: Код ошибки
        message: Сообщение об ошибке
    """
    code: Optional[str] = Field(
        None, description="Код ошибки."
    )
    message: Optional[str] = Field(
        None, description="Сообщение об ошибке."
    )


class ProductImportPricesResultItem(BaseModel):
    """Схема для элемента результата импорта цен.

    Attributes:
        product_id: Идентификатор товара в системе Ozon
        offer_id: Идентификатор товара в системе продавца
        updated: Статус обновления
        errors: Массив ошибок
    """
    product_id: Optional[int] = Field(
        None, description="Идентификатор товара в системе Ozon — product_id."
    )
    offer_id: Optional[str] = Field(
        None, description="Идентификатор товара в системе продавца — артикул."
    )
    updated: bool = Field(
        ..., description="Если информация о товаре успешно обновлена — true."
    )
    errors: list[ProductImportPricesError] = Field(
        default_factory=list, description="Массив ошибок, которые возникли при обработке запроса."
    )


class ProductImportPricesResponse(BaseModel):
    """Схема ответа на запрос импорта цен.

    Attributes:
        result: Массив результатов обработки запросов
    """
    result: list[ProductImportPricesResultItem] = Field(
        ..., description="Список статусов и возможных ошибок."
    )