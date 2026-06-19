from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftCreateRequest,
    DraftCreateResponse,
)


class DraftCreateMixin(APIManager):
    """Реализует метод /v1/draft/create"""

    async def draft_create(
            self: "DraftCreateMixin",
            request: DraftCreateRequest
    ) -> DraftCreateResponse:
        """Создаёт черновик заявки на поставку FBO.

        Notes:
            • ⚠️ Устаревший метод: Ozon удалил `/v1/draft/create` из спецификации Seller API
              (зафиксировано 2026-06-19). Метод оставлен для обратной совместимости. Перейдите
              на специализированные методы создания черновика: `draft_direct_create()`
              (прямая поставка), `draft_crossdock_create()` (кросс-докинг),
              `draft_multi_cluster_create()` (мультикластерная поставка).
            • Запускает асинхронный расчёт черновика; результат — через `draft_create_info()`
              по полученному `operation_id`/`draft_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftCreate

        Args:
            request: Запрос создания черновика по схеме `DraftCreateRequest`

        Returns:
            Идентификатор операции по схеме `DraftCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_create(
                    DraftCreateRequest(
                        items=[DraftCreateItem(sku=123, quantity=10)],
                        type=SupplyCreateType.DIRECT
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftCreateResponse(**response)
