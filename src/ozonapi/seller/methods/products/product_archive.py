from ...core import APIManager
from ...schemas.products import ProductArchiveRequest, ProductArchiveResponse


class ProductArchiveMixin(APIManager):
    """Реализует метод /v1/product/archive"""

    async def product_archive(
        self: "ProductArchiveMixin",
        request: ProductArchiveRequest
    ) -> ProductArchiveResponse:
        """Перемещает товарные карточки в архив.

        Notes:
            • Вы можете передать до `100` идентификаторов за раз.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductArchive

        Args:
            request: Список `product_id` по схеме `ProductArchiveRequest`.

        Returns:
            Логическое значение выполнения операции по схеме `ProductArchiveResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_archive(
                    ProductArchiveRequest(
                        product_id=[1234567, ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/archive",
            payload=request.model_dump(),
        )
        return ProductArchiveResponse(**response)
