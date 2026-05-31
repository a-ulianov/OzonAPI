import pytest

from src.ozonapi.seller.schemas.warehouses import (
    DeliveryMethodListRequest,
    DeliveryMethodListResponse,
    DeliveryMethodListFilter,
)
from src.ozonapi.seller.common.enumerations.delivery import DeliveryMethodStatus, SortDir


def _method() -> dict:
    return {
        "id": 12345,
        "name": "Курьерская доставка",
        "warehouse_id": 15588127982000,
        "provider_id": 424,
        "template_id": 789,
        "status": "ACTIVE",
        "cutoff": "18:00",
        "sla_cut_in": 120,
        "is_express": False,
        "tpl_integration_type": "ozon",
        "tpl_dropoff_point": {
            "address": "Москва, ул. Примерная, 1",
            "code": "MSK-1",
            "name": "ПВЗ Примерный",
            "address_coordinates": {"latitude": 55.75, "longitude": 37.61},
        },
        "created_at": "2023-10-01T10:00:00Z",
        "updated_at": "2023-10-01T10:00:00Z",
    }


class TestDeliveryMethodList:
    """Тесты для метода delivery_method_list (API v2)."""

    @pytest.mark.asyncio
    async def test_delivery_method_list(self, api, mock_api_request):
        """Тестирует метод delivery_method_list."""

        mock_api_request.return_value = {
            "delivery_methods": [_method()],
            "cursor": "",
            "has_next": False,
        }

        request = DeliveryMethodListRequest(
            filter=DeliveryMethodListFilter(
                warehouse_ids=["15588127982000"],
                status=[DeliveryMethodStatus.ACTIVE],
            ),
            limit=100,
            sort_dir=SortDir.ASC,
        )
        response = await api.delivery_method_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="delivery-method/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, DeliveryMethodListResponse)
        assert response.has_next is False
        assert len(response.delivery_methods) == 1

        method = response.delivery_methods[0]
        assert method.id == 12345
        assert method.name == "Курьерская доставка"
        assert method.warehouse_id == 15588127982000
        assert method.provider_id == 424
        assert method.status == "ACTIVE"
        assert method.tpl_dropoff_point.code == "MSK-1"
        assert method.tpl_dropoff_point.address_coordinates.latitude == 55.75

    @pytest.mark.asyncio
    async def test_delivery_method_list_with_pagination(self, api, mock_api_request):
        """Тестирует курсорную пагинацию метода delivery_method_list."""

        mock_api_request.return_value = {
            "delivery_methods": [_method()],
            "cursor": "next_cursor",
            "has_next": True,
        }

        request = DeliveryMethodListRequest(limit=1, cursor="prev_cursor")
        response = await api.delivery_method_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="delivery-method/list",
            payload=request.model_dump(),
        )
        assert response.has_next is True
        assert response.cursor == "next_cursor"
        assert response.delivery_methods[0].id == 12345
