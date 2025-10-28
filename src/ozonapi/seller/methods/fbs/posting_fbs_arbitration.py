from ...core import APIManager
from ...schemas.fbs import PostingFBSArbitrationRequest, PostingFBSArbitrationResponse


class PostingFBSArbitrationMixin(APIManager):
    """Реализует метод /v2/posting/fbs/arbitration"""

    async def posting_fbs_arbitration(
            self: "PostingFBSArbitrationMixin",
            request: PostingFBSArbitrationRequest
    ) -> PostingFBSArbitrationResponse:
        """Метод для открытия спора по отправлениям FBS.

        Notes:
            • Если отправление передано в доставку, но не просканировано в сортировочном центре, можно открыть спор.
            • Открытый спор переведёт отправление в статус `arbitration`.
            • Метод позволяет открыть спор для одного или нескольких отправлений одновременно.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_MoveFbsPostingToArbitration

        Args:
            request: Запрос на открытие спора по отправлениям по схеме `PostingFBSArbitrationRequest`

        Returns:
            Результат обработки запроса по схеме `PostingFBSArbitrationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_arbitration(
                    PostingFBSArbitrationRequest(
                        posting_number=["33920143-1195-1", ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/arbitration",
            payload=request.model_dump()
        )
        return PostingFBSArbitrationResponse(**response)