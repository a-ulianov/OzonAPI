from ...core import APIManager
from ...schemas.quants import (
    ProductQuantInfoRequest,
    ProductQuantInfoResponse,
)


class ProductQuantInfoMixin(APIManager):
    """Реализует метод /v1/product/quant/info"""

    async def product_quant_info(
            self: "ProductQuantInfoMixin",
            request: ProductQuantInfoRequest
    ) -> ProductQuantInfoResponse:
        """Возвращает информацию об эконом-товарах по идентификаторам квантов.

        Notes:
            • За один запрос можно запросить от 1 до 1000 квантов (`quant_code`).
            • Размер кванта приходит в поле `quant_sice` (опечатка в API Ozon) и
              доступен через атрибут `quant_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/QuantGetInfo

        Args:
            request: Запрос информации об эконом-товарах по схеме `ProductQuantInfoRequest`

        Returns:
            Информация об эконом-товарах по схеме `ProductQuantInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_quant_info(
                    ProductQuantInfoRequest(quant_code=["123456"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/quant/info",
            payload=request.model_dump()
        )
        return ProductQuantInfoResponse(**response)
