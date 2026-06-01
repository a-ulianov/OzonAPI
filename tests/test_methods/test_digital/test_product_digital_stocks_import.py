import pytest

from src.ozonapi.seller.schemas.digital import (
    ProductDigitalStocksImportRequest,
    ProductDigitalStocksImportResponse,
)


class TestProductDigitalStocksImport:
    """Тесты для метода product_digital_stocks_import."""

    @pytest.mark.asyncio
    async def test_product_digital_stocks_import(self, api, mock_api_request):
        """Тестирует метод product_digital_stocks_import."""

        mock_api_request.return_value = {
            "status": [
                {
                    "offer_id": "DIGITAL-1",
                    "product_id": 777,
                    "sku": 123456,
                    "updated": True,
                    "errors": [],
                }
            ]
        }

        request = ProductDigitalStocksImportRequest(
            stocks=[{"offer_id": "DIGITAL-1", "stock": 100}]
        )

        response = await api.product_digital_stocks_import(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/digital/stocks/import",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductDigitalStocksImportResponse)
        assert response.status[0].offer_id == "DIGITAL-1"
        assert response.status[0].updated is True
