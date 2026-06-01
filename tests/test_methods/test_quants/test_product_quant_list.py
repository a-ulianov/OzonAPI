import pytest

from src.ozonapi.seller.schemas.quants import (
    ProductQuantListRequest,
    ProductQuantListResponse,
)


class TestProductQuantList:
    """Тесты для метода product_quant_list."""

    @pytest.mark.asyncio
    async def test_product_quant_list(self, api, mock_api_request):
        """Тестирует метод product_quant_list."""

        mock_api_request.return_value = {
            "cursor": "next",
            "total_items": 5,
            "products": [
                {
                    "offer_id": "ECON-1",
                    "product_id": 777,
                    "quants": [{"quant_code": "Q-1", "quant_size": 2}],
                }
            ],
        }

        request = ProductQuantListRequest(limit=100, visibility="ALL")

        response = await api.product_quant_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/quant/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ProductQuantListResponse)
        assert response.cursor == "next"
        assert response.total_items == 5
        assert response.products[0].quants[0].quant_code == "Q-1"
        assert response.products[0].quants[0].quant_size == 2
