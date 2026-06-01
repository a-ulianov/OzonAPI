import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsListRequest,
    SellerActionsListResponse,
)


class TestSellerActionsList:
    """Тесты для метода seller_actions_list."""

    @pytest.mark.asyncio
    async def test_seller_actions_list(self, api, mock_api_request):
        """Тестирует метод seller_actions_list."""

        mock_api_request.return_value = {
            "actions": [
                {
                    "action_id": 123456,
                    "sku_count": 5,
                    "is_participated": True,
                    "is_turn_on": True,
                    "is_editable": True,
                    "allow_delete": False,
                    "highlight_url": "https://seller.ozon.ru/app/promo/123456",
                    "action_parameters": {
                        "title": "Летняя распродажа",
                        "type": "DISCOUNT",
                        "status": "ACTIVE",
                        "date_start": "2026-07-01T00:00:00Z",
                        "date_end": "2026-07-31T23:59:59Z",
                        "min_action_percent": 10.0,
                        "discount_levels": [
                            {"order_amount": 3000.0, "discount_value": 5.0}
                        ],
                        "picked_segments": [
                            {"segments": [{"id": 1, "name": "VIP", "type": "SELLER"}]}
                        ],
                        "voucher_parameters": {
                            "count_codes": 100,
                            "is_private": True,
                            "type": "UNIQUE",
                        },
                    },
                }
            ],
            "total": 1,
        }

        request = SellerActionsListRequest(status=["ACTIVE"], limit=50)

        response = await api.seller_actions_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/list",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsListResponse)
        assert response.total == 1
        action = response.actions[0]
        assert action.action_id == 123456
        assert action.action_parameters.title == "Летняя распродажа"
        assert action.action_parameters.discount_levels[0].order_amount == 3000.0
        assert action.action_parameters.picked_segments[0].segments[0].name == "VIP"
        assert action.action_parameters.voucher_parameters.type == "UNIQUE"
