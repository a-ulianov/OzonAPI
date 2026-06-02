from ...core import APIManager
from ...schemas.fbo import PostingFBOListV2Request, PostingFBOListV2Response


class PostingFBOListV2Mixin(APIManager):
    """Реализует метод /v2/posting/fbo/list"""

    async def posting_fbo_list_v2(
            self: "PostingFBOListV2Mixin",
            request: PostingFBOListV2Request
    ) -> PostingFBOListV2Response:
        """Метод для получения списка отправлений FBO за указанный период времени (API v2).

        Notes:
            • ⚠️ Устаревший метод: Ozon отключит `/v2/posting/fbo/list` **1 августа 2026 года**.
              Перейдите на каноническую `posting_fbo_list()` (v3) с курсорной пагинацией.
              Анонс: https://dev.ozon.ru/news/734-Otkliuchenie-starykh-metodov-Seller-API-dlia-raboty-s-postingami/
            • Период должен быть не больше одного года, иначе вернётся ошибка `PERIOD_IS_TOO_LONG`.
            • Обязательно заполните поля `since` и `to_` в фильтре для указания периода.
            • Для пагинации используйте `offset` и `limit` (максимум 1000 элементов в ответе, максимум 20000 для offset).
            • Можно включить транслитерацию адреса из кириллицы в латиницу через параметр `translit`.
            • Дополнительные поля (аналитика, финансовые данные, юридическая информация) можно запросить через параметр `with_`.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_GetFboPostingList

        Args:
            request: Запрос на получение информации об отправлениях FBO за указанный период времени по схеме `PostingFBOListV2Request`

        Returns:
            Список отправлений FBO за указанный период времени по схеме `PostingFBOListV2Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbo_list_v2(
                    PostingFBOListV2Request(
                        filter=PostingFilter(
                            since=datetime.datetime(2025, 9, 1),
                            to=datetime.datetime(2025, 11, 17),
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbo/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBOListV2Response(**response)
