import pytest

from src.ozonapi.seller.common.enumerations.fbo import ItemSortField
from src.ozonapi.seller.schemas.fbo import (
    SupplyOrderBundleItemTagsCalculation,
    SupplyOrderBundleRequest,
    SupplyOrderBundleResponse,
)


class TestSupplyOrderBundle:
    """Тесты для метода supply_order_bundle."""

    @pytest.mark.asyncio
    async def test_supply_order_bundle(self, api, mock_api_request):
        """Тестирует метод supply_order_bundle."""

        mock_response_data = {
            "items": [
                {
                    "sku": 987654321,
                    "name": "Тестовый товар",
                    "offer_id": "TEST-001",
                    "quantity": 10,
                    "barcode": "4600000000001",
                    "product_id": 123456789,
                    "quant": 1,
                    "is_quant_editable": True,
                    "volume_in_litres": 0.5,
                    "total_volume_in_litres": 5.0,
                    "sfbo_attribute": "ITEM_SFBO_ATTRIBUTE_NONE",
                    "shipment_type": "BUNDLE_ITEM_SHIPMENT_TYPE_GENERAL",
                    "tags": ["ECONOM"],
                    "placement_zone": "PRODUCTS",
                }
            ],
            "total_count": 1,
            "has_next": False,
            "last_id": "last-123",
        }
        mock_api_request.return_value = mock_response_data

        request = SupplyOrderBundleRequest(
            bundle_ids=["1234567890"],
            limit=100,
            is_asc=True,
            item_tags_calculation=SupplyOrderBundleItemTagsCalculation(
                dropoff_warehouse_id="111",
                storage_warehouse_ids=["222", "333"],
            ),
            sort_field=ItemSortField.SKU,
        )

        response = await api.supply_order_bundle(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="supply-order/bundle",
            payload=request.model_dump(by_alias=True),
        )

        assert isinstance(response, SupplyOrderBundleResponse)
        assert response.total_count == 1
        assert response.has_next is False
        assert len(response.items) == 1
        assert response.items[0].sku == 987654321
        assert response.items[0].offer_id == "TEST-001"
        assert response.items[0].tags == ["ECONOM"]
