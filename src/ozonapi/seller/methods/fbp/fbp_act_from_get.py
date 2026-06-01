from ...core import APIManager
from ...schemas.fbp import FbpActFromGetRequest, FbpActFromGetResponse


class FbpActFromGetMixin(APIManager):
    """Реализует метод /v1/fbp/act-from/get"""

    async def fbp_act_from_get(
            self: "FbpActFromGetMixin",
            request: FbpActFromGetRequest,
    ) -> FbpActFromGetResponse:
        """Получает статус генерации акта приёмки.

        Notes:
            • При статусе `EXIST` в `cdn_url` приходит ссылка на готовый акт.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpCheckActState

        Args:
            request: Идентификатор файла акта по схеме `FbpActFromGetRequest`

        Returns:
            Статус генерации акта по схеме `FbpActFromGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_act_from_get(
                    FbpActFromGetRequest(file_uuid="uuid-act")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/act-from/get",
            payload=request.model_dump(),
        )
        return FbpActFromGetResponse(**response)
