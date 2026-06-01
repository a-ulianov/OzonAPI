from ...core import APIManager
from ...schemas.products import (
    ProductPricesDetailsRequest,
    ProductPricesDetailsResponse,
)


class ProductPricesDetailsMixin(APIManager):
    """Реализует метод /v1/product/prices/details"""

    async def product_prices_details(
            self: "ProductPricesDetailsMixin",
            request: ProductPricesDetailsRequest,
    ) -> ProductPricesDetailsResponse:
        """Получает подробную информацию о ценах товаров (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Возвращает цену, цену для покупателя, процент скидки и ценовые индексы
              (по ценам конкурентов на других площадках и по ценам этого товара на Ozon).
            • Денежные значения возвращаются строками с указанием валюты.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductPricesDetails

        Args:
            request: Список SKU по схеме `ProductPricesDetailsRequest`

        Returns:
            Подробная информация о ценах по схеме `ProductPricesDetailsResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_prices_details(
                    ProductPricesDetailsRequest(skus=["1234567890"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/prices/details",
            payload=request.model_dump(),
        )
        return ProductPricesDetailsResponse(**response)
