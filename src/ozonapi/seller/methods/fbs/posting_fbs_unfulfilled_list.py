from ...core import APIManager
from ...schemas.fbs import PostingFBSUnfulfilledListRequest, PostingFBSUnfulfilledListResponse


class PostingFBSUnfulfilledListMixin(APIManager):
    """Реализует метод /v3/posting/fbs/unfulfilled/list"""

    async def posting_fbs_unfulfilled_list(
        self: "PostingFBSUnfulfilledListMixin",
        request: PostingFBSUnfulfilledListRequest
    ) -> PostingFBSUnfulfilledListResponse:
        """Метод для получения списка необработанных отправлений за указанный период времени.

        Notes:
            • Период должен быть не больше одного года.
            • Обязательно используйте фильтр либо по времени сборки — `cutoff`, либо по дате передачи отправления в доставку — `delivering_date`.
            • Если использовать фильтры `cutoff` и `delivering_date` вместе, в ответе вернётся ошибка.
            • Чтобы использовать фильтр по времени сборки, заполните поля `cutoff_from` и `cutoff_to`.
            • Чтобы использовать фильтр по дате передачи отправления в доставку, заполните поля `delivering_date_from` и `delivering_date_to`.
            • Для пагинации используйте `offset`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBS

        Args:
            request: Запрос на получение информации о необработанных отправлениях FBS и rFBS за указанный период времени по схеме `PostingFBSUnfulfilledListRequest`

        Returns:
            Список необработанных отправлений за указанный период времени по схеме `PostingFBSUnfulfilledListResponse`

        Examples:
            Базовое применение:
                async with SellerAPI(client_id, api_key) as api:
                    # noinspection PyArgumentList

                    result = await api.posting_fbs_unfulfilled_list(
                        PostingFBSUnfulfilledListRequest(
                            filter=PostingFBSUnfulfilledListFilter(
                                delivering_date_from=datetime.datetime.now() - datetime.timedelta(days=30),
                                delivering_date_to=datetime.datetime.now(),
                            ),
                        )
                    )

            Пример с фильтрацией выборки:
                async with SellerAPI(client_id, api_key) as api:
                    # noinspection PyArgumentList

                    result = await api.posting_fbs_unfulfilled_list(
                        PostingFBSUnfulfilledListRequest(
                            filter=PostingFBSUnfulfilledListFilter(
                                cutoff_from=None,
                                cutoff_to=None,
                                delivering_date_from=datetime.datetime.now() - datetime.timedelta(days=30),
                                delivering_date_to=datetime.datetime.now(),
                                delivery_method_id=[],
                                is_quantum=False,
                                provider_id=[],
                                status=None,
                                warehouse_id=[],
                                last_changed_status_date=None
                            ),
                            dir=SortingDirection.DESC,
                            limit=10,
                            offset=0,
                            with_=PostingFBSUnfulfilledListFilterWith(
                                barcodes=True,
                                financial_data=True
                            )
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/unfulfilled/list",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSUnfulfilledListResponse(**response)
