from ...core import APIManager
from ...schemas.fbp import FbpActToCreateRequest, FbpActToCreateResponse


class FbpActToCreateMixin(APIManager):
    """Реализует метод /v1/fbp/act-to/create"""

    async def fbp_act_to_create(
            self: "FbpActToCreateMixin",
            request: FbpActToCreateRequest,
    ) -> FbpActToCreateResponse:
        """Генерирует транспортную накладную.

        Notes:
            • Запускает генерацию накладной; статус и ссылку получайте методом
              `fbp_act_to_get()` по `code`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpCreateConsignmentNote

        Args:
            request: Идентификатор поставки по схеме `FbpActToCreateRequest`

        Returns:
            Код задания на генерацию по схеме `FbpActToCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_act_to_create(
                    FbpActToCreateRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/act-to/create",
            payload=request.model_dump(),
        )
        return FbpActToCreateResponse(**response)
