import pytest

from src.ozonapi.seller.schemas.quants import (
    ProductQuantInfoRequest,
    ProductQuantInfoResponse,
)


class TestProductQuantInfo:
    """Тесты для метода product_quant_info."""

    @pytest.mark.asyncio
    async def test_product_quant_info(self, api, mock_api_request):
        """Тестирует метод product_quant_info."""

        mock_api_request.return_value = {
            "items": [
                {
                    "offer_id": "ECON-1",
                    "product_id": 777,
                    "quant_info": {
                        "quants": [
                            {
                                "quant_code": "Q-1",
                                "quant_sice": 2,
                                "sku": 123456,
                                "price": "199.00",
                                "dimensions": {"depth": 10, "height": 20, "weight": 30, "width": 40},
                                "marketing_price": {"price": "189.00", "seller_price": "199.00"},
                                "barcodes_extended": [{"barcode": "460000", "status": "OK"}],
                                "statuses": {"state_name": "Продаётся"},
                            }
                        ]
                    },
                }
            ]
        }

        request = ProductQuantInfoRequest(quant_code=["Q-1"])

        response = await api.product_quant_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/quant/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductQuantInfoResponse)
        quant = response.items[0].quant_info.quants[0]
        assert quant.quant_code == "Q-1"
        # swagger typo wire-key `quant_sice` mapped to `quant_size`
        assert quant.quant_size == 2
        assert quant.dimensions.depth == 10
        assert quant.marketing_price.price == "189.00"
        assert quant.barcodes_extended[0].barcode == "460000"
        assert quant.statuses.state_name == "Продаётся"
