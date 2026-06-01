from ...core import APIManager
from ...schemas.passes import (
    PassListRequest,
    PassListResponse,
)


class PassListMixin(APIManager):
    """Реализует метод /v1/pass/list"""

    async def pass_list(
            self: "PassListMixin",
            request: PassListRequest
    ) -> PassListResponse:
        """Возвращает список пропусков на склады Ozon с курсорной пагинацией.

        Notes:
            • Постраничная навигация курсором: передайте `cursor` из предыдущего ответа.
            • Можно отфильтровать пропуска по складам, точкам отгрузки, цели въезда
              и активности через `filter`.
            • Поле `limit` обязательно (по умолчанию — 1000).

        References:
            https://docs.ozon.ru/api/seller/#operation/PassList

        Args:
            request: Запрос списка пропусков по схеме `PassListRequest`

        Returns:
            Список пропусков по схеме `PassListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.pass_list(
                    PassListRequest(limit=100, filter={"only_active_passes": True})
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="pass/list",
            payload=request.model_dump()
        )
        return PassListResponse(**response)
