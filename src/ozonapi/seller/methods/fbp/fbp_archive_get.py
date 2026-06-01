from ...core import APIManager
from ...schemas.fbp import FbpArchiveGetRequest, FbpArchiveGetResponse


class FbpArchiveGetMixin(APIManager):
    """Реализует метод /v1/fbp/archive/get"""

    async def fbp_archive_get(
            self: "FbpArchiveGetMixin",
            request: FbpArchiveGetRequest,
    ) -> FbpArchiveGetResponse:
        """Получает информацию о завершённой поставке.

        Notes:
            • Возвращает статус, сводку по товарам, причину отклонения и детали доставки.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpArchiveGet

        Args:
            request: Идентификатор поставки по схеме `FbpArchiveGetRequest`

        Returns:
            Информация о завершённой поставке по схеме `FbpArchiveGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_archive_get(
                    FbpArchiveGetRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/archive/get",
            payload=request.model_dump(),
        )
        return FbpArchiveGetResponse(**response)
