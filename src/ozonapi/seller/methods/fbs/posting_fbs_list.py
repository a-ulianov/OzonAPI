from ...core import APIManager
from ...schemas.fbs import PostingFBSListRequest, PostingFBSListResponse


class PostingFBSListMixin(APIManager):
    """Реализует метод /v3/posting/fbs/list"""

    async def posting_fbs_list(
            self: "PostingFBSListMixin",
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
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSListResponse(**response)
