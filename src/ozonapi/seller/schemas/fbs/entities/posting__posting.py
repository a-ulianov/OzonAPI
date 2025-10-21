import datetime
from typing import Optional

from pydantic import Field, BaseModel

from ....common.enumerations.postings import AvailablePostingActions, PrrOption, PostingStatus, \
    PostingSubstatus, TplIntegrationType
from .posting__addressee import PostingFBSAddressee
from .posting__analytics_data import PostingFBSAnalyticsData
from .posting__barcodes import PostingFBSBarcodes
from .posting__cancellation import PostingFBSCancellation
from .posting__customer import PostingFBSCustomer
from .posting__delivery_method import PostingFBSDeliveryMethod
from .posting__financial_data import PostingFBSFinancialData
from .posting__legal_info import PostingFBSLegalInfo
from .posting__optional import PostingFBSOptional
from .posting__product import PostingFBSProductDetailed
from .posting__requirements import PostingFBSRequirements
from .posting__tariffication import PostingFBSTariffication


class PostingFBSPosting(BaseModel):
    """Информация об отправлении.

    Attributes:
        addressee: Контактные данные получателя
        analytics_data: Данные аналитики
        available_actions: Доступные действия
        barcodes: Штрихкоды отправления
        cancellation: Информация об отмене
        customer: Данные о покупателе
        delivering_date: Дата передачи отправления в доставку
        delivery_method: Метод доставки
        financial_data: Данные о стоимости товара
        in_process_at: Дата и время начала обработки отправления
        is_express: Признак быстрой доставки Ozon Express
        is_multibox: Признак многокоробочного товара
        legal_info: Юридическая информация о покупателе
        multi_box_qty: Количество коробок
        optional: Список товаров с дополнительными характеристиками
        order_id: Идентификатор заказа
        order_number: Номер заказа
        parent_posting_number: Номер родительского отправления
        pickup_code_verified_at: Дата успешной валидации кода курьера
        posting_number: Номер отправления
        products: Список товаров в отправлении
        prr_option: Код услуги погрузочно-разгрузочных работ
        quantum_id: Идентификатор эконом-товара
        requirements: Требования к товарам
        shipment_date: Дата и время, до которой необходимо собрать отправление. Показываем рекомендованное время отгрузки. По истечении этого времени начнёт применяться новый тариф, информацию о нём уточняйте в поле tariffication.
        shipment_date_without_delay: Дата и время отгрузки без просрочки
        status: Статус отправления
        substatus: Подстатус отправления
        tpl_integration_type: Тип интеграции со службой доставки
        tracking_number: Трек-номер отправления
        tariffication: Информация по тарификации отгрузки
    """
    addressee: Optional[PostingFBSAddressee] = Field(
        None, description="Контактные данные получателя.",
    )
    analytics_data: Optional[PostingFBSAnalyticsData] = Field(
        None, description="Данные аналитики."
    )
    available_actions: list[AvailablePostingActions] = Field(
        ..., description="Доступные действия и информация об отправлении."
    )
    barcodes: Optional[PostingFBSBarcodes] = Field(
        None, description="Штрихкоды отправления."
    )
    cancellation: Optional[PostingFBSCancellation] = Field(
        None, description="Информация об отмене."
    )
    customer: Optional[PostingFBSCustomer] = Field(
        None, description="Данные о покупателе."
    )
    delivering_date: Optional[datetime.datetime] = Field(
        ..., description="Дата передачи отправления в доставку."
    )
    delivery_method: PostingFBSDeliveryMethod = Field(
        ..., description="Метод доставки."
    )
    financial_data: Optional[PostingFBSFinancialData] = Field(
        None, description="Данные о стоимости товара, размере скидки, выплате и комиссии."
    )
    in_process_at: datetime.datetime = Field(
        ..., description="Дата и время начала обработки отправления."
    )
    is_express: bool = Field(
        ..., description="Если использовалась быстрая доставка Ozon Express — true."
    )
    is_multibox: bool = Field(
        ..., description="Признак, что в отправлении есть многокоробочный товар и нужно передать количество коробок."
    )
    legal_info: Optional[PostingFBSLegalInfo] = Field(
        None, description="Юридическая информация о покупателе."
    )
    multi_box_qty: Optional[int] = Field(
        None, description="Количество коробок, в которые упакован товар."
    )
    optional: Optional[PostingFBSOptional] = Field(
        None, description="Список товаров с дополнительными характеристиками."
    )
    order_id: int = Field(
        ..., description="Идентификатор заказа, к которому относится отправление."
    )
    order_number: str = Field(
        ..., description="Номер заказа, к которому относится отправление."
    )
    parent_posting_number: Optional[str] = Field(
        None, description="Номер родительского отправления, в результате разделения которого появилось текущее."
    )
    pickup_code_verified_at: Optional[datetime.datetime] = Field(
        None, description="Дата успешной валидации кода курьера. Проверить код posting_fbs_pick_up_code_verify()"
    )
    posting_number: str = Field(
        ..., description="Номер отправления."
    )
    products: list[PostingFBSProductDetailed] = Field(
        ..., description="Список товаров в отправлении."
    )
    prr_option: Optional[PrrOption] = Field(
        None, description="Код услуги погрузочно-разгрузочных работ."
    )
    quantum_id: Optional[int] = Field(
        None, description="Идентификатор эконом-товара."
    )
    requirements: PostingFBSRequirements = Field(
        ..., description="""
        Cписок продуктов, для которых нужно передать страну-изготовителя, номер грузовой таможенной декларации (ГТД), 
        регистрационный номер партии товара (РНПТ), маркировку «Честный ЗНАК», другие маркировки или вес, 
        чтобы перевести отправление в следующий статус.
        """
    )
    shipment_date: datetime.datetime = Field(
        ..., description="""
        Дата и время, до которой необходимо собрать отправление. Показываем рекомендованное время отгрузки. 
        По истечении этого времени начнёт применяться новый тариф, информацию о нём уточняйте в поле tariffication.
        """
    )
    shipment_date_without_delay: datetime.datetime = Field(
        ..., description="Дата и время отгрузки без просрочки."
    )
    status: PostingStatus = Field(
        ..., description="Статус отправления."
    )
    substatus: PostingSubstatus = Field(
        ..., description="Подстатус отправления."
    )
    tpl_integration_type: TplIntegrationType = Field(
        ..., description="Тип интеграции со службой доставки."
    )
    tracking_number: Optional[str] = Field(
        None, description="Трек-номер отправления."
    )
    tariffication: PostingFBSTariffication = Field(
        ..., description="Информация по тарификации отгрузки."
    )
