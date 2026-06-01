from ...core import APIManager
from ...schemas.fbp import FbpActToGetRequest, FbpActToGetResponse


class FbpActToGetMixin(APIManager):
    """Реализует метод /v1/fbp/act-to/get"""

    async def fbp_act_to_get(
            self: "FbpActToGetMixin",
            request: FbpActToGetRequest,
    ) -> FbpActToGetResponse:
        """Получает статус генерации транспортной накладной.

        Notes:
            • При статусе `FINISHED` в `label_url` приходит ссылка на готовую накладную.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpCheckConsignmentNoteState

        Args:
            request: Идентификатор поставки и код задания по схеме `FbpActToGetRequest`

        Returns:
            Статус генерации накладной по схеме `FbpActToGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_act_to_get(
                    FbpActToGetRequest(supply_id="70", code="code-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/act-to/get",
            payload=request.model_dump(),
        )
        return FbpActToGetResponse(**response)
