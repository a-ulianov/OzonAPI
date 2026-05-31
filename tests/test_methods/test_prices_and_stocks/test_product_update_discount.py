import pytest

from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductUpdateDiscountRequest,
    ProductUpdateDiscountResponse,
)


class TestProductUpdateDiscount:
    """Тесты для метода product_update_discount."""

    @pytest.mark.asyncio
    async def test_product_update_discount(self, api, mock_api_request):
        """Тестирует метод product_update_discount."""
        mock_response_data = {"result": True}
        mock_api_request.return_value = mock_response_data

        request = ProductUpdateDiscountRequest(product_id=313455276, discount=20)
        response = await api.product_update_discount(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/update/discount",
            payload=request.model_dump()
        )
        assert isinstance(response, ProductUpdateDiscountResponse)
        assert response.result is True

        # Тесты валидации размера скидки (допустимо от 3 до 99)
        with pytest.raises(ValueError):
            ProductUpdateDiscountRequest(product_id=1, discount=2)
        with pytest.raises(ValueError):
            ProductUpdateDiscountRequest(product_id=1, discount=100)
