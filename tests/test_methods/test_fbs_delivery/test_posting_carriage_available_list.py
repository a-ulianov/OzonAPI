import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingCarriageAvailableListRequest,
    PostingCarriageAvailableListResponse,
)


class TestPostingCarriageAvailableList:
    """Тесты для метода posting_carriage_available_list."""

    @pytest.mark.asyncio
    async def test_posting_carriage_available_list(self, api, mock_api_request):
        """Тестирует метод posting_carriage_available_list."""

        mock_response_data = {
            "result": [
                {
                    "carriage_id": 12345,
                    "carriage_postings_count": 4,
                    "carriage_status": "received",
                    "delivery_method_id": 999,
                    "delivery_method_name": "Ozon Логистика",
                    "warehouse_id": 555,
                    "errors": [
                        {"code": "SOME_CODE", "status": "warning"}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingCarriageAvailableListRequest(delivery_method_id=999)

        response = await api.posting_carriage_available_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/carriage-available/list",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingCarriageAvailableListResponse)
        assert response.result[0].carriage_id == 12345
        assert response.result[0].errors[0].status == "warning"
