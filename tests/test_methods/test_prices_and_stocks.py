import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.common.enumerations.prices import PricingStrategy, VAT
from src.ozonapi.seller.methods import SellerPricesAndStocksAPI
from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoPricesRequest,
    ProductInfoPricesResponse,
    ProductInfoStocksRequest,
    ProductInfoStocksResponse,
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
)


class TestSellerPricesAndStocksAPI:
    """Тесты для класса SellerPricesAndStocksAPI."""

    @pytest.fixture
    def seller_prices_stocks_api(self):
        """Фикстура для создания экземпляра SellerPricesAndStocksAPI."""
        return SellerPricesAndStocksAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerPricesAndStocksAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_product_info_prices(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_prices."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoPricesRequest()
        response = await seller_prices_stocks_api.product_info_prices(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="product/info/prices",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoPricesResponse)
        assert response.cursor == "test_cursor"

    @pytest.mark.asyncio
    async def test_product_info_stocks(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_stocks."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoStocksRequest()
        response = await seller_prices_stocks_api.product_info_stocks(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/stocks",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksResponse)
        assert response.cursor == "test_cursor"

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbs."""
        mock_response_data = {
            "result": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoStocksByWarehouseFBSRequest(
            sku=[9876543210]
        )
        response = await seller_prices_stocks_api.product_info_stocks_by_warehouse_fbs(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksByWarehouseFBSResponse)
        assert response.result == []

    @pytest.mark.asyncio
    async def test_product_import_prices(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_import_prices."""
        mock_response_data = {
            "result": [
                {
                    "product_id": 1386,
                    "offer_id": "PH8865",
                    "updated": True,
                    "errors": []
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        request_data = {
            "prices": [
                {
                    "auto_action_enabled": PricingStrategy.UNKNOWN,
                    "auto_add_to_ozon_actions_list_enabled": PricingStrategy.UNKNOWN,
                    "currency_code": "RUB",
                    "min_price": "800",
                    "min_price_for_auto_actions_enabled": True,
                    "net_price": "650",
                    "offer_id": "PH8865",
                    "old_price": "0",
                    "price": "1448",
                    "price_strategy_enabled": PricingStrategy.UNKNOWN,
                    "product_id": 1386,
                    "quant_size": 1,
                    "vat": VAT.PERCENT_20
                }
            ]
        }

        # Тестируем создание схемы и валидацию
        from src.ozonapi.seller.schemas.prices_and_stocks.v1__product_import_prices import (
            ProductImportPricesRequest, ProductImportPricesItem
        )

        # Должен пройти валидацию
        request = ProductImportPricesRequest(**request_data)

        # Вызываем метод
        response = await seller_prices_stocks_api.product_import_prices(request)

        # Проверяем вызов API
        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import/prices",
            json=request.model_dump()
        )

        # Проверяем ответ
        from src.ozonapi.seller.schemas.prices_and_stocks.v1__product_import_prices import ProductImportPricesResponse
        assert isinstance(response, ProductImportPricesResponse)
        assert len(response.result) == 1
        assert response.result[0].product_id == 1386
        assert response.result[0].offer_id == "PH8865"
        assert response.result[0].updated is True
        assert response.result[0].errors == []

        # Тест на обязательность хотя бы одного идентификатора
        with pytest.raises(ValueError, match="Должен быть указан хотя бы один из параметров: offer_id или product_id"):
            ProductImportPricesItem(price="1000")

        # Тест на корректность формата цен
        with pytest.raises(ValueError, match="неправильный формат цены"):
            ProductImportPricesItem(offer_id="TEST", price="invalid_price")

        # Тесты на разницу между old_price и price
        with pytest.raises(ValueError, match="old_price должен быть больше price"):
            ProductImportPricesItem(offer_id="TEST", old_price="1000", price="1500")

        with pytest.raises(ValueError, match="не менее 20 руб"):
            ProductImportPricesItem(offer_id="TEST", old_price="310", price="300")

        with pytest.raises(ValueError, match="не менее 500 руб"):
            ProductImportPricesItem(offer_id="TEST", old_price="10490", price="10001")

        with pytest.raises(ValueError, match="не менее 5%"):
            ProductImportPricesItem(offer_id="TEST", old_price="1040", price="1000")

    @pytest.mark.asyncio
    async def test_products_stocks(self, seller_prices_stocks_api, mock_api_manager_request):
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
        mock_api_manager_request.return_value = mock_response_data

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
        response = await seller_prices_stocks_api.products_stocks(request)

        # Проверяем вызов API
        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="products/stocks",
            json=request.model_dump()
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