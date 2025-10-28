import pytest

from src.ozonapi.seller.common.enumerations.prices import PricingStrategy, VAT


class TestProductImportPrices:
    """Тесты для метода product_import_prices."""

    @pytest.mark.asyncio
    async def test_product_import_prices(self, api, mock_api_request):
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
        mock_api_request.return_value = mock_response_data

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
        response = await api.product_import_prices(request)

        # Проверяем вызов API
        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import/prices",
            payload=request.model_dump()
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
