from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftCreateInfoV1Request,
    DraftCreateInfoV1Response,
)


class DraftCreateInfoV1Mixin(APIManager):
    """Реализует метод /v1/draft/create/info"""

    async def draft_create_info_v1(
            self: "DraftCreateInfoV1Mixin",
            request: DraftCreateInfoV1Request
    ) -> DraftCreateInfoV1Response:
        """Возвращает информацию о черновике заявки на поставку по `operation_id` (версия 1).

        Notes:
            • ⚠️ Устаревший метод: Ozon удалил `/v1/draft/create/info` из спецификации
              Seller API (зафиксировано 2026-06-19). Метод оставлен для обратной
              совместимости. Перейдите на каноническую `draft_create_info()` (v2, по `draft_id`).
            • Принимает `operation_id` из `draft_create()`. Предпочтительна версия
              `draft_create_info()` (v2, по `draft_id`).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftCreateInfo

        Args:
            request: Запрос информации о черновике по схеме `DraftCreateInfoV1Request`

        Returns:
            Информация о черновике по схеме `DraftCreateInfoV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_create_info_v1(
                    DraftCreateInfoV1Request(operation_id="abc-123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/create/info",
            payload=request.model_dump(by_alias=True)
        )
        return DraftCreateInfoV1Response(**response)
