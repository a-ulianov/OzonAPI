import pytest

from src.ozonapi.seller.schemas.actions import (
    ActionsCandidatesRequest,
    ActionsCandidatesResponse,
)


class TestActionsCandidates:
    """Тесты для метода actions_candidates."""

    @pytest.mark.asyncio
    async def test_actions_candidates(self, api, mock_api_request):
        """Тестирует метод actions_candidates."""
        mock_api_request.return_value = {
            "result": {
                "products": [
                    {
                        "id": 313455276,
                        "price": 1000.0,
                        "action_price": 900.0,
                        "max_action_price": 950.0,
                        "stock": 5,
                        "sku": 635548518,
                    }
                ],
                "total": 1,
            }
        }

        request = ActionsCandidatesRequest(action_id=123456, limit=100)
        response = await api.actions_candidates(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="actions/candidates",
            payload=request.model_dump(),
        )
        assert isinstance(response, ActionsCandidatesResponse)
        assert response.result.total == 1
        assert response.result.products[0].id == 313455276
        assert response.result.products[0].action_price == 900.0
