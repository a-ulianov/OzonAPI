import pytest

from src.ozonapi.seller.schemas.receipts import (
    ReceiptsGetRequest,
    ReceiptsGetResponse,
)


class TestReceiptsGet:
    """Тесты для метода receipts_get."""

    @pytest.mark.asyncio
    async def test_receipts_get(self, api, mock_api_request):
        """Тестирует метод receipts_get."""

        mock_api_request.return_value = {"content": "JVBERi0xLjQK"}

        request = ReceiptsGetRequest(receipt_id="123")

        response = await api.receipts_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="receipts/get",
            payload=request.model_dump()
        )

        assert isinstance(response, ReceiptsGetResponse)
        assert response.content == "JVBERi0xLjQK"
