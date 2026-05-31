import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutListRequest, ReturnGiveoutListResponse


class TestReturnGiveoutList:
    """Тесты для метода return_giveout_list."""

    @pytest.mark.asyncio
    async def test_return_giveout_list(self, api, mock_api_request):
        """Тестирует метод return_giveout_list."""

        mock_response_data = {
            "giveouts": [
                {
                    "giveout_id": 777,
                    "giveout_status": "GIVEOUT_STATUS_NEW",
                    "approved_articles_count": 2,
                    "total_articles_count": 3,
                    "warehouse_id": 555,
                    "warehouse_name": "Склад"
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnGiveoutListRequest(limit=100)

        response = await api.return_giveout_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnGiveoutListResponse)
        assert response.giveouts[0].giveout_id == 777
        assert response.giveouts[0].approved_articles_count == 2
