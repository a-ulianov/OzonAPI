from ...core import APIManager
from ...schemas.products import ProductImportInfoRequest, ProductImportInfoResponse


class ProductImportInfoMixin(APIManager):
    """Реализует метод /v1/product/import/info"""

    async def product_import_info(
        self: "ProductImportInfoMixin",
        request: ProductImportInfoRequest
    ) -> ProductImportInfoResponse:
        """Получает информацию об обработке задачи загрузки или обновления товарных карточек.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_GetImportProductsInfo

        Args:
            request: Айдишник задачи по схеме `ProductImportInfoRequest`

        Returns:
            Массив с информаций об обработанных товарах и их кол-ве по схеме `ProductImportInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_import_info(
                    ProductImportInfoRequest(task_id=1234567),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import/info",
            payload=request.model_dump(),
        )
        return ProductImportInfoResponse(**response)
