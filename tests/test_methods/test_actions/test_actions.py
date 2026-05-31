import pytest

from src.ozonapi.seller.schemas.actions import ActionsResponse


class TestActions:
    """Тесты для метода actions."""

    @pytest.mark.asyncio
    async def test_actions(self, api, mock_api_request):
        """Тестирует метод actions."""
        mock_api_request.return_value = {
            "result": [
                {
                    "id": 123456,
                    "title": "Распродажа",
                    "action_type": "DISCOUNT",
                    "date_start": "2024-01-01T00:00:00Z",
                    "date_end": "2024-01-31T00:00:00Z",
                    "is_participating": False,
                    "potential_products_count": 10,
                    "participating_products_count": 0,
                }
            ]
        }

        response = await api.actions()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions",
            payload={},
        )
        assert isinstance(response, ActionsResponse)
        assert response.result[0].id == 123456
        assert response.result[0].title == "Распродажа"
        assert response.result[0].is_participating is False
