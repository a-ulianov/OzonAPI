import pytest

from src.ozonapi.seller.schemas.fbs_delivery import CarriageSetPostingsRequest, CarriageSetPostingsResponse


class TestCarriageSetPostings:
    """Тесты для метода carriage_set_postings."""

    @pytest.mark.asyncio
    async def test_carriage_set_postings(self, api, mock_api_request):
        """Тестирует метод carriage_set_postings."""

        mock_response_data = {
            "result": [
                {"posting_number": "33920113-1231-1", "result": True, "error": ""}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageSetPostingsRequest(
            carriage_id=12345,
            posting_numbers=["33920113-1231-1"]
        )

        response = await api.carriage_set_postings(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/set-postings",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageSetPostingsResponse)
        assert response.result[0].posting_number == "33920113-1231-1"
        assert response.result[0].result is True
