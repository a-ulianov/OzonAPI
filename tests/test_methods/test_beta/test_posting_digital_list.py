import pytest

from src.ozonapi.seller.schemas.beta import (
    PostingDigitalListRequest,
    PostingDigitalListResponse,
)


class TestPostingDigitalList:
    """Тесты для метода posting_digital_list."""

    @pytest.mark.asyncio
    async def test_posting_digital_list(self, api, mock_api_request):
        """Тестирует метод posting_digital_list."""

        mock_api_request.return_value = {
            "cursor": "next",
            "has_next": True,
            "postings": [
                {
                    "posting_number": "0001-1",
                    "order_id": 777,
                    "status": "delivered",
                    "products": [
                        {
                            "name": "Код активации",
                            "offer_id": "code-1",
                            "price": {"amount": "500.0000", "currency": "RUB"},
                            "quantity": 1,
                            "required_qty_for_digital_code": 1,
                            "sku": 999,
                        }
                    ],
                    "waiting_deadline_for_digital_code": "2026-06-02T00:00:00Z",
                }
            ],
        }

        request = PostingDigitalListRequest(
            limit=100,
            filter={"since": "2026-05-01T00:00:00Z", "to": "2026-06-01T00:00:00Z"},
            sort_dir="ASC",
            with_={"financial_data": True},
        )

        response = await api.posting_digital_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/digital/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingDigitalListResponse)
        assert response.postings[0].products[0].price.amount == "500.0000"
        assert response.postings[0].products[0].required_qty_for_digital_code == 1
        payload = request.model_dump(by_alias=True)
        assert "with" in payload
        assert "to" in payload["filter"]
