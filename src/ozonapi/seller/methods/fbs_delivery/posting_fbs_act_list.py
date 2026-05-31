from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActListRequest,
    PostingFBSActListResponse,
)


class PostingFBSActListMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/list"""

    async def posting_fbs_act_list(
            self: "PostingFBSActListMixin",
            request: PostingFBSActListRequest
    ) -> PostingFBSActListResponse:
        """Метод для получения списка актов по отгрузкам.

        Notes:
            • Возвращает список отгрузок с информацией о связанных документах
              (акт приёма-передачи, акт о расхождениях, акт об излишках).
            • Фильтруйте по дате создания, типу интеграции и статусам перевозок.
            • `limit` должен быть в диапазоне от 1 до 50.
            • Даты `date_from`/`date_to` передавайте в формате `yyyy-mm-dd`;
              если фильтр указан, заполняйте обе даты.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActList

        Args:
            request: Запрос на получение списка актов по схеме `PostingFBSActListRequest`

        Returns:
            Список актов по отгрузкам по схеме `PostingFBSActListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_list(
                    PostingFBSActListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/list",
            payload=request.model_dump()
        )
        return PostingFBSActListResponse(**response)
