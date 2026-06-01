from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffPointListRequest,
    FbpDraftDropOffPointListResponse,
)


class FbpDraftDropOffPointListMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/point/list"""

    async def fbp_draft_drop_off_point_list(
            self: "FbpDraftDropOffPointListMixin",
            request: FbpDraftDropOffPointListRequest,
    ) -> FbpDraftDropOffPointListResponse:
        """Получает список drop-off пунктов в провинции.

        Notes:
            • Поддерживает постраничную выборку через `next_page_number`/`page_size`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffPointList

        Args:
            request: Параметры выборки по схеме `FbpDraftDropOffPointListRequest`

        Returns:
            Список drop-off пунктов по схеме `FbpDraftDropOffPointListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_point_list(
                    FbpDraftDropOffPointListRequest(
                        warehouse_id=123,
                        province_uuid="uuid-1",
                        page_size=50,
                    )
                )

            for point in result.drop_off_points:
                print(point.drop_off_point_id, point.point_address)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/point/list",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffPointListResponse(**response)
