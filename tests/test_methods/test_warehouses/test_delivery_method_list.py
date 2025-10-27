import pytest

from src.ozonapi.seller.schemas.warehouses import (
    DeliveryMethodListRequest,
    DeliveryMethodListResponse,
)
from src.ozonapi.seller.common.enumerations.delivery import DeliveryMethodStatus
from src.ozonapi.seller.schemas.warehouses.v1__delivery_method_list import DeliveryMethodListFilter


class TestDeliveryMethodList:
    """Тесты для метода delivery_method_list."""

    @pytest.mark.asyncio
    async def test_delivery_method_list(self, api, mock_api_request):
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
        mock_api_request.return_value = mock_response_data

        request = DeliveryMethodListRequest(
            filter=DeliveryMethodListFilter(
                provider_id=424,
                status=DeliveryMethodStatus.ACTIVE,
                warehouse_id=15588127982000
            ),
            limit=50,
            offset=0
        )
        response = await api.delivery_method_list(request)

        mock_api_request.assert_called_once_with(
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
    async def test_delivery_method_list_with_pagination(self, api, mock_api_request):
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
        mock_api_request.return_value = mock_response_data

        request = DeliveryMethodListRequest(
            filter=DeliveryMethodListFilter(
                warehouse_id=15588127982000
            ),
            limit=1,
            offset=10
        )
        response = await api.delivery_method_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            json=request.model_dump(),
        )
        assert isinstance(response, DeliveryMethodListResponse)
        assert len(response.result) == 1
        assert response.has_next is True
        assert response.result[0].id == 12345