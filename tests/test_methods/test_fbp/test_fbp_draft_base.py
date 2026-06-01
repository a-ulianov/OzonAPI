import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpDraftGetRequest,
    FbpDraftGetResponse,
    FbpDraftListRequest,
    FbpDraftListResponse,
    FbpWarehouseListResponse,
)


class TestFbpWarehouseList:
    """Тесты для метода fbp_warehouse_list."""

    @pytest.mark.asyncio
    async def test_fbp_warehouse_list(self, api, mock_api_request):
        """Тестирует метод fbp_warehouse_list."""
        mock_api_request.return_value = {
            "warehouses": [
                {
                    "id": 111,
                    "name": "Партнёрский склад",
                    "partner_name": "Партнёр",
                    "address_detailing": {"city": "Москва", "country": "Россия"},
                    "is_bonded": False,
                    "supply_types": [1, 2],
                    "timezone_name": "Europe/Moscow",
                }
            ]
        }

        response = await api.fbp_warehouse_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/warehouse/list",
            payload={},
        )
        assert isinstance(response, FbpWarehouseListResponse)
        assert len(response.warehouses) == 1
        assert response.warehouses[0].id == 111
        assert response.warehouses[0].address_detailing.city == "Москва"
        assert response.warehouses[0].supply_types == [1, 2]


class TestFbpDraftGet:
    """Тесты для метода fbp_draft_get."""

    @pytest.mark.asyncio
    async def test_fbp_draft_get(self, api, mock_api_request):
        """Тестирует метод fbp_draft_get."""
        mock_api_request.return_value = {
            "id": 999,
            "supply_id": "555",
            "status": "NEW",
            "delivery_details": {
                "supply_type": "DROP_OFF",
                "drop_off_point": {"id": 7, "province_uuid": "uuid-1"},
            },
            "is_registration_available": True,
        }

        request = FbpDraftGetRequest(supply_id="555")
        response = await api.fbp_draft_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftGetResponse)
        assert response.id == 999
        assert response.status == "NEW"
        assert response.delivery_details.supply_type == "DROP_OFF"
        assert response.delivery_details.drop_off_point.id == 7
        assert response.is_registration_available is True


class TestFbpDraftList:
    """Тесты для метода fbp_draft_list."""

    @pytest.mark.asyncio
    async def test_fbp_draft_list(self, api, mock_api_request):
        """Тестирует метод fbp_draft_list."""
        mock_api_request.return_value = {
            "items": [
                {"id": 1, "supply_id": "10", "status": "NEW"},
                {"id": 2, "supply_id": "11", "status": "SUPPLY_VARIANT_CONFIRMATION"},
            ],
            "has_next": True,
        }

        request = FbpDraftListRequest(count=50)
        response = await api.fbp_draft_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpDraftListResponse)
        assert response.has_next is True
        assert len(response.items) == 2
        assert response.items[0].id == 1
        assert response.items[1].status == "SUPPLY_VARIANT_CONFIRMATION"
