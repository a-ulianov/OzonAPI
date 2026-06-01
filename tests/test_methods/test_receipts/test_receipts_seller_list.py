import pytest

from src.ozonapi.seller.schemas.receipts import (
    ReceiptsSellerListRequest,
    ReceiptsSellerListResponse,
)


class TestReceiptsSellerList:
    """Тесты для метода receipts_seller_list."""

    @pytest.mark.asyncio
    async def test_receipts_seller_list(self, api, mock_api_request):
        """Тестирует метод receipts_seller_list."""

        mock_api_request.return_value = {
            "has_next": True,
            "receipts": [
                {
                    "created_at": "2026-06-01T00:00:00Z",
                    "operation_type": "COMMODITY",
                    "order_id": 555,
                    "parent_receipt_id": "",
                    "posting_numbers": ["0001-1"],
                    "receipt_id": "123",
                    "receipt_number": "RCPT-1",
                    "type": "INCOMING",
                    "updated_at": "2026-06-01T01:00:00Z",
                }
            ],
        }

        request = ReceiptsSellerListRequest(
            page=1, page_size=100, posting_numbers=["0001-1"]
        )

        response = await api.receipts_seller_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="receipts/seller/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReceiptsSellerListResponse)
        assert response.has_next is True
        assert response.receipts[0].receipt_id == "123"
        assert response.receipts[0].operation_type == "COMMODITY"
        assert response.receipts[0].type == "INCOMING"
