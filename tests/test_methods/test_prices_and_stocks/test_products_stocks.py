import pytest


class TestProductsStocks:
    """Тесты для метода products_stocks."""

    @pytest.mark.asyncio
    async def test_products_stocks(self, api, mock_api_request):
        """Тестирует метод products_stocks."""
        mock_response_data = {
            "result": [
                {
                    "warehouse_id": 22142605386000,
                    "product_id": 313455276,
                    "offer_id": "PH11042",
                    "updated": True,
                    "errors": []
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        # Должен пройти валидацию
        from src.ozonapi.seller.schemas.prices_and_stocks.v2__products_stocks import (
            ProductsStocksRequest, ProductsStocksItem
        )

        request = ProductsStocksRequest(
            stocks=[
                ProductsStocksItem(
                    offer_id="PH11042",
                    product_id=313455276,
                    stock=100,
                    warehouse_id=22142605386000
                )
            ]
        )

        # Вызываем метод
        response = await api.products_stocks(request)

        # Проверяем вызов API
        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="products/stocks",
            payload=request.model_dump()
        )

        # Проверяем ответ
        from src.ozonapi.seller.schemas.prices_and_stocks.v2__products_stocks import ProductsStocksResponse
        assert isinstance(response, ProductsStocksResponse)
        assert len(response.result) == 1
        assert response.result[0].warehouse_id == 22142605386000
        assert response.result[0].product_id == 313455276
        assert response.result[0].offer_id == "PH11042"
        assert response.result[0].updated is True
        assert response.result[0].errors == []

        # Тесты валидаторов
        # Тест на обязательность хотя бы одного идентификатора
        with pytest.raises(ValueError, match="Должен быть указан хотя бы один из параметров: offer_id или product_id"):
            ProductsStocksItem(stock=100, warehouse_id=22142605386000)

        # Тест на валидацию с только offer_id
        item_only_offer = ProductsStocksItem(offer_id="TEST", stock=50, warehouse_id=22142605386000)
        assert item_only_offer.offer_id == "TEST"
        assert item_only_offer.product_id is None

        # Тест на валидацию с только product_id
        item_only_product = ProductsStocksItem(product_id=123456, stock=50, warehouse_id=22142605386000)
        assert item_only_product.product_id == 123456
        assert item_only_product.offer_id is None

        # Тест на валидацию с обоими идентификаторами
        item_both = ProductsStocksItem(offer_id="TEST", product_id=123456, stock=50, warehouse_id=22142605386000)
        assert item_both.offer_id == "TEST"
        assert item_both.product_id == 123456