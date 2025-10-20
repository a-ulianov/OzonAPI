import pytest
from unittest.mock import AsyncMock, patch
import datetime

from src.ozonapi.seller.methods import SellerFBSAPI
from src.ozonapi.seller.schemas.fbs import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse, PostingFBSListResponse, PostingFBSGetResponse, PostingFBSGetByBarcodeResponse,
    PostingFBSMultiBoxQtySetResponse,
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
                        "shipment_date": "2023-11-04T19:00:00Z",
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
    async def test_posting_multiboxqty_set(self, seller_fbs_api, mock_api_manager_request):
        """Тестирует метод posting_multiboxqty_set."""

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

        response = await seller_fbs_api.posting_multiboxqty_set(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/multi-box-qty/set",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSMultiBoxQtySetResponse)
        assert response.result.result is True