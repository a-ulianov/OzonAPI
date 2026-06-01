from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftCreateInfoRequest,
    DraftCreateInfoResponse,
)


class DraftCreateInfoMixin(APIManager):
    """Реализует метод /v2/draft/create/info"""

    async def draft_create_info(
            self: "DraftCreateInfoMixin",
            request: DraftCreateInfoRequest
    ) -> DraftCreateInfoResponse:
        """Возвращает информацию о черновике заявки на поставку по `draft_id`.

        Notes:
            • По каждому кластеру — склады размещения с рейтингом, статусом доступности
              и товарным составом (`bundle_id`). Ошибки расчёта — в `errors`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftCreateInfoV2

        Args:
            request: Запрос информации о черновике по схеме `DraftCreateInfoRequest`

        Returns:
            Информация о черновике по схеме `DraftCreateInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_create_info(
                    DraftCreateInfoRequest(draft_id=123456)
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="draft/create/info",
            payload=request.model_dump(by_alias=True)
        )
        return DraftCreateInfoResponse(**response)
