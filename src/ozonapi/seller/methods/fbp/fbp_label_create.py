from ...core import APIManager
from ...schemas.fbp import FbpLabelCreateRequest, FbpLabelCreateResponse


class FbpLabelCreateMixin(APIManager):
    """Реализует метод /v1/fbp/label/create"""

    async def fbp_label_create(
            self: "FbpLabelCreateMixin",
            request: FbpLabelCreateRequest,
    ) -> FbpLabelCreateResponse:
        """Создаёт задание на генерацию этикеток.

        Notes:
            • Запускает генерацию этикеток; статус и ссылку получайте методом
              `fbp_label_get()` по `code`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpCreateLabel

        Args:
            request: Идентификатор поставки по схеме `FbpLabelCreateRequest`

        Returns:
            Код задания на генерацию по схеме `FbpLabelCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_label_create(
                    FbpLabelCreateRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/label/create",
            payload=request.model_dump(),
        )
        return FbpLabelCreateResponse(**response)
