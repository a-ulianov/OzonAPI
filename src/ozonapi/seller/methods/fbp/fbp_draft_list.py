from ...core import APIManager
from ...schemas.fbp import FbpDraftListRequest, FbpDraftListResponse


class FbpDraftListMixin(APIManager):
    """Реализует метод /v1/fbp/draft/list"""

    async def fbp_draft_list(
            self: "FbpDraftListMixin",
            request: FbpDraftListRequest,
    ) -> FbpDraftListResponse:
        """Метод для получения списка черновиков поставки FBP.

        Notes:
            • Возвращает список черновиков с постраничной выборкой по `last_id`.
            • Признак `has_next` указывает на наличие следующей страницы.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftList

        Args:
            request: Параметры выборки по схеме `FbpDraftListRequest`

        Returns:
            Список черновиков по схеме `FbpDraftListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_list(
                    FbpDraftListRequest(count=50)
                )

            for item in result.items:
                print(item.id, item.supply_id, item.status)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/list",
            payload=request.model_dump(),
        )
        return FbpDraftListResponse(**response)
