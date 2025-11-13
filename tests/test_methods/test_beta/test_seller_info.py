import pytest

from src.ozonapi.seller.schemas.beta import SellerInfoResponse
from src.ozonapi.seller.common.enumerations.company import TaxSystem, SubscriptionType, RatingStatus, RatingValueType


class TestSellerInfo:
    """Тесты для метода seller_info."""

    @pytest.mark.asyncio
    async def test_seller_info(self, api, mock_api_request):
        """Тестирует метод seller_info."""
        mock_response_data = {
            "company": {
                "country": "Россия",
                "currency": "RUB",
                "inn": "1234567890",
                "legal_name": "ООО 'Тестовая Компания'",
                "name": "Test Company на Ozon",
                "ogrn": "1234567890123",
                "ownership_form": "Общество с ограниченной ответственностью",
                "tax_system": "OSNO"  # Исправлено с "OSN" на "OSNO"
            },
            "ratings": [
                {
                    "current_value": {
                        "date_from": "2024-01-01T00:00:00Z",
                        "date_to": "2024-01-31T23:59:59Z",
                        "formatted": "4.8/5",
                        "status": {
                            "danger": False,
                            "premium": True,
                            "warning": False
                        },
                        "value": 4.8
                    },
                    "name": "Общий рейтинг продавца",
                    "past_value": {
                        "date_from": "2023-12-01T00:00:00Z",
                        "date_to": "2023-12-31T23:59:59Z",
                        "formatted": "4.7/5",
                        "status": {
                            "danger": False,
                            "premium": False,
                            "warning": True
                        },
                        "value": 4.7
                    },
                    "rating": "seller_rating",
                    "status": "OK",
                    "value_type": "REVIEW_SCORE"
                }
            ],
            "subscription": {
                "is_premium": True,
                "type": "PREMIUM"
            }
        }
        mock_api_request.return_value = mock_response_data

        response = await api.seller_info()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller/info",
            payload={}
        )
        assert isinstance(response, SellerInfoResponse)
        assert response.company.name == "Test Company на Ozon"
        assert response.company.inn == "1234567890"
        assert response.company.currency == "RUB"
        assert response.company.tax_system == TaxSystem.OSNO  # Исправлено на корректное значение перечисления
        assert len(response.ratings) == 1
        assert response.ratings[0].name == "Общий рейтинг продавца"
        assert response.ratings[0].current_value.value == 4.8
        assert response.ratings[0].current_value.status.premium is True
        assert response.subscription.is_premium is True
        assert response.subscription.type == SubscriptionType.PREMIUM