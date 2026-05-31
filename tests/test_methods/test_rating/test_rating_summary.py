import pytest

from src.ozonapi.seller.schemas.rating import RatingSummaryResponse


class TestRatingSummary:
    """Тесты для метода rating_summary."""

    @pytest.mark.asyncio
    async def test_rating_summary(self, api, mock_api_request):
        """Тестирует метод rating_summary."""

        mock_api_request.return_value = {
            "groups": [
                {
                    "group_name": "Качество",
                    "items": [
                        {
                            "change": {"direction": "DIRECTION_RISE", "meaning": "MEANING_GOOD"},
                            "current_value": 4.8,
                            "name": "Оценка товаров",
                            "past_value": 4.7,
                            "rating": "rating_review_avg_score_total",
                            "rating_direction": "HIGHER_IS_BETTER",
                            "status": "OK",
                            "value_type": "SCORE",
                        }
                    ],
                }
            ],
            "localization_index": {
                "calculation_date": "2026-04-01", "localization_percentage": 75
            },
            "penalty_score_exceeded": False,
            "premium": True,
            "premium_plus": False,
        }

        response = await api.rating_summary()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="rating/summary",
            payload={},
        )

        assert isinstance(response, RatingSummaryResponse)
        assert response.groups[0].items[0].current_value == 4.8
        assert response.groups[0].items[0].change.direction == "DIRECTION_RISE"
        assert response.premium is True
        assert response.localization_index.localization_percentage == 75
