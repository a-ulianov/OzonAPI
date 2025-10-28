from ...core import APIManager
from ...schemas.products import ProductUpdateOfferIdRequest, ProductUpdateOfferIdResponse


class ProductUpdateOfferIdMixin(APIManager):
    """Реализует метод /v1/product/update/offer-id"""

    async def product_update_offer_id(
        self: "ProductUpdateOfferIdMixin",
        request: ProductUpdateOfferIdRequest
    ) -> ProductUpdateOfferIdResponse:
        """Изменяет артикулы товаров в системе продавца.

        Notes:
            • Метод позволяет изменить несколько `offer_id` в одном запросе.
            • Рекомендуется передавать до `250` пар артикулов в одном запросе.
            • Длина нового артикула не должна превышать `50` символов.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductUpdateOfferID

        Args:
            request: Список пар текущий/новый артикул для изменения по схеме `ProductUpdateOfferIdRequest`.

        Returns:
            Информация об ошибках изменения артикулов по схеме `ProductUpdateOfferIdResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_update_offer_id(
                    ProductUpdateOfferIdRequest(
                        update_offer_id=[
                            ProductUpdateOfferIdRequestItem(
                                offer_id="old-article-123",
                                new_offer_id="new-article-456"
                            ),
                            ProductUpdateOfferIdRequestItem(
                                offer_id="old-article-789",
                                new_offer_id="new-article-012"
                            ),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/update/offer-id",
            payload=request.model_dump(),
        )
        return ProductUpdateOfferIdResponse(**response)
