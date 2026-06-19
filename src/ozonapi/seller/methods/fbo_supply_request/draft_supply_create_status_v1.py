from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftSupplyCreateStatusV1Request,
    DraftSupplyCreateStatusV1Response,
)


class DraftSupplyCreateStatusV1Mixin(APIManager):
    """Реализует метод /v1/draft/supply/create/status"""

    async def draft_supply_create_status_v1(
            self: "DraftSupplyCreateStatusV1Mixin",
            request: DraftSupplyCreateStatusV1Request
    ) -> DraftSupplyCreateStatusV1Response:
        """Возвращает статус создания заявки на поставку по `operation_id` (версия 1).

        Notes:
            • ⚠️ Устаревший метод: Ozon удалил `/v1/draft/supply/create/status` из
              спецификации Seller API (зафиксировано 2026-06-19). Метод оставлен для
              обратной совместимости. Перейдите на каноническую
              `draft_supply_create_status()` (v2).
            • При успехе возвращает `order_ids` созданных заявок; при ошибке —
              `error_messages`. Предпочтительна версия `draft_supply_create_status()` (v2).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftSupplyCreateStatus

        Args:
            request: Запрос статуса по схеме `DraftSupplyCreateStatusV1Request`

        Returns:
            Статус создания заявки по схеме `DraftSupplyCreateStatusV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_supply_create_status_v1(
                    DraftSupplyCreateStatusV1Request(operation_id="op-123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/supply/create/status",
            payload=request.model_dump(by_alias=True)
        )
        return DraftSupplyCreateStatusV1Response(**response)
