from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffProvinceListRequest,
    FbpDraftDropOffProvinceListResponse,
)


class FbpDraftDropOffProvinceListMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/province/list"""

    async def fbp_draft_drop_off_province_list(
            self: "FbpDraftDropOffProvinceListMixin",
            request: FbpDraftDropOffProvinceListRequest,
    ) -> FbpDraftDropOffProvinceListResponse:
        """Получает список провинций для drop-off поставки.

        Notes:
            • Возвращает провинции склада с количеством drop-off пунктов в каждой.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffProvinceList

        Args:
            request: Идентификатор склада по схеме `FbpDraftDropOffProvinceListRequest`

        Returns:
            Список провинций по схеме `FbpDraftDropOffProvinceListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_province_list(
                    FbpDraftDropOffProvinceListRequest(warehouse_id=123)
                )

            for province in result.provinces:
                print(province.name, province.points_count)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/province/list",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffProvinceListResponse(**response)
