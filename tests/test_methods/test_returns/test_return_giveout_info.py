import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutInfoRequest, ReturnGiveoutInfoResponse


class TestReturnGiveoutInfo:
    """Тесты для метода return_giveout_info."""

    @pytest.mark.asyncio
    async def test_return_giveout_info(self, api, mock_api_request):
        """Тестирует метод return_giveout_info."""

        mock_response_data = {
            "giveout_id": 777,
            "giveout_status": "GIVEOUT_STATUS_NEW",
            "warehouse_name": "Склад",
            "articles": [
                {"name": "Товар", "seller_id": 555, "approved": True, "delivery_schema": "FBS"}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnGiveoutInfoRequest(giveout_id=777)

        response = await api.return_giveout_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnGiveoutInfoResponse)
        assert response.giveout_id == 777
        assert response.articles[0].approved is True
