from ...core import APIManager
from ...schemas.fbo import PostingFBOGetRequest, PostingFBOGetResponse


class PostingFBOGetMixin(APIManager):
    """Реализует метод /v2/posting/fbo/get"""

    async def posting_fbo_get(
            self: "PostingFBOGetMixin",
            request: PostingFBOGetRequest
    ) -> PostingFBOGetResponse:
        """Метод для получения информации об отправлении FBO по его номеру.

        Notes:
            • Для получения информации необходимо указать номер отправления в параметре `posting_number`.
            • Можно включить транслитерацию адреса из кириллицы в латиницу через параметр `translit`.
            • Дополнительные поля (аналитика, финансовые данные, юридическая информация) можно запросить через параметр `with_`.
            • В ответе содержится полная информация об отправлении: данные о товарах, аналитика, финансовая информация и юридические данные.
            • Финансовые данные включают информацию о комиссиях, выплатах, скидках и акциях.
            • Аналитические данные содержат информацию о городе, типе доставки, складе и других параметрах доставки.
            • Юридическая информация включает данные о компании покупателя (название, ИНН, КПП).

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_GetFboPosting

        Args:
            request: Запрос на получение информации об отправлении FBO по схеме `PostingFBOGetRequest`

        Returns:
            Детализированная информация об отправлении FBO по схеме `PostingFBOGetResponse`

        Examples:
            Базовое применение:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbo_get(
                        PostingFBOGetRequest(
                            posting_number="50520644-0012-7"
                        )
                    )

            Пример с дополнительными полями:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbo_get(
                        PostingFBOGetRequest(
                            posting_number="50520644-0012-7",
                            translit=True,
                            with_=PostingFilterWith(
                                analytics_data=True,
                                financial_data=True,
                                legal_info=False
                            )
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbo/get",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBOGetResponse(**response)