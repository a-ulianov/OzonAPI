from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActGetPostingsRequest,
    PostingFBSActGetPostingsResponse,
)


class PostingFBSActGetPostingsMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/get-postings"""

    async def posting_fbs_act_get_postings(
            self: "PostingFBSActGetPostingsMixin",
            request: PostingFBSActGetPostingsRequest
    ) -> PostingFBSActGetPostingsResponse:
        """Метод для получения списка отправлений в акте.

        Notes:
            • Возвращает отправления, вошедшие в акт, со списком товаров в каждом.
            • Идентификатор акта получите методом `posting_fbs_act_create()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActGetPostings

        Args:
            request: Запрос на получение отправлений в акте по схеме `PostingFBSActGetPostingsRequest`

        Returns:
            Список отправлений в акте по схеме `PostingFBSActGetPostingsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_get_postings(
                    PostingFBSActGetPostingsRequest(
                        id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-postings",
            payload=request.model_dump()
        )
        return PostingFBSActGetPostingsResponse(**response)
