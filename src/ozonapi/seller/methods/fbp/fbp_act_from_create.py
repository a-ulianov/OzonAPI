from ...core import APIManager
from ...schemas.fbp import FbpActFromCreateRequest, FbpActFromCreateResponse


class FbpActFromCreateMixin(APIManager):
    """Реализует метод /v1/fbp/act-from/create"""

    async def fbp_act_from_create(
            self: "FbpActFromCreateMixin",
            request: FbpActFromCreateRequest,
    ) -> FbpActFromCreateResponse:
        """Генерирует акт приёмки.

        Notes:
            • Запускает генерацию акта; статус и ссылку получайте методом
              `fbp_act_from_get()` по `file_uuid`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpCreateAct

        Args:
            request: Идентификатор поставки по схеме `FbpActFromCreateRequest`

        Returns:
            Идентификатор файла акта по схеме `FbpActFromCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_act_from_create(
                    FbpActFromCreateRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/act-from/create",
            payload=request.model_dump(),
        )
        return FbpActFromCreateResponse(**response)
