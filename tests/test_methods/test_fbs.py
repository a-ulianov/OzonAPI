import pytest
from unittest.mock import AsyncMock, patch
import datetime

from src.ozonapi.seller.methods import SellerFBSAPI
from src.ozonapi.seller.schemas.fbs import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse, PostingFBSListResponse, PostingFBSGetResponse, PostingFBSGetByBarcodeResponse,
    PostingFBSMultiBoxQtySetResponse, PostingFBSProductChangeResponse, PostingFBSProductCountryListResponse,
    PostingFBSProductCountrySetResponse, PostingFBSRestrictionsResponse, PostingFBSPackageLabelResponse,
    PostingFBSPackageLabelCreateResponse, PostingFBSPackageLabelGetResponse, PostingFBSAwaitingDeliveryResponse,
    PostingFBSCancelReasonListResponse, PostingFBSCancelReasonResponse, PostingFBSProductCancelResponse,
    PostingFBSCancelResponse, PostingFBSArbitrationResponse,
)
from src.ozonapi.seller.common.enumerations.requests import SortingDirection
from src.ozonapi.seller.common.enumerations.postings import (
    PostingStatus,
    AvailablePostingActions,
    PostingSubstatus,
    TplIntegrationType
)
from src.ozonapi.seller.common.enumerations.localization import CurrencyCode
from src.ozonapi.seller.schemas.fbs.entities import PostingFBSFilterWith
from src.ozonapi.seller.schemas.fbs.v3__posting_fbs_unfulfilled_list import PostingFBSUnfulfilledListFilter


