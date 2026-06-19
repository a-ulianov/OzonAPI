from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftSupplyCreateV1Request,
    DraftSupplyCreateV1Response,
)


class DraftSupplyCreateV1Mixin(APIManager):
    """Реализует метод /v1/draft/supply/create"""

    async def draft_supply_create_v1(
            self: "DraftSupplyCreateV1Mixin",
            request: DraftSupplyCreateV1Request
    ) -> DraftSupplyCreateV1Response:
        """Создаёт заявку на поставку по черновику (версия 1).

        Notes:
            • ⚠️ Устаревший метод: Ozon удалил `/v1/draft/supply/create` из спецификации
              Seller API (зафиксировано 2026-06-19). Метод оставлен для обратной
              совместимости. Перейдите на каноническую `draft_supply_create()` (v2).
            • Принимает `draft_id` и `warehouse_id`. Результат — через
              `draft_supply_create_status_v1()` по `operation_id`. Предпочтительна
              версия `draft_supply_create()` (v2).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftSupplyCreate

        Args:
            request: Запрос создания заявки по схеме `DraftSupplyCreateV1Request`

        Returns:
            Идентификатор операции по схеме `DraftSupplyCreateV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_supply_create_v1(
                    DraftSupplyCreateV1Request(draft_id=123456, warehouse_id=100)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/supply/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftSupplyCreateV1Response(**response)
