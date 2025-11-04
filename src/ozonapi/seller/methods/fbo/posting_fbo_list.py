from ...core import APIManager
from ...schemas.fbo import PostingFBOListRequest, PostingFBOListResponse


class PostingFBOListMixin(APIManager):
    """Реализует метод /v2/posting/fbo/list"""

    async def posting_fbo_list(
            self: "PostingFBOListMixin",
            request: PostingFBOListRequest
    ) -> PostingFBOListResponse:
        """Метод для получения списка отправлений FBO за указанный период времени.

        Notes:
            • Период должен быть не больше одного года, иначе вернётся ошибка `PERIOD_IS_TOO_LONG`.
            • Обязательно заполните поля `since` и `to_` в фильтре для указания периода.
            • Для фильтрации можно использовать дополнительные параметры: статус отправления.
            • Для пагинации используйте `offset` и `limit` (максимум 1000 элементов в ответе, максимум 20000 для offset).
            • Можно включить транслитерацию адреса из кириллицы в латиницу через параметр `translit`.
            • Дополнительные поля (аналитика, финансовые данные, юридическая информация) можно запросить через параметр `with_`.

        References:
            https://docs.ozon.com/api/seller/?#operation/PostingAPI_GetFboPostingList

        Args:
            request: Запрос на получение информации об отправлениях FBO за указанный период времени по схеме `PostingFBOListRequest`

        Returns:
            Список отправлений FBO за указанный период времени по схеме `PostingFBOListResponse`

        Examples:
            Базовое применение:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbo_list(
                        PostingFBOListRequest(
                            filter=PostingFilter(
                                since=datetime.datetime(2025, 9, 1),
                                to=datetime.datetime(2025, 11, 17, 10, 44, 12, 828000),
                            ),
                        )
                    )

            Пример с фильтрацией по статусу:
                # OZON_SELLER_TOKEN или OZON_SELLER_CLIENT_ID + OZON_SELLER_API_KEY определены в .env
                async with SellerAPI() as api:
                    # noinspection PyArgumentList
                    result = await api.posting_fbo_list(
                        PostingFBOListRequest(
                            dir=SortingDirection.ASC,
                            filter=PostingFilter(
                                since=datetime.datetime.now() - datetime.timedelta(days=30),
                                to=datetime.datetime.now(),
                                status=PostingStatus.DELIVERED
                            ),
                            limit=100,
                            offset=0,
                            translit=False,
                            with_=PostingFilterWith(
                                analytics_data=True,
                                financial_data=False,
                                legal_info=True
                            )
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbo/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBOListResponse(**response)