class TestSellerFBSAPI:
    """Тесты для класса SellerFBSAPI."""

    @pytest.fixture
    def seller_fbs_api(self):
        """Фикстура для создания экземпляра SellerFBSAPI."""
        return SellerFBSAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerFBSAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_posting_fbs_unfulfilled_list(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_unfulfilled_list."""

        mock_response_data = {
            "result": {
                "count": 2,
                "postings": [
                    {
                        "addressee": None,
                        "analytics_data": None,
                        "available_actions": [AvailablePostingActions.ARBITRATION],
                        "barcodes": None,
                        "cancellation": None,
                        "customer": None,
                        "delivering_date": "2023-10-01T10:00:00Z",
                        "delivery_method": {
                            "id": 12345,
                            "name": "Курьерская доставка",
                            "warehouse_id": 15588127982000,
                            "tpl_provider": "Ozon Логистика",
                            "tpl_provider_id": 424,
                            "warehouse": "Основной склад"
                        },
                        "financial_data": None,
                        "in_process_at": "2023-10-01T09:00:00Z",
                        "is_express": False,
                        "is_multibox": False,
                        "legal_info": None,
                        "multi_box_qty": None,
                        "optional": None,
                        "order_id": 123456789,
                        "order_number": "ORDER-123",
                        "parent_posting_number": None,
                        "pickup_code_verified_at": None,
                        "posting_number": "4567890123",
                        "products": [
                            {
                                "name": "Товар 1",
                                "offer_id": "TEST-001",
                                "price": 1500.0,
                                "quantity": 1,
                                "sku": 987654321,
                                "currency_code": CurrencyCode.RUB,
                                "is_blr_traceable": False,
                                "is_marketplace_buyout": False,
                                "imei": None
                            }
                        ],
                        "prr_option": None,
                        "quantum_id": None,
                        "requirements": {
                            "products_requiring_change_country": [],
                            "products_requiring_gtd": [],
                            "products_requiring_country": [],
                            "products_requiring_mandatory_mark": [],
                            "products_requiring_jw_uin": [],
                            "products_requiring_rnpt": [],
                            "products_requiring_weight": [],
                            "products_requiring_imei": []
                        },
                        "shipment_date": "2023-10-02T18:00:00Z",
                        "shipment_date_without_delay": "2023-10-02T18:00:00Z",
                        "status": PostingStatus.AWAITING_PACKAGING,
                        "substatus": PostingSubstatus.POSTING_CREATED,
                        "tpl_integration_type": TplIntegrationType.NON_INTEGRATED,
                        "tracking_number": None,
                        "tariffication": {
                            "current_tariff_rate": 10.0,
                            "current_tariff_type": "discount",
                            "current_tariff_charge": "150.0",
                            "current_tariff_charge_currency_code": "RUB",
                            "next_tariff_rate": 10.0,
                            "next_tariff_type": "discount",
                            "next_tariff_charge": "150.0",
                            "next_tariff_starts_at": None,
                            "next_tariff_charge_currency_code": "RUB"
                        }
                    },
                    {
                        "addressee": None,
                        "analytics_data": None,
                        "available_actions": [AvailablePostingActions.ARBITRATION],
                        "barcodes": None,
                        "cancellation": None,
                        "customer": None,
                        "delivering_date": "2023-10-01T11:00:00Z",
                        "delivery_method": {
                            "id": 12346,
                            "name": "Самовывоз",
                            "warehouse_id": 15588127982000,
                            "tpl_provider": "Ozon Логистика",
                            "tpl_provider_id": 424,
                            "warehouse": "Основной склад"
                        },
                        "financial_data": None,
                        "in_process_at": "2023-10-01T10:00:00Z",
                        "is_express": False,
                        "is_multibox": False,
                        "legal_info": None,
                        "multi_box_qty": None,
                        "optional": None,
                        "order_id": 123456790,
                        "order_number": "ORDER-124",
                        "parent_posting_number": None,
                        "pickup_code_verified_at": None,
                        "posting_number": "4567890124",
                        "products": [
                            {
                                "name": "Товар 2",
                                "offer_id": "TEST-002",
                                "price": 2000.0,
                                "quantity": 2,
                                "sku": 987654322,
                                "currency_code": CurrencyCode.RUB,
                                "is_blr_traceable": False,
                                "is_marketplace_buyout": False,
                                "imei": None
                            }
                        ],
                        "prr_option": None,
                        "quantum_id": None,
                        "requirements": {
                            "products_requiring_change_country": [],
                            "products_requiring_gtd": [],
                            "products_requiring_country": [],
                            "products_requiring_mandatory_mark": [],
                            "products_requiring_jw_uin": [],
                            "products_requiring_rnpt": [],
                            "products_requiring_weight": [],
                            "products_requiring_imei": []
                        },
                        "shipment_date": "2023-10-02T19:00:00Z",
                        "shipment_date_without_delay": "2023-10-02T19:00:00Z",
                        "status": PostingStatus.AWAITING_PACKAGING,
                        "substatus": PostingSubstatus.POSTING_CREATED,
                        "tpl_integration_type": TplIntegrationType.NON_INTEGRATED,
                        "tracking_number": None,
                        "tariffication": {
                            "current_tariff_rate": 10.0,
                            "current_tariff_type": "discount",
                            "current_tariff_charge": "200.0",
                            "current_tariff_charge_currency_code": "RUB",
                            "next_tariff_rate": 10.0,
                            "next_tariff_type": "discount",
                            "next_tariff_charge": "200.0",
                            "next_tariff_starts_at": None,
                            "next_tariff_charge_currency_code": "RUB"
                        }
                    }
                ]
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        request = PostingFBSUnfulfilledListRequest(
            filter=PostingFBSUnfulfilledListFilter(
                cutoff_from=datetime.datetime.now() - datetime.timedelta(days=7),
                cutoff_to=datetime.datetime.now(),
                delivery_method_id=[12345, 12346],
                is_quantum=True,
                provider_id=[424],
                status=PostingStatus.AWAITING_PACKAGING,
                warehouse_id=[15588127982000],
                last_changed_status_date=None
            ),
            dir=SortingDirection.ASC,
            limit=50,
            offset=0,
            with_=PostingFBSFilterWith(
                analytics_data=True,
                barcodes=True,
                financial_data=True
            )
        )
        response = await seller_fbs_api.posting_fbs_unfulfilled_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/unfulfilled/list",
            json=request.model_dump(by_alias=True)
        )
        assert isinstance(response, PostingFBSUnfulfilledListResponse)
        assert response.result.count == 2
        assert len(response.result.postings) == 2

        first_posting = response.result.postings[0]
        second_posting = response.result.postings[1]

        assert first_posting.posting_number == "4567890123"
        assert first_posting.delivery_method.name == "Курьерская доставка"
        assert second_posting.posting_number == "4567890124"
        assert second_posting.delivery_method.name == "Самовывоз"
        assert second_posting.products[0].quantity == 2

    @pytest.mark.asyncio
    async def test_posting_fbs_list(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_list."""

        mock_response_data = {
            "result": {
                "has_next": False,
                "postings": [
                    {
                        "addressee": None,
                        "analytics_data": None,
                        "available_actions": [AvailablePostingActions.ARBITRATION],
                        "barcodes": None,
                        "cancellation": None,
                        "customer": None,
                        "delivering_date": "2023-11-03T10:00:00Z",
                        "delivery_method": {
                            "id": 21321684811000,
                            "name": "Курьерская доставка",
                            "warehouse_id": 15588127982000,
                            "tpl_provider": "Ozon Логистика",
                            "tpl_provider_id": 24,
                            "warehouse": "Основной склад"
                        },
                        "financial_data": None,
                        "in_process_at": "2023-11-03T09:00:00Z",
                        "is_express": False,
                        "is_multibox": False,
                        "legal_info": None,
                        "multi_box_qty": None,
                        "optional": None,
                        "order_id": 123456789,
                        "order_number": "ORDER-123",
                        "parent_posting_number": None,
                        "pickup_code_verified_at": None,
                        "posting_number": "4567890123",
                        "products": [
                            {
                                "name": "Тестовый товар",
                                "offer_id": "TEST-001",
                                "price": 1500.0,
                                "quantity": 1,
                                "sku": 987654321,
                                "currency_code": CurrencyCode.RUB,
                                "is_blr_traceable": False,  # Добавлено
                                "is_marketplace_buyout": False,  # Добавлено
                                "imei": None  # Добавлено
                            }
                        ],
                        "prr_option": None,
                        "quantum_id": None,
                        "requirements": {
                            "products_requiring_gtd": [],
                            "products_requiring_country": [],
                            "products_requiring_mandatory_mark": []
                        },
                        "shipment_date": "2023-11-04T18:00:00Z",
                        "shipment_date_without_delay": "2023-11-04T18:00:00Z",
                        "status": PostingStatus.AWAITING_PACKAGING,
                        "substatus": PostingSubstatus.POSTING_CREATED,
                        "tpl_integration_type": TplIntegrationType.NON_INTEGRATED,
                        "tracking_number": None,
                        "tariffication": {
                            "current_tariff_rate": 10.0,
                            "current_tariff_type": "discount",
                            "current_tariff_charge": "150.0",
                            "current_tariff_charge_currency_code": CurrencyCode.RUB,
                            "next_tariff_rate": 10.0,
                            "next_tariff_type": "discount",
                            "next_tariff_charge": "150.0",
                            "next_tariff_starts_at": None,
                            "next_tariff_charge_currency_code": CurrencyCode.RUB
                        }
                    },
                    {
                        "addressee": None,
                        "analytics_data": None,
                        "available_actions": [AvailablePostingActions.ARBITRATION],
                        "barcodes": None,
                        "cancellation": None,
                        "customer": None,
                        "delivering_date": "2023-11-03T11:00:00Z",
                        "delivery_method": {
                            "id": 21321684811000,
                            "name": "Самовывоз",
                            "warehouse_id": 15588127982000,
                            "tpl_provider": "Ozon Логистика",
                            "tpl_provider_id": 24,
                            "warehouse": "Основной склад"
                        },
                        "financial_data": None,
                        "in_process_at": "2023-11-03T10:00:00Z",
                        "is_express": False,
                        "is_multibox": False,
                        "legal_info": None,
                        "multi_box_qty": None,
                        "optional": None,
                        "order_id": 123456790,
                        "order_number": "ORDER-124",
                        "parent_posting_number": None,
                        "pickup_code_verified_at": None,
                        "posting_number": "4567890124",
                        "products": [
                            {
                                "name": "Тестовый товар 2",
                                "offer_id": "TEST-002",
                                "price": 2000.0,
                                "quantity": 2,
                                "sku": 987654322,
                                "currency_code": CurrencyCode.RUB,
                                "is_blr_traceable": False,  # Добавлено
                                "is_marketplace_buyout": False,  # Добавлено
                                "imei": None  # Добавлено
                            }
                        ],
                        "prr_option": None,
                        "quantum_id": None,
                        "requirements": {
                            "products_requiring_gtd": [],
                            "products_requiring_country": [],
                            "products_requiring_mandatory_mark": []
                        },
                        "shipment_date": "2023-11-04T18:00:00Z",
                        "shipment_date_without_delay": "2023-11-04T18:00:00Z",
                        "status": PostingStatus.AWAITING_PACKAGING,
                        "substatus": PostingSubstatus.POSTING_CREATED,
                        "tpl_integration_type": TplIntegrationType.NON_INTEGRATED,
                        "tracking_number": None,
                        "tariffication": {
                            "current_tariff_rate": 10.0,
                            "current_tariff_type": "discount",
                            "current_tariff_charge": "200.0",
                            "current_tariff_charge_currency_code": "RUB",
                            "next_tariff_rate": 10.0,
                            "next_tariff_type": "discount",
                            "next_tariff_charge": "200.0",
                            "next_tariff_starts_at": None,
                            "next_tariff_charge_currency_code": "RUB"
                        }
                    }
                ]
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v3__posting_fbs_list import (
            PostingFBSListRequest,
            PostingFBSListFilter,
            PostingFBSFilterWith,
            PostingFBSListRequestFilterLastChangedStatusDate
        )

        request = PostingFBSListRequest(
            filter=PostingFBSListFilter(
                since=datetime.datetime(2023, 11, 3, 11, 47, 39, 878000),
                to_=datetime.datetime(2023, 11, 3, 11, 47, 39, 878000),
                delivery_method_id=[21321684811000],
                is_quantum=False,
                provider_id=[24],
                status=PostingStatus.AWAITING_PACKAGING,
                warehouse_id=[21321684811000],
                order_id=0,
                last_changed_status_date=PostingFBSListRequestFilterLastChangedStatusDate(
                    from_=datetime.datetime(2023, 11, 3, 11, 47, 39, 878000),
                    to_=datetime.datetime(2023, 11, 3, 11, 47, 39, 878000)
                )
            ),
            dir=SortingDirection.ASC,
            limit=100,
            offset=0,
            with_=PostingFBSFilterWith(
                analytics_data=True,
                barcodes=True,
                financial_data=True,
                translit=True
            )
        )

        response = await seller_fbs_api.posting_fbs_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/list",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSListResponse)
        assert response.result.has_next is False
        assert len(response.result.postings) == 2

        first_posting = response.result.postings[0]
        second_posting = response.result.postings[1]

        assert first_posting.posting_number == "4567890123"
        assert first_posting.delivery_method.tpl_provider_id == 24
        assert first_posting.status == PostingStatus.AWAITING_PACKAGING
        assert second_posting.posting_number == "4567890124"
        assert second_posting.products[0].quantity == 2
        assert second_posting.products[0].offer_id == "TEST-002"

    @pytest.mark.asyncio
    async def test_posting_fbs_get(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_get."""

        mock_response_data = {
            "result": {
                "additional_data": [],
                "addressee": None,
                "analytics_data": None,
                "available_actions": [AvailablePostingActions.ARBITRATION],
                "barcodes": None,
                "cancellation": {
                    "cancel_reason_id": 0,
                    "cancel_reason": "",
                    "cancellation_type": "",
                    "cancelled_after_ship": False,
                    "affect_cancellation_rating": False,
                    "cancellation_initiator": ""
                },
                "courier": None,
                "customer": None,
                "delivering_date": None,
                "delivery_method": {
                    "id": 18114520187000,
                    "name": "Ozon Логистика самостоятельно, Москва",
                    "warehouse_id": 18114520187000,
                    "warehouse": "Москва основной",
                    "tpl_provider_id": 24,
                    "tpl_provider": "Ozon Логистика"
                },
                "delivery_price": "",
                "financial_data": None,
                "in_process_at": "2021-11-20T09:14:16Z",
                "is_express": False,
                "is_multibox": False,
                "legal_info": None,
                "multi_box_qty": None,
                "optional": {
                    "products_with_possible_mandatory_mark": [0]
                },
                "order_id": 438764970,
                "order_number": "57195475-0050",
                "parent_posting_number": None,
                "pickup_code_verified_at": "2025-01-17T11:04:59.958Z",
                "posting_number": "57195475-0050-3",
                "product_exemplars": None,
                "products": [
                    {
                        "currency_code": CurrencyCode.RUB,
                        "is_blr_traceable": True,
                        "is_marketplace_buyout": True,
                        "price": "279.0000",
                        "offer_id": "250-7898-1",
                        "name": "Кофе ароматизированный \"Шоколадный апельсин\" 250 гр",
                        "sku": 180550365,
                        "quantity": 1,
                        "jw_uin": [],
                        "dimensions": {
                            "height": "40.00",
                            "length": "240.00",
                            "weight": "260",
                            "width": "140.00"
                        },
                        "has_imei": False
                    }
                ],
                "provider_status": "",
                "prr_option": None,
                "quantum_id": None,
                "related_postings": {
                    "related_posting_numbers": ["57195475-0050-4"]
                },
                "related_weight_postings": [],
                "requirements": {
                    "products_requiring_change_country": [],
                    "products_requiring_gtd": [],
                    "products_requiring_country": [],
                    "products_requiring_jwn": [],
                    "products_requiring_imei": []
                },
                "shipment_date": "2021-11-23T10:00:00Z",
                "shipment_date_without_delay": "2021-11-23T10:00:00Z",
                "status": PostingStatus.AWAITING_PACKAGING,
                "substatus": PostingSubstatus.POSTING_AWAITING_PASSPORT_DATA,
                "previous_substatus": PostingSubstatus.POSTING_TRANSFERRING_TO_DELIVERY,
                "tpl_integration_type": TplIntegrationType.OZON,
                "tracking_number": "",
                "tariffication": {
                    "current_tariff_rate": 0,
                    "current_tariff_type": "",
                    "current_tariff_charge": "",
                    "current_tariff_charge_currency_code": "",
                    "next_tariff_rate": 0,
                    "next_tariff_type": "",
                    "next_tariff_charge": "",
                    "next_tariff_starts_at": "2023-11-13T08:05:57.657Z",
                    "next_tariff_charge_currency_code": ""
                }
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v3__posting_fbs_get import (
            PostingFBSGetRequest,
            PostingFBSGetRequestWith
        )

        request = PostingFBSGetRequest(
            posting_number="57195475-0050-3",
            with_=PostingFBSGetRequestWith(
                analytics_data=False,
                barcodes=False,
                financial_data=False,
                legal_info=False,
                product_exemplars=False,
                related_postings=True,
                translit=False
            )
        )

        response = await seller_fbs_api.posting_fbs_get(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/get",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSGetResponse)
        assert response.result.posting_number == "57195475-0050-3"
        assert response.result.order_id == 438764970
        assert response.result.order_number == "57195475-0050"
        assert response.result.status == PostingStatus.AWAITING_PACKAGING
        assert response.result.substatus == PostingSubstatus.POSTING_AWAITING_PASSPORT_DATA
        assert response.result.previous_substatus == PostingSubstatus.POSTING_TRANSFERRING_TO_DELIVERY
        assert response.result.delivery_method.name == "Ozon Логистика самостоятельно, Москва"
        assert response.result.delivery_method.tpl_provider_id == 24
        assert len(response.result.products) == 1
        assert response.result.products[0].sku == 180550365
        assert response.result.products[0].offer_id == "250-7898-1"
        assert response.result.products[0].name == "Кофе ароматизированный \"Шоколадный апельсин\" 250 гр"
        assert response.result.related_postings.related_posting_numbers == ["57195475-0050-4"]

    @pytest.mark.asyncio
    async def test_posting_fbs_get_by_barcode(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_get_by_barcode."""
        mock_response_data = {
            "result": {
                "barcodes": {
                    "upper_barcode": "%101%10293145035",
                    "lower_barcode": "201864523528000"
                },
                "cancel_reason_id": 0,
                "created_at": "2025-01-29T08:58:07Z",
                "in_process_at": "2025-01-29T08:59:40Z",
                "order_id": 47558522075,
                "order_number": "2130415463-0013",
                "posting_number": "2130415463-0013-1",
                "products": [
                    {
                        "sku": 498274975,
                        "name": "Стульчик для кормления ребенка",
                        "quantity": 1,
                        "offer_id": "6460551001",
                        "price": "2300.0000"
                    }
                ],
                "shipment_date": "2025-01-29T18:00:00Z",
                "status": "delivered"
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_get_by_barcode import PostingFBSGetByBarcodeRequest

        request = PostingFBSGetByBarcodeRequest(
            barcode="20325804886000"
        )

        response = await seller_fbs_api.posting_fbs_get_by_barcode(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/get-by-barcode",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSGetByBarcodeResponse)
        assert response.posting_number == "2130415463-0013-1"
        assert response.order_id == 47558522075
        assert response.order_number == "2130415463-0013"
        assert response.status == "delivered"
        assert response.cancel_reason_id == 0
        assert response.barcodes.upper_barcode == "%101%10293145035"
        assert response.barcodes.lower_barcode == "201864523528000"
        assert len(response.products) == 1

        product = response.products[0]
        assert product.sku == 498274975
        assert product.name == "Стульчик для кормления ребенка"
        assert product.quantity == 1
        assert product.offer_id == "6460551001"
        assert product.price == 2300.00

        assert response.created_at.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 8, 58, 7)
        assert response.in_process_at.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 8, 59, 40)
        assert response.shipment_date.replace(tzinfo=None) == datetime.datetime(2025, 1, 29, 18, 0, 0)

    @pytest.mark.asyncio
    async def test_posting_fbs_multiboxqty_set(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_multiboxqty_set."""

        mock_response_data = {
            "result": {
                "result": True
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v3__posting_multiboxqty_set import (
            PostingFBSMultiBoxQtySetRequest
        )

        request = PostingFBSMultiBoxQtySetRequest(
            posting_number="57195475-0050-3",
            multi_box_qty=3
        )

        response = await seller_fbs_api.posting_fbs_multiboxqty_set(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/multi-box-qty/set",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSMultiBoxQtySetResponse)
        assert response.result.result is True

    @pytest.mark.asyncio
    async def test_posting_fbs_product_change(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_product_change."""

        mock_response_data = {
            "result": "33920158-0006-1"
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_change import (
            PostingFBSProductChangeRequest,
            PostingFBSProductChangeRequestItem
        )

        request = PostingFBSProductChangeRequest(
            posting_number="33920158-0006-1",
            items=[
                PostingFBSProductChangeRequestItem(
                    sku=1231428352,
                    weight_real=0.3
                )
            ]
        )

        response = await seller_fbs_api.posting_fbs_product_change(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/change",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSProductChangeResponse)
        assert response.result == "33920158-0006-1"

    @pytest.mark.asyncio
    async def test_posting_fbs_product_country_list(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_product_country_list и его кеширование."""

        mock_response_data = {
            "result": [
                {
                    "name": "Турция",
                    "country_iso_code": "TR"
                },
                {
                    "name": "Туркменистан",
                    "country_iso_code": "TM"
                },
                {
                    "name": "Тунис",
                    "country_iso_code": "TN"
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_country_list import (
            PostingFBSProductCountryListRequest
        )

        request = PostingFBSProductCountryListRequest(
            name_search="тУрЦ"
        )

        # Первый вызов - должен выполнить запрос к API
        response1 = await seller_fbs_api.posting_fbs_product_country_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/list",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response1, PostingFBSProductCountryListResponse)
        assert len(response1.result) == 3

        first_country = response1.result[0]
        second_country = response1.result[1]
        third_country = response1.result[2]

        assert first_country.name == "Турция"
        assert first_country.country_iso_code == "TR"
        assert second_country.name == "Туркменистан"
        assert second_country.country_iso_code == "TM"
        assert third_country.name == "Тунис"
        assert third_country.country_iso_code == "TN"

        # Второй вызов с теми же параметрами - должен вернуть закешированный результат
        response2 = await seller_fbs_api.posting_fbs_product_country_list(request)

        # Проверяем, что метод _request был вызван только один раз (кеширование работает)
        assert mock_api_manager_request.call_count == 1

        # Проверяем, что результаты одинаковые
        assert response1 == response2
        assert len(response2.result) == 3
        assert response2.result[0].name == "Турция"
        assert response2.result[0].country_iso_code == "TR"

    @pytest.mark.asyncio
    async def test_posting_fbs_product_country_set(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_product_country_set."""

        mock_response_data = {
            "product_id": 180550365,
            "is_gtd_needed": True
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_country_set import (
            PostingFBSProductCountrySetRequest
        )

        request = PostingFBSProductCountrySetRequest(
            posting_number="57195475-0050-3",
            product_id=180550365,
            country_iso_code="NO"
        )

        response = await seller_fbs_api.posting_fbs_product_country_set(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/set",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSProductCountrySetResponse)
        assert response.product_id == 180550365
        assert response.is_gtd_needed is True

    @pytest.mark.asyncio
    async def test_posting_fbs_restrictions(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_restrictions."""

        mock_response_data = {
            "result": {
                "posting_number": "76673629-0020-1",
                "max_posting_weight": 40000,
                "min_posting_weight": 0,
                "width": 500,
                "height": 500,
                "length": 500,
                "max_posting_price": 500000.0,
                "min_posting_price": 0.0
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_restrictions import (
            PostingFBSRestrictionsRequest
        )

        request = PostingFBSRestrictionsRequest(
            posting_number="76673629-0020-1"
        )

        response = await seller_fbs_api.posting_fbs_restrictions(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/restrictions",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSRestrictionsResponse)
        assert response.posting_number == "76673629-0020-1"
        assert response.max_posting_weight == 40000
        assert response.min_posting_weight == 0
        assert response.width == 500
        assert response.height == 500
        assert response.length == 500
        assert response.max_posting_price == 500000.0
        assert response.min_posting_price == 0.0

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_package_label."""

        mock_response_data = {
            "content_type": "application/pdf",
            "file_name": "ticket-170660-2023-07-13T13:17:06Z.pdf",
            "file_content": "%PDF-1.7\n%âãÏÓ\n53 0 obj\n<</MarkInfo<</Marked true/Type/MarkInfo>>/Pages 9 0 R/StructTreeRoot 10 0 R/Type/Catalog>>\nendobj\n8 0 obj\n<</Filter/FlateDecode/Length 2888>>\nstream\nxå[[ݶ\u0011~?¿BÏ\u0005Bs\u001c^\u0000Àwí5ú\u0010 m\u0016Èsà¦)\n;hÒ\u0014èÏïG\u0014)<{äµ] ]?¬¬oIÎ}¤F±óϤñï\u001bÕü×X­´OÏï?^~¹$<ø¨È9q\u0013Y\u0012åñì§_¼|ÿégü\t+\u0012\u001bxª}Æxҿ¿¼_º¼xg¦þ5OkuÌ3ýíògüûå\"Ni\u0016C\u0001°\u000fA9g'r¢\"\u0013YóĪ\u0018NÑ{\u001dÕóZ¬\\Ô\""
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_package_label import (
            PostingFBSPackageLabelRequest
        )

        request = PostingFBSPackageLabelRequest(
            posting_number=["48173252-0034-4", "48173252-0035-4"]
        )

        response = await seller_fbs_api.posting_fbs_package_label(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSPackageLabelResponse)
        assert response.content_type == "application/pdf"
        assert response.file_name == "ticket-170660-2023-07-13T13:17:06Z.pdf"
        assert isinstance(response.file_content, str)
        assert len(response.file_content) > 0
        assert response.file_content.startswith("%PDF-1.7")

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label_create(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_package_label_create."""

        mock_response_data = {
            "result": {
                "tasks": [
                    {
                        "task_id": 5819327210248,
                        "task_type": "big_label"
                    },
                    {
                        "task_id": 5819327210249,
                        "task_type": "small_label"
                    }
                ]
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_package_label_create import (
            PostingFBSPackageLabelCreateRequest
        )

        request = PostingFBSPackageLabelCreateRequest(
            posting_number=["4708216109137", "3697105098026"]
        )

        response = await seller_fbs_api.posting_fbs_package_label_create(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label/create",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSPackageLabelCreateResponse)
        assert len(response.result.tasks) == 2

        first_task = response.result.tasks[0]
        second_task = response.result.tasks[1]

        assert first_task.task_id == 5819327210248
        assert first_task.task_type == "big_label"
        assert second_task.task_id == 5819327210249
        assert second_task.task_type == "small_label"

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label_get(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_package_label_get."""

        mock_response_data = {
            "result": {
                "error": "",
                "status": "completed",
                "file_url": "https://cdn1.ozone.ru/s3/ord-tmp-12/small_label/ticket-00-0000-0000.pdf",
                "printed_postings_count": 1,
                "unprinted_postings_count": 0,
                "unprinted_postings": []
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_package_label_get import (
            PostingFBSPackageLabelGetRequest
        )

        request = PostingFBSPackageLabelGetRequest(
            task_id=5819327210248
        )

        response = await seller_fbs_api.posting_fbs_package_label_get(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/package-label/get",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSPackageLabelGetResponse)
        assert response.result.error == ""
        assert response.result.status == "completed"
        assert response.result.file_url == "https://cdn1.ozone.ru/s3/ord-tmp-12/small_label/ticket-00-0000-0000.pdf"
        assert response.result.printed_postings_count == 1
        assert response.result.unprinted_postings_count == 0
        assert response.result.unprinted_postings == []

    @pytest.mark.asyncio
    async def test_posting_fbs_awaiting_delivery(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_awaiting_delivery."""

        mock_response_data = {
            "result": True
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_awaiting_delivery import (
            PostingFBSAwaitingDeliveryRequest
        )

        request = PostingFBSAwaitingDeliveryRequest(
            posting_number=["33920143-1195-1", "33920143-1195-2"]
        )

        response = await seller_fbs_api.posting_fbs_awaiting_delivery(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/awaiting-delivery",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSAwaitingDeliveryResponse)
        assert response.result is True

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel_reason_list(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_cancel_reason_list."""

        mock_response_data = {
            "result": [
                {
                    "id": 352,
                    "title": "Товар закончился на складе продавца",
                    "type_id": "seller",
                    "is_available_for_cancellation": True
                },
                {
                    "id": 401,
                    "title": "Продавец отклонил арбитраж",
                    "type_id": "seller",
                    "is_available_for_cancellation": False
                },
                {
                    "id": 402,
                    "title": "Другое (вина продавца)",
                    "type_id": "seller",
                    "is_available_for_cancellation": True
                },
                {
                    "id": 666,
                    "title": "Возврат из службы доставки: нет доставки в указанный регион",
                    "type_id": "seller",
                    "is_available_for_cancellation": False
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        response = await seller_fbs_api.posting_fbs_cancel_reason_list()

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel-reason/list",
        )

        assert isinstance(response, PostingFBSCancelReasonListResponse)
        assert len(response.result) == 4

        first_reason = response.result[0]
        second_reason = response.result[1]
        third_reason = response.result[2]
        fourth_reason = response.result[3]

        assert first_reason.id_ == 352
        assert first_reason.title == "Товар закончился на складе продавца"
        assert first_reason.type_id == "seller"
        assert first_reason.is_available_for_cancellation is True

        assert second_reason.id_ == 401
        assert second_reason.title == "Продавец отклонил арбитраж"
        assert second_reason.type_id == "seller"
        assert second_reason.is_available_for_cancellation is False

        assert third_reason.id_ == 402
        assert third_reason.title == "Другое (вина продавца)"
        assert third_reason.type_id == "seller"
        assert third_reason.is_available_for_cancellation is True

        assert fourth_reason.id_ == 666
        assert fourth_reason.title == "Возврат из службы доставки: нет доставки в указанный регион"
        assert fourth_reason.type_id == "seller"
        assert fourth_reason.is_available_for_cancellation is False

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel_reason(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_cancel_reason."""

        mock_response_data = {
            "result": [
                {
                    "posting_number": "73837363-0010-3",
                    "reasons": [
                        {
                            "id": 352,
                            "title": "Товар закончился на складе продавца",
                            "type_id": "seller"
                        },
                        {
                            "id": 400,
                            "title": "Остался только бракованный товар",
                            "type_id": "seller"
                        },
                        {
                            "id": 402,
                            "title": "Другое (вина продавца)",
                            "type_id": "seller"
                        }
                    ]
                },
                {
                    "posting_number": "73837363-0011-3",
                    "reasons": [
                        {
                            "id": 665,
                            "title": "Покупатель не забрал заказ",
                            "type_id": "buyer"
                        },
                        {
                            "id": 667,
                            "title": "Заказ утерян службой доставки",
                            "type_id": "seller"
                        }
                    ]
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_cancel_reason import (
            PostingFBSCancelReasonRequest
        )

        request = PostingFBSCancelReasonRequest(
            related_posting_numbers=["73837363-0010-3", "73837363-0011-3"]
        )

        response = await seller_fbs_api.posting_fbs_cancel_reason(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/cancel-reason",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSCancelReasonResponse)
        assert len(response.result) == 2

        first_posting = response.result[0]
        second_posting = response.result[1]

        assert first_posting.posting_number == "73837363-0010-3"
        assert len(first_posting.reasons) == 3

        first_reason = first_posting.reasons[0]
        second_reason = first_posting.reasons[1]
        third_reason = first_posting.reasons[2]

        assert first_reason.id_ == 352
        assert first_reason.title == "Товар закончился на складе продавца"
        assert first_reason.type_id == "seller"

        assert second_reason.id_ == 400
        assert second_reason.title == "Остался только бракованный товар"
        assert second_reason.type_id == "seller"

        assert third_reason.id_ == 402
        assert third_reason.title == "Другое (вина продавца)"
        assert third_reason.type_id == "seller"

        assert second_posting.posting_number == "73837363-0011-3"
        assert len(second_posting.reasons) == 2

        fourth_reason = second_posting.reasons[0]
        fifth_reason = second_posting.reasons[1]

        assert fourth_reason.id_ == 665
        assert fourth_reason.title == "Покупатель не забрал заказ"
        assert fourth_reason.type_id == "buyer"

        assert fifth_reason.id_ == 667
        assert fifth_reason.title == "Заказ утерян службой доставки"
        assert fifth_reason.type_id == "seller"

    @pytest.mark.asyncio
    async def test_posting_fbs_product_cancel(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_product_cancel."""

        mock_response_data = {
            "result": "33920113-1231-1"
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_cancel import (
            PostingFBSProductCancelRequest,
            PostingFBSProductCancelItem
        )

        request = PostingFBSProductCancelRequest(
            cancel_reason_id=352,
            cancel_reason_message="Product is out of stock",
            items=[
                PostingFBSProductCancelItem(
                    quantity=5,
                    sku=150587396
                )
            ],
            posting_number="33920113-1231-1"
        )

        response = await seller_fbs_api.posting_fbs_product_cancel(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/cancel",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSProductCancelResponse)
        assert response.result == "33920113-1231-1"

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_cancel."""

        mock_response_data = {
            "result": True
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_cancel import (
            PostingFBSCancelRequest
        )

        request = PostingFBSCancelRequest(
            cancel_reason_id=352,
            cancel_reason_message="Product is out of stock",
            posting_number="33920113-1231-1"
        )

        response = await seller_fbs_api.posting_fbs_cancel(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSCancelResponse)
        assert response.result is True

    @pytest.mark.asyncio
    async def test_posting_fbs_arbitration(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_fbs_arbitration."""

        mock_response_data = {
            "result": True
        }
        mock_api_manager_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_arbitration import (
            PostingFBSArbitrationRequest
        )

        request = PostingFBSArbitrationRequest(
            posting_number=["33920143-1195-1", "33920143-1195-2"]
        )

        response = await seller_fbs_api.posting_fbs_arbitration(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/arbitration",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSArbitrationResponse)
        assert response.result is True