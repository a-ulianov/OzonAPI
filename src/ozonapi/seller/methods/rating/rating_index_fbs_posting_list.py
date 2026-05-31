from ...core import APIManager
from ...schemas.rating import (
    RatingIndexFBSPostingListRequest,
    RatingIndexFBSPostingListResponse,
)


class RatingIndexFBSPostingListMixin(APIManager):
    """Реализует метод /v1/rating/index/fbs/posting/list"""

    async def rating_index_fbs_posting_list(
            self: "RatingIndexFBSPostingListMixin",
            request: RatingIndexFBSPostingListRequest
    ) -> RatingIndexFBSPostingListResponse:
        """Возвращает список отправлений, повлиявших на индекс ошибок FBS и rFBS.

        Notes:
            • Курсорная пагинация (`cursor` + `has_next`); фильтр по периоду и номерам
              отправлений. По каждому отправлению — тип ошибки, индекс и стоимость обработки.

        References:
            https://docs.ozon.ru/api/seller/#operation/RatingAPI_ListFBSRatingIndexPostingsV1

        Args:
            request: Запрос списка отправлений по схеме `RatingIndexFBSPostingListRequest`

        Returns:
            Список отправлений по схеме `RatingIndexFBSPostingListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.rating_index_fbs_posting_list(
                    RatingIndexFBSPostingListRequest(
                        filter=RatingIndexFBSPostingListFilter(
                            date_from="2026-04-01", date_to="2026-04-30"
                        ),
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="rating/index/fbs/posting/list",
            payload=request.model_dump(by_alias=True)
        )
        return RatingIndexFBSPostingListResponse(**response)
