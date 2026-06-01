from ...core import APIManager
from ...schemas.fbp import FbpDraftGetRequest, FbpDraftGetResponse


class FbpDraftGetMixin(APIManager):
    """Реализует метод /v1/fbp/draft/get"""

    async def fbp_draft_get(
            self: "FbpDraftGetMixin",
            request: FbpDraftGetRequest,
    ) -> FbpDraftGetResponse:
        """Метод для получения информации о черновике поставки FBP.

        Notes:
            • Возвращает подробную информацию о черновике: статус, состояние отмены,
              детали доставки и признаки доступных действий.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftGet

        Args:
            request: Идентификатор поставки по схеме `FbpDraftGetRequest`

        Returns:
            Информация о черновике по схеме `FbpDraftGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_get(
                    FbpDraftGetRequest(supply_id="123456")
                )

            status = result.status
            supply_type = result.delivery_details.supply_type if result.delivery_details else None
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/get",
            payload=request.model_dump(),
        )
        return FbpDraftGetResponse(**response)
