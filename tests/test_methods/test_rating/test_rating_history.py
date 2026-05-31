import pytest

from src.ozonapi.seller.schemas.rating import (
    RatingHistoryRequest,
    RatingHistoryResponse,
)


class TestRatingHistory:
    """Тесты для метода rating_history."""

    @pytest.mark.asyncio
    async def test_rating_history(self, api, mock_api_request):
        """Тестирует метод rating_history."""

        mock_api_request.return_value = {
            "premium_scores": [
                {
                    "rating": "rating_on_time",
                    "scores": [
                        {"date": "2026-04-10", "rating_value": 90.0, "value": 5}
                    ],
                }
            ],
            "ratings": [
                {
                    "danger_threshold": 80.0,
                    "premium_threshold": 98.0,
                    "rating": "rating_on_time",
                    "values": [
                        {
                            "date_from": "2026-04-01",
                            "date_to": "2026-04-30",
                            "status": {"danger": False, "premium": True, "warning": False},
                            "value": 99.0,
                        }
                    ],
                    "warning_threshold": 90.0,
                }
            ],
        }

        request = RatingHistoryRequest(
            date_from="2026-04-01T00:00:00Z",
            date_to="2026-04-30T23:59:59Z",
            ratings=["rating_on_time"],
            with_premium_scores=True,
        )

        response = await api.rating_history(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="rating/history",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, RatingHistoryResponse)
        assert response.ratings[0].values[0].value == 99.0
        assert response.ratings[0].values[0].status.premium is True
        assert response.premium_scores[0].scores[0].value == 5
