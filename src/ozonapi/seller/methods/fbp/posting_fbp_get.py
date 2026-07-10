from ...core import APIManager
from ...schemas.fbp import PostingFbpGetRequest, PostingFbpGetResponse


class PostingFbpGetMixin(APIManager):
    """Реализует метод /v1/posting/fbp/get"""

    async def posting_fbp_get(
            self: "PostingFbpGetMixin",
            request: PostingFbpGetRequest,
    ) -> PostingFbpGetResponse:
        """Получает информацию об отправлении FBP по идентификатору.

        Notes:
            • Возвращает детальную информацию об одном отправлении по его номеру:
              аналитические и финансовые данные, состав товаров, статус и отмену.
            • Даты в ответе (`in_process_at`, `order_date`, `analytics_data.*`)
              приходят строками в формате RFC3339.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetFbpPosting

        Args:
            request: Номер отправления по схеме `PostingFbpGetRequest`

        Returns:
            Информация об отправлении по схеме `PostingFbpGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbp_get(
                    PostingFbpGetRequest(posting_number="P-1")
                )

            print(result.posting.status, result.posting.posting_number)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbp/get",
            payload=request.model_dump(),
        )
        return PostingFbpGetResponse(**response)
