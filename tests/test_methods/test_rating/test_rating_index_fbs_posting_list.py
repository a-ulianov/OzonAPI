import pytest

from src.ozonapi.seller.schemas.rating import (
    RatingIndexFBSPostingListFilter,
    RatingIndexFBSPostingListRequest,
    RatingIndexFBSPostingListResponse,
)


class TestRatingIndexFBSPostingList:
    """Тесты для метода rating_index_fbs_posting_list."""

    @pytest.mark.asyncio
    async def test_rating_index_fbs_posting_list(self, api, mock_api_request):
        """Тестирует метод rating_index_fbs_posting_list."""

        mock_api_request.return_value = {
            "cursor": "next-cursor",
            "errors": [
                {
                    "charge_percent": 10.0,
                    "charge_price": 50.0,
                    "charge_price_currency_code": "RUB",
                    "delivery_schema": "FBS",
                    "error_at": "2026-04-15",
                    "has_grace_status": False,
                    "index": 2.0,
                    "posting_error_type": "LATE_SHIPMENT",
                    "posting_number": "0001-1",
                    "product_price": 500.0,
                    "product_price_currency_code": "RUB",
                }
            ],
            "has_next": True,
        }

        request = RatingIndexFBSPostingListRequest(
            filter=RatingIndexFBSPostingListFilter(
                date_from="2026-04-01", date_to="2026-04-30"
            ),
            limit=100,
        )

        response = await api.rating_index_fbs_posting_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="rating/index/fbs/posting/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, RatingIndexFBSPostingListResponse)
        assert response.errors[0].posting_number == "0001-1"
        assert response.errors[0].posting_error_type == "LATE_SHIPMENT"
        assert response.has_next is True
