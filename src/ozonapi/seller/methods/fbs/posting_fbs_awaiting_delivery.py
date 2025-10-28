from ...core import APIManager
from ...schemas.fbs import PostingFBSAwaitingDeliveryRequest, PostingFBSAwaitingDeliveryResponse


class PostingFBSAwaitingDeliveryMixin(APIManager):
    """Реализует метод /v2/posting/fbs/awaiting-delivery"""

    async def posting_fbs_awaiting_delivery(
            self: "PostingFBSAwaitingDeliveryMixin",
            request: PostingFBSAwaitingDeliveryRequest
    ) -> PostingFBSAwaitingDeliveryResponse:
        """Метод для передачи отправлений к отгрузке.

        Notes:
            • Метод изменяет статус отправления на `awaiting_deliver`.
            • В одном запросе можно передать не больше `100` идентификаторов отправлений.
            • Метод применяется для передачи спорных заказов к отгрузке.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_MoveFbsPostingToAwaitingDelivery

        Args:
            request: Запрос на передачу отправлений к отгрузке по схеме `PostingFbsAwaitingDeliveryRequest`

        Returns:
            Результат обработки запроса по схеме `PostingFbsAwaitingDeliveryResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_awaiting_delivery(
                    PostingFbsAwaitingDeliveryRequest(
                        posting_number=["33920143-1195-1", ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/awaiting-delivery",
            payload=request.model_dump()
        )
        return PostingFBSAwaitingDeliveryResponse(**response)