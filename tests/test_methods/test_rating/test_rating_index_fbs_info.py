import pytest

from src.ozonapi.seller.schemas.rating import RatingIndexFBSInfoResponse


class TestRatingIndexFBSInfo:
    """Тесты для метода rating_index_fbs_info."""

    @pytest.mark.asyncio
    async def test_rating_index_fbs_info(self, api, mock_api_request):
        """Тестирует метод rating_index_fbs_info."""

        mock_api_request.return_value = {
            "currency_code": "RUB",
            "defects": [
                {
                    "date": "2026-04-10",
                    "index_by_date": 1.5,
                    "processing_costs_sum_by_date": 120.0,
                }
            ],
            "index": 1.2,
            "period_from": "2026-04-01",
            "period_to": "2026-04-30",
            "processing_costs_sum": 500.0,
        }

        response = await api.rating_index_fbs_info()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="rating/index/fbs/info",
            payload={},
        )

        assert isinstance(response, RatingIndexFBSInfoResponse)
        assert response.index == 1.2
        assert response.defects[0].index_by_date == 1.5
        assert response.currency_code == "RUB"
