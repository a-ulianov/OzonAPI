from pydantic import Field, BaseModel

from ....common.enumerations.localization import CurrencyCode


class PostingFBSFinancialDataProducts(BaseModel):
    """Список товаров в заказе.

    Attributes:
        actions: Список акций
        currency_code: Валюта цен
        commission_amount: Размер комиссии за товар
        commission_percent: Процент комиссии
        commissions_currency_code: Код валюты комиссий
        old_price: Цена до учёта скидок
        payout: Выплата продавцу
        price: Цена товара с учётом акций
        customer_price: Цена товара для покупателя
        product_id: Идентификатор товара в системе продавца
        quantity: Количество товара в отправлении
        total_discount_percent: Процент скидки
        total_discount_value: Сумма скидки
    """
    actions: list[str] = Field(
        ..., description="Список акций."
    )
    currency_code: CurrencyCode = Field(
        ..., description="Валюта ваших цен. Cовпадает с валютой, которая установлена в настройках личного кабинета."
    )
    commission_amount: float = Field(
        ..., description="Размер комиссии за товар."
    )
    commission_percent: float = Field(
        ..., description="Процент комиссии."
    )
    commissions_currency_code: CurrencyCode = Field(
        ..., description="Код валюты, в которой рассчитывались комиссии."
    )
    old_price: float = Field(
        ..., description="Цена до учёта скидок. На карточке товара отображается зачёркнутой."
    )
    payout: float = Field(
        ..., description="Выплата продавцу."
    )
    price: float = Field(
        ..., description="Цена товара с учётом акций, кроме акций за счёт Ozon."
    )
    customer_price: float = Field(
        ..., description="Цена товара для покупателя с учётом скидок продавца и Ozon."
    )
    product_id: int = Field(
        ..., description="Идентификатор товара в системе продавца."
    )
    quantity: int = Field(
        ..., description="Количество товара в отправлении."
    )
    total_discount_percent: float = Field(
        ..., description="Процент скидки."
    )
    total_discount_value: float = Field(
        ..., description="Сумма скидки."
    )
