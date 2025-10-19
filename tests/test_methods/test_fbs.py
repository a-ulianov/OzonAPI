import pytest
from unittest.mock import AsyncMock, patch
import datetime

from src.ozonapi.seller.methods import SellerFBSAPI
from src.ozonapi.seller.schemas.fbs import (
    PostingFBSUnfulfilledListRequest,
    PostingFBSUnfulfilledListResponse, PostingFBSListResponse,
)
from src.ozonapi.seller.common.enumerations.requests import SortingDirection
from src.ozonapi.seller.common.enumerations.postings import (
    PostingStatus,
    AvailablePostingActions,
    PostingSubstatus,
    TplIntegrationType
)
from src.ozonapi.seller.common.enumerations.localization import CurrencyCode
from src.ozonapi.seller.schemas.fbs.v3__posting_fbs_unfulfilled_list import PostingFBSUnfulfilledListFilter, \
    PostingFBSUnfulfilledListFilterWith


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
            with_=PostingFBSUnfulfilledListFilterWith(
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
            PostingFBSListFilterWith,
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
            with_=PostingFBSListFilterWith(
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