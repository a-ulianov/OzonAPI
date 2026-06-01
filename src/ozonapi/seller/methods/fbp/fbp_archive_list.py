from ...core import APIManager
from ...schemas.fbp import FbpArchiveListRequest, FbpArchiveListResponse


class FbpArchiveListMixin(APIManager):
    """Реализует метод /v1/fbp/archive/list"""

    async def fbp_archive_list(
            self: "FbpArchiveListMixin",
            request: FbpArchiveListRequest,
    ) -> FbpArchiveListResponse:
        """Получает список завершённых поставок.

        Notes:
            • Параметры `count`/`last_id` передаются строками (так требует API).
            • Признак `has_next` указывает на наличие следующей страницы.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpArchiveList

        Args:
            request: Параметры выборки по схеме `FbpArchiveListRequest`

        Returns:
            Список завершённых поставок по схеме `FbpArchiveListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_archive_list(
                    FbpArchiveListRequest(count="50")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/archive/list",
            payload=request.model_dump(),
        )
        return FbpArchiveListResponse(**response)
