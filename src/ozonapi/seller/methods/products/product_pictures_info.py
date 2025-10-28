from ...core import APIManager
from ...schemas.products import ProductPicturesInfoRequest, ProductPicturesInfoResponse


class ProductPicturesInfoMixin(APIManager):
    """Реализует метод /v2/product/pictures/info"""

    async def product_pictures_info(
        self: "ProductPicturesInfoMixin",
        request: ProductPicturesInfoRequest
    ) -> ProductPicturesInfoResponse:
        """Получает информацию об изображениях товаров.

        Notes:
            • В одном запросе можно передать до `1000` идентификаторов товаров.
            • Метод возвращает ссылки на все типы изображений товара: основные фото, образцы цвета и изображения 360°.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductInfoPicturesV2

        Args:
            request: Список `product_id` для получения информации об изображениях по схеме `ProductPicturesInfoRequest`.

        Returns:
            Информация об изображениях товаров с возможными ошибками загрузки по схеме `ProductPicturesInfoResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_pictures_info(
                    ProductPicturesInfoRequest(
                        product_id=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="product/pictures/info",
            payload=request.model_dump(),
        )
        return ProductPicturesInfoResponse(**response)
