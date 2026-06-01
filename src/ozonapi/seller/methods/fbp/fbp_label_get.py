from ...core import APIManager
from ...schemas.fbp import FbpLabelGetRequest, FbpLabelGetResponse


class FbpLabelGetMixin(APIManager):
    """Реализует метод /v1/fbp/label/get"""

    async def fbp_label_get(
            self: "FbpLabelGetMixin",
            request: FbpLabelGetRequest,
    ) -> FbpLabelGetResponse:
        """Получает статус задания на генерацию этикеток.

        Notes:
            • При статусе `FINISHED` в `label_url` приходит ссылка на готовые этикетки.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpGetLabel

        Args:
            request: Идентификатор поставки и код задания по схеме `FbpLabelGetRequest`

        Returns:
            Статус задания на генерацию этикеток по схеме `FbpLabelGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_label_get(
                    FbpLabelGetRequest(supply_id="70", code="code-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/label/get",
            payload=request.model_dump(),
        )
        return FbpLabelGetResponse(**response)
