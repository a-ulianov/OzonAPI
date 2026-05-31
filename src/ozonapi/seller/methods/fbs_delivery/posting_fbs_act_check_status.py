from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActCheckStatusRequest,
    PostingFBSActCheckStatusResponse,
)


class PostingFBSActCheckStatusMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/check-status"""

    async def posting_fbs_act_check_status(
            self: "PostingFBSActCheckStatusMixin",
            request: PostingFBSActCheckStatusRequest
    ) -> PostingFBSActCheckStatusResponse:
        """Метод для проверки статуса отгрузки и документов.

        Notes:
            • Возвращает статус формирования документов по заданию из `posting_fbs_act_create()`.
            • Содержит списки отправлений, добавленных в перевозку и не попавших в неё.
            • Рекомендуется опрашивать до статуса готовности документов.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActCheckStatus

        Args:
            request: Запрос на проверку статуса по схеме `PostingFBSActCheckStatusRequest`

        Returns:
            Статус отгрузки и документов по схеме `PostingFBSActCheckStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_check_status(
                    PostingFBSActCheckStatusRequest(
                        id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/check-status",
            payload=request.model_dump()
        )
        return PostingFBSActCheckStatusResponse(**response)
