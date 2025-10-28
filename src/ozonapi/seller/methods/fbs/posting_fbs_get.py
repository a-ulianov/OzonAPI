from ...core import APIManager, method_rate_limit
from ...schemas.fbs import PostingFBSGetRequest, PostingFBSGetResponse


class PostingFBSGetMixin(APIManager):
    """Реализует метод /v3/posting/fbs/get"""

    @method_rate_limit(limit_requests=2, interval_seconds=1)
    async def posting_fbs_get(
            self: "PostingFBSGetMixin",
            request: PostingFBSGetRequest
    ) -> PostingFBSGetResponse:
        """Метод для получения информации об отправлении FBS по его номеру.

        Notes:
            • Метод часто возвращает 429 (TooManyRequestsError), поэтому установлено ограничение 2 запроса в секунду (экспериментальное значение).
            • Чтобы получать актуальную дату отгрузки, регулярно обновляйте информацию об отправлениях или подключите пуш-уведомления.
            • Для получения дополнительных данных используйте параметр `with_` в запросе.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetFbsPostingV3

        Args:
            request: Запрос на получение информации об отправлении FBS по схеме `PostingFBSGetRequest`

        Returns:
            Детализированная информация об отправлении по схеме `PostingFBSGetResponse`

        Examples:
            Базовое применение:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_get(
                        PostingFBSGetRequest(
                            posting_number="57195475-0050-3"
                        )
                    )

            Пример с дополнительными полями:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_get(
                        PostingFBSGetRequest(
                            posting_number="57195475-0050-3",
                            with_=PostingFBSGetRequestWith(
                                analytics_data=True,
                                barcodes=True,
                                financial_data=True,
                                legal_info=False,
                                product_exemplars=True,
                                related_postings=True,
                                translit=False
                            )
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/get",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSGetResponse(**response)
