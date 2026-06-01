import pytest

from src.ozonapi.seller.schemas.warehouses import (
    DeliveryMethodListV1Filter,
    DeliveryMethodListV1Request,
    DeliveryMethodListV1Response,
)


class TestDeliveryMethodListV1:
    """Тесты для метода delivery_method_list_v1."""

    @pytest.mark.asyncio
    async def test_delivery_method_list_v1(self, api, mock_api_request):
        """Тестирует метод delivery_method_list_v1."""

        mock_api_request.return_value = {
            "has_next": False,
            "result": [{"id": 5, "name": "Метод", "status": "ACTIVE"}],
        }

        request = DeliveryMethodListV1Request(
            filter=DeliveryMethodListV1Filter(warehouse_id=1), limit=10
        )

        response = await api.delivery_method_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DeliveryMethodListV1Response)
        assert response.result[0].id == 5
