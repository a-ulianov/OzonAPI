from ..core import APIManager
from ..schemas.fbs import PostingFBSUnfulfilledListRequest, PostingFBSUnfulfilledListResponse, PostingFBSListResponse, \
    PostingFBSListRequest, PostingFBSGetRequest, PostingFBSGetResponse


class SellerFBSAPI(APIManager):
    """Реализует методы раздела Обработка заказов FBS и rFBS.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/FBS
    """

    async def posting_fbs_unfulfilled_list(
        self: "SellerFBSAPI",
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
            json=request.model_dump(by_alias=True)
        )
        return PostingFBSUnfulfilledListResponse(**response)

    async def posting_fbs_list(
            self: "SellerFBSAPI",
            request: PostingFBSListRequest
    ) -> PostingFBSListResponse:
        """Метод для получения списка отправлений FBS за указанный период времени.

        Notes:
            • Период должен быть не больше одного года.
            • Обязательно заполните поля `since` и `to` для указания периода.
            • Для фильтрации можно использовать дополнительные параметры: статус, склад, службу доставки и другие.
            • Для пагинации используйте `offset`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_GetFbsPostingListV3

        Args:
            request: Запрос на получение информации об отправлениях FBS за указанный период времени по схеме `PostingFBSListRequest`

        Returns:
            Список отправлений FBS за указанный период времени по схеме `PostingFBSListResponse`

        Examples:
            Базовое применение:
                async with SellerAPI(client_id, api_key) as api:
                    # noinspection PyArgumentList

                    result = await api.posting_fbs_list(
                        PostingFBSListRequest(
                            filter=PostingFBSListFilter(
                                since=datetime.datetime.now() - datetime.timedelta(days=300),
                                to_=datetime.datetime.now(),
                            )
                        )
                    )

            Пример с фильтрацией выборки:
                async with SellerAPI(client_id, api_key) as api:
                    # noinspection PyArgumentList

                    result = await api.posting_fbs_list(
                        PostingFBSListRequest(
                            filter=PostingFBSListFilter(
                                since=datetime.datetime.now() - datetime.timedelta(days=30),
                                to_=datetime.datetime.now(),
                                status=PostingStatus.AWAITING_PACKAGING,
                                warehouse_id=[21321684811000],
                                provider_id=[24],
                                delivery_method_id=[21321684811000],
                                order_id=123456,
                                posting_number="123456789",
                                product_offer_id="ART-001",
                                product_sku=987654321,
                                last_changed_status_date=PostingFBSListRequestFilterLastChangedStatusDate(
                                    from_=datetime.datetime.now() - datetime.timedelta(days=7),
                                    to_=datetime.datetime.now()
                                ),
                                is_quantum=False
                            ),
                            dir=SortingDirection.ASC,
                            limit=100,
                            offset=0,
                            with_=PostingFBSListFilterWith(
                                analytics_data=True,
                                barcodes=True,
                                financial_data=True,
                                legal_info=False,
                                translit=True
                            )
                        )
                    )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/list",
            json=request.model_dump(by_alias=True)
        )
        return PostingFBSListResponse(**response)

    async def posting_fbs_get(
            self: "SellerFBSAPI",
            request: PostingFBSGetRequest
    ) -> PostingFBSGetResponse:
        """Метод для получения информации об отправлении FBS по его номеру.

        Notes:
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
            json=request.model_dump(by_alias=True)
        )
        return PostingFBSGetResponse(**response)