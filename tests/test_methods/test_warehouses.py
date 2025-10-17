import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.common.enumerations.warehouses import WarehouseWorkingDays, WarehouseStatus
from src.ozonapi.seller.methods import SellerWarehouseAPI
from src.ozonapi.seller.schemas.warehouses import (
    WarehouseListResponse,
    DeliveryMethodListRequest,
    DeliveryMethodListResponse,
)
from src.ozonapi.seller.common.enumerations.delivery import DeliveryMethodStatus
from src.ozonapi.seller.schemas.warehouses.v1__delivery_method_list import DeliveryMethodListFilter


class TestSellerWarehouseAPI:
    """Тесты для класса SellerWarehouseAPI."""

    @pytest.fixture
    def seller_warehouse_api(self):
        """Фикстура для создания экземпляра SellerWarehouseAPI."""
        return SellerWarehouseAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerWarehouseAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_warehouse_list(self, seller_warehouse_api, mock_api_manager_request):
        """Тестирует метод warehouse_list."""

        mock_response_data = {
            "result": [
                {
                    "has_entrusted_acceptance": True,
                    "is_rfbs": False,
                    "name": "Основной склад FBS",
                    "warehouse_id": 15588127982000,
                    "can_print_act_in_advance": True,
                    "first_mile_type": {
                        "dropoff_point_id": "point_123",
                        "dropoff_timeslot_id": 456,
                        "first_mile_is_changing": False,
                        "first_mile_type": "DropOff"
                    },
                    "has_postings_limit": True,
                    "is_karantin": False,
                    "is_kgt": True,
                    "is_economy": False,
                    "is_timetable_editable": True,
                    "min_postings_limit": 10,
                    "postings_limit": 100,
                    "min_working_days": 5,
                    "status": WarehouseStatus.CREATED,
                    "working_days": [
                        WarehouseWorkingDays.MONDAY,
                    ]
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        response = await seller_warehouse_api.warehouse_list()

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/list",
        )
        assert isinstance(response, WarehouseListResponse)
        assert len(response.result) == 1
        warehouse = response.result[0]
        assert warehouse.warehouse_id == 15588127982000
        assert warehouse.name == "Основной склад FBS"
        assert warehouse.is_rfbs is False
        assert warehouse.has_entrusted_acceptance is True
        assert warehouse.first_mile_type.first_mile_type == "DropOff"

    @pytest.mark.asyncio
    async def test_delivery_method_list(self, seller_warehouse_api, mock_api_manager_request):
        """Тестирует метод delivery_method_list."""

        mock_response_data = {
            "result": [
                {
                    "id": 12345,
                    "name": "Курьерская доставка",
                    "warehouse_id": 15588127982000,
                    "company_id": 424,
                    "created_at": "2023-10-01T10:00:00Z",
                    "cutoff": "18:00",
                    "provider_id": 424,
                    "sla_cut_in": 120,
                    "status": "ACTIVE",
                    "template_id": 789,
                    "updated_at": "2023-10-01T10:00:00Z"
                }
            ],
            "has_next": False
        }
        mock_api_manager_request.return_value = mock_response_data

        request = DeliveryMethodListRequest(
            filter=DeliveryMethodListFilter(
                provider_id=424,
                status=DeliveryMethodStatus.ACTIVE,
                warehouse_id=15588127982000
            ),
            limit=50,
            offset=0
        )
        response = await seller_warehouse_api.delivery_method_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            json=request.model_dump(),
        )
        assert isinstance(response, DeliveryMethodListResponse)
        assert len(response.result) == 1
        assert response.has_next is False

        delivery_method = response.result[0]
        assert delivery_method.id == 12345
        assert delivery_method.name == "Курьерская доставка"
        assert delivery_method.warehouse_id == 15588127982000
        assert delivery_method.provider_id == 424
        assert delivery_method.status == DeliveryMethodStatus.ACTIVE

    @pytest.mark.asyncio
    async def test_delivery_method_list_with_pagination(self, seller_warehouse_api, mock_api_manager_request):
        """Тестирует метод delivery_method_list с пагинацией."""

        mock_response_data = {
            "result": [
                {
                    "id": 12345,
                    "name": "Курьерская доставка",
                    "warehouse_id": 15588127982000,
                    "company_id": 424,
                    "created_at": "2023-10-01T10:00:00Z",
                    "cutoff": "18:00",
                    "provider_id": 424,
                    "sla_cut_in": 120,
                    "status": "ACTIVE",
                    "template_id": 789,
                    "updated_at": "2023-10-01T10:00:00Z"
                }
            ],
            "has_next": True
        }
        mock_api_manager_request.return_value = mock_response_data

        request = DeliveryMethodListRequest(
            filter=DeliveryMethodListFilter(
                warehouse_id=15588127982000
            ),
            limit=1,
            offset=10
        )
        response = await seller_warehouse_api.delivery_method_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            json=request.model_dump(),
        )
        assert isinstance(response, DeliveryMethodListResponse)
        assert len(response.result) == 1
        assert response.has_next is True
        assert response.result[0].id == 12345