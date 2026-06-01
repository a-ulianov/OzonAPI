import pytest

from src.ozonapi.seller.schemas.warehouses import (
    WarehouseFBSReturnMileCheckRequest,
    WarehouseFBSReturnMileCheckResponse,
)


class TestWarehouseFBSReturnMileCheck:
    """Тесты для метода warehouse_fbs_return_mile_check."""

    @pytest.mark.asyncio
    async def test_warehouse_fbs_return_mile_check(self, api, mock_api_request):
        """Тестирует метод warehouse_fbs_return_mile_check."""

        mock_api_request.return_value = {
            "should_set_return_mile": True,
            "unavailability_reasons": ["NO_POINTS"],
        }

        request = WarehouseFBSReturnMileCheckRequest(
            warehouse_id=123, country_code="RU", first_mile_type="DROP_OFF"
        )

        response = await api.warehouse_fbs_return_mile_check(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/return-mile/check",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, WarehouseFBSReturnMileCheckResponse)
        assert response.should_set_return_mile is True
        assert response.unavailability_reasons == ["NO_POINTS"]
