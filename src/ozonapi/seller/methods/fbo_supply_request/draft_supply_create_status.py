from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftSupplyCreateStatusRequest,
    DraftSupplyCreateStatusResponse,
)


class DraftSupplyCreateStatusMixin(APIManager):
    """Реализует метод /v2/draft/supply/create/status"""

    async def draft_supply_create_status(
            self: "DraftSupplyCreateStatusMixin",
            request: DraftSupplyCreateStatusRequest
    ) -> DraftSupplyCreateStatusResponse:
        """Возвращает статус создания заявки на поставку по черновику.

        Notes:
            • При успехе возвращает `order_id` созданной заявки; при ошибке — `error_reasons`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftSupplyCreateStatusV2

        Args:
            request: Запрос статуса по схеме `DraftSupplyCreateStatusRequest`

        Returns:
            Статус создания заявки по схеме `DraftSupplyCreateStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_supply_create_status(
                    DraftSupplyCreateStatusRequest(draft_id=123456)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="draft/supply/create/status",
            payload=request.model_dump(by_alias=True)
        )
        return DraftSupplyCreateStatusResponse(**response)
