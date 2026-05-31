from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSDigitalActCheckStatusRequest,
    PostingFBSDigitalActCheckStatusResponse,
)


class PostingFBSDigitalActCheckStatusMixin(APIManager):
    """Реализует метод /v2/posting/fbs/digital/act/check-status"""

    async def posting_fbs_digital_act_check_status(
            self: "PostingFBSDigitalActCheckStatusMixin",
            request: PostingFBSDigitalActCheckStatusRequest
    ) -> PostingFBSDigitalActCheckStatusResponse:
        """Метод для проверки статуса формирования накладной.

        Notes:
            • Возвращает статус формирования электронных документов (накладной)
              по заданию из `posting_fbs_act_create()`.
            • Ответ возвращается без обёртки `result`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_DigitalActCheckStatus

        Args:
            request: Запрос на проверку статуса по схеме `PostingFBSDigitalActCheckStatusRequest`

        Returns:
            Статус формирования накладной по схеме `PostingFBSDigitalActCheckStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_digital_act_check_status(
                    PostingFBSDigitalActCheckStatusRequest(
                        id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/digital/act/check-status",
            payload=request.model_dump()
        )
        return PostingFBSDigitalActCheckStatusResponse(**response)
