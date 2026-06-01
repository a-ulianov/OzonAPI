import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    SupplyOrderContentUpdateValidationRequest,
    SupplyOrderContentUpdateValidationResponse,
)


class TestSupplyOrderContentUpdateValidation:
    """Тесты для метода supply_order_content_update_validation."""

    @pytest.mark.asyncio
    async def test_supply_order_content_update_validation(self, api, mock_api_request):
        """Тестирует метод supply_order_content_update_validation."""

        mock_api_request.return_value = {
            "editing_errors": [],
            "validated_assortment": {
                "approved_items": [
                    {"sku": 10, "quantity": 2, "name": "Товар", "barcode": "bc"}
                ],
                "rejected_items": [
                    {
                        "sku": 11,
                        "quantity": 1,
                        "rejection_reason": ["NO_SALES"],
                        "restrictions": {
                            "reasons_restrictions": ["LIMIT"],
                            "sku_quantity_limit": 0,
                        },
                    }
                ],
                "total_approved_item_count": 1,
                "total_rejected_item_count": 1,
            },
        }

        request = SupplyOrderContentUpdateValidationRequest(
            new_bundle_id="b1", supply_id=2
        )

        response = await api.supply_order_content_update_validation(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update/validation",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, SupplyOrderContentUpdateValidationResponse)
        assert response.validated_assortment.approved_items[0].sku == 10
        assert response.validated_assortment.rejected_items[0].rejection_reason == [
            "NO_SALES"
        ]
