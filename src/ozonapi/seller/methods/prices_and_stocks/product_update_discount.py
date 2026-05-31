from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductUpdateDiscountRequest,
    ProductUpdateDiscountResponse,
)


class ProductUpdateDiscountMixin(APIManager):
    """Реализует метод /v1/product/update/discount"""

    async def product_update_discount(
            self: "ProductUpdateDiscountMixin",
            request: ProductUpdateDiscountRequest,
    ) -> ProductUpdateDiscountResponse:
        """Устанавливает скидку на уценённый товар.

        Notes:
            • Метод применяется только к уценённым товарам.
            • Размер скидки указывается в процентах и должен быть в диапазоне от 3 до 99.
            • Информацию об уценённых товарах можно получить методом `product_info_discounted()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductUpdateDiscount

        Args:
            request: Идентификатор товара и размер скидки по схеме `ProductUpdateDiscountRequest`

        Returns:
            Результат установки скидки по схеме `ProductUpdateDiscountResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_update_discount(
                    ProductUpdateDiscountRequest(
                        product_id=313455276,
                        discount=20
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/update/discount",
            payload=request.model_dump(),
        )
        return ProductUpdateDiscountResponse(**response)
