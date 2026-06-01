from ...core import APIManager
from ...schemas.fbs import (
    PostingFBSPickUpCodeVerifyRequest,
    PostingFBSPickUpCodeVerifyResponse,
)


class PostingFBSPickUpCodeVerifyMixin(APIManager):
    """Реализует метод /v1/posting/fbs/pick-up-code/verify"""

    async def posting_fbs_pick_up_code_verify(
            self: "PostingFBSPickUpCodeVerifyMixin",
            request: PostingFBSPickUpCodeVerifyRequest
    ) -> PostingFBSPickUpCodeVerifyResponse:
        """Проверяет код курьера при передаче отправления rFBS.

        Notes:
            • Возвращает `valid` — корректен ли код курьера для отправления.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSPickupCodeVerify

        Args:
            request: Запрос проверки по схеме `PostingFBSPickUpCodeVerifyRequest`

        Returns:
            Результат проверки по схеме `PostingFBSPickUpCodeVerifyResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_pick_up_code_verify(
                    PostingFBSPickUpCodeVerifyRequest(
                        posting_number="123-456-1", pickup_code="0000"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/pick-up-code/verify",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSPickUpCodeVerifyResponse(**response)
