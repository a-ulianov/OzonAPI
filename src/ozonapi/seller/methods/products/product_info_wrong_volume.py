from ...core import APIManager
from ...schemas.products import (
    ProductInfoWrongVolumeRequest,
    ProductInfoWrongVolumeResponse,
)


class ProductInfoWrongVolumeMixin(APIManager):
    """Реализует метод /v1/product/info/wrong-volume"""

    async def product_info_wrong_volume(
            self: "ProductInfoWrongVolumeMixin",
            request: ProductInfoWrongVolumeRequest = ProductInfoWrongVolumeRequest(),
    ) -> ProductInfoWrongVolumeResponse:
        """Метод для получения списка товаров с некорректными ОВХ.

        Notes:
            • Возвращает товары, у которых заданы некорректные объёмно-весовые
              характеристики (высота, длина, ширина, вес).
            • Использует курсорную пагинацию: передайте `cursor` из предыдущего
              ответа, чтобы получить следующую страницу.
            • Параметр `limit` ограничивает количество элементов в ответе (1–1000).

        References:
            https://docs.ozon.ru/api/seller/?#operation/ProductAPI_ProductInfoWrongVolume

        Args:
            request: Параметры пагинации по схеме `ProductInfoWrongVolumeRequest`

        Returns:
            Список товаров с некорректными ОВХ по схеме `ProductInfoWrongVolumeResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_wrong_volume(
                    ProductInfoWrongVolumeRequest(limit=100)
                )

            for product in result.products:
                print(product.offer_id, product.weight)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/wrong-volume",
            payload=request.model_dump(),
        )
        return ProductInfoWrongVolumeResponse(**response)
