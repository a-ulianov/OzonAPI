from async_lru import alru_cache

from ..core import APIManager, method_rate_limit
from ..core.exceptions import APINotFoundError
from ..schemas.fbs import PostingFBSUnfulfilledListRequest, PostingFBSUnfulfilledListResponse, PostingFBSListResponse, \
    PostingFBSListRequest, PostingFBSGetRequest, PostingFBSGetResponse, PostingFBSGetByBarcodeResponse, \
    PostingFBSGetByBarcodeRequest, PostingFBSMultiBoxQtySetResponse, PostingFBSMultiBoxQtySetRequest, \
    PostingFBSProductChangeRequest, PostingFBSProductChangeResponse, PostingFBSProductCountryListResponse, \
    PostingFBSProductCountryListRequest, PostingFBSProductCountrySetRequest, PostingFBSProductCountrySetResponse, \
    PostingFBSRestrictionsResponse, PostingFBSRestrictionsRequest


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

    @method_rate_limit(limit_requests=2, interval_seconds=1)
    async def posting_fbs_get(
            self: "SellerFBSAPI",
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
            json=request.model_dump(by_alias=True)
        )
        return PostingFBSGetResponse(**response)

    async def posting_fbs_get_by_barcode(
            self: "SellerFBSAPI",
            request: PostingFBSGetByBarcodeRequest
    ) -> PostingFBSGetByBarcodeResponse:
        """Метод для получения информации об отправлении FBS по штрихкоду.

        Notes:
            • Штрихкод отправления можно получить с помощью методов posting_fbs_get(), posting_fbs_list(), posting_fbs_unfulfilled_list() в массиве barcodes
            • Метод возвращает основную информацию об отправлении: статус, данные о заказе, товары и штрихкоды.
            • Для получения дополнительных данных (финансовой информации, аналитики и т.д.) используйте метод posting_fbs_get().

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_GetFbsPostingByBarcode

        Args:
            request: Запрос на получение информации об отправлении по штрихкоду по схеме `PostingFBSGetByBarcodeRequest`

        Returns:
            Информация об отправлении FBS по схеме `PostingFBSGetByBarcodeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_get_by_barcode(
                    PostingFBSGetByBarcodeRequest(
                        barcode="20325804886000"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/get-by-barcode",
            json=request.model_dump()
        )
        return PostingFBSGetByBarcodeResponse(**response["result"])

    async def posting_fbs_multiboxqty_set(
            self: "SellerFBSAPI",
            request: PostingFBSMultiBoxQtySetRequest
    ) -> PostingFBSMultiBoxQtySetResponse:
        """Метод для передачи количества коробок для отправлений, в которых есть многокоробочные товары.

        Notes:
            • Метод используется при работе по схеме rFBS Агрегатор — с доставкой партнёрами Ozon.
            • Используется только для многокоробочных отправлений, где товары упакованы в несколько коробок.
            • Количество коробок должно быть целым положительным числом.
            • После успешного выполнения метода система учитывает указанное количество коробок при дальнейшей обработке отправления.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_PostingMultiBoxQtySetV3

        Args:
            request: Запрос на указание количества коробок для многокоробочного отправления по схеме `PostingFBSMultiBoxQtySetRequest`

        Returns:
            Результат выполнения операции по схеме `PostingFBSMultiBoxQtySetResponse`

        Examples:
            Пример с проверкой результата:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_multiboxqty_set(
                        PostingFBSMultiBoxQtySetRequest(
                            posting_number="57195475-0050-3",
                            multi_box_qty=3
                        )
                    )

                    if result.result.result:
                        print("Количество коробок успешно передано")
                    else:
                        print("Произошла ошибка при указании количества коробок")
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/multi-box-qty/set",
            json=request.model_dump()
        )
        return PostingFBSMultiBoxQtySetResponse(**response)

    async def posting_fbs_product_change(
            self: "SellerFBSAPI",
            request: PostingFBSProductChangeRequest
    ) -> PostingFBSProductChangeResponse:
        """Метод для добавления веса для весовых товаров в отправлении FBS.

        Notes:
            • Метод используется для указания фактического веса весовых товаров в отправлении.
            • Можно указать вес для нескольких товаров в одном запросе.
            • После указания веса система пересчитывает стоимость доставки и другие параметры отправления.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_ChangeFbsPostingProduct

        Args:
            request: Запрос на добавление веса для весовых товаров в отправлении по схеме `PostingFBSProductChangeRequest`

        Returns:
            Результат выполнения операции по схеме `PostingFBSProductChangeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_change(
                    PostingFBSProductChangeRequest(
                        posting_number="33920158-0006-1",
                        items=[
                            PostingFBSProductChangeRequestItem(
                                sku=1231428352,
                                weight_real=0.3
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/change",
            json=request.model_dump(by_alias=True)
        )
        return PostingFBSProductChangeResponse(**response)

    @alru_cache(ttl=86400)
    async def posting_fbs_product_country_list(
            self: "SellerFBSAPI",
            request: PostingFBSProductCountryListRequest = PostingFBSProductCountryListRequest.model_construct()
    ) -> PostingFBSProductCountryListResponse:
        """Метод для получения списка доступных стран-изготовителей и их ISO кодов.

        Notes:
            • Метод возвращает полный список стран-изготовителей, доступных для указания в карточках товаров.
            • Для фильтрации результатов можно использовать параметр `name_search` - поисковая строка по названию страны.
            • Если параметр `name_search` не указан или пустой, возвращается полный список всех доступных стран.
            • Поиск осуществляется по частичному совпадению с названием страны на русском языке.
            • Регистр букв в поисковой строке не имеет значения.
            • ISO код страны возвращается в формате двухбуквенного кода (Alpha-2) согласно стандарту ISO 3166-1.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_ListCountryProductFbsPostingV2

        Args:
            request: Запрос на получение списка стран-изготовителей по схеме `PostingFBSProductCountryListRequest`

        Returns:
            Список доступных стран-изготовителей с их ISO кодами по схеме `PostingFBSProductCountryListResponse`

        Examples:
            Базовое применение (получение полного списка стран):
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_product_country_list(
                        PostingFBSProductCountryListRequest()
                    )

            Пример с фильтрацией по названию страны (частичное совпадение):
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.posting_fbs_product_country_list(
                        PostingFBSProductCountryListRequest(
                            name_search="тУрЦ"
                        )
                    )
        """
        try:
            response = await self._request(
                method="post",
                api_version="v2",
                endpoint="posting/fbs/product/country/list",
                json=request.model_dump()
            )
        except APINotFoundError:
            return PostingFBSProductCountryListResponse.model_construct()
        return PostingFBSProductCountryListResponse(**response)

    async def posting_fbs_product_country_set(
            self: "SellerFBSAPI",
            request: PostingFBSProductCountrySetRequest
    ) -> PostingFBSProductCountrySetResponse:
        """Метод для добавления информации о стране-изготовителе товара в отправлении FBS.

        Notes:
            • Метод используется для добавления атрибута «Страна-изготовитель» к товару в отправлении, если он не был указан ранее.
            • Страна-изготовитель указывается в формате двухбуквенного кода стандарта ISO 3166-1 (Alpha-2).
            • Список доступных стран-изготовителей и их ISO кодов можно получить с помощью метода posting_fbs_product_country_list().
            • После успешного выполнения метода система возвращает признак необходимости передачи номера ГТД (грузовой таможенной декларации).
            • Если is_gtd_needed = true, необходимо передать номер ГТД для указанного продукта и отправления.
            • Метод может быть применен только к отправлениям, где страна-изготовитель еще не указана.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_SetCountryProductFbsPostingV2

        Args:
            request: Запрос на добавление информации о стране-изготовителе товара по схеме `PostingFBSProductCountrySetRequest`

        Returns:
            Результат выполнения операции с информацией о необходимости ГТД по схеме `PostingFBSProductCountrySetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_country_set(
                    PostingFBSProductCountrySetRequest(
                        posting_number="57195475-0050-3",
                        product_id=180550365,
                        country_iso_code="NO"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/country/set",
            json=request.model_dump()
        )
        return PostingFBSProductCountrySetResponse(**response)

    async def posting_fbs_restrictions(
            self: "SellerFBSAPI",
            request: PostingFBSRestrictionsRequest
    ) -> PostingFBSRestrictionsResponse:
        """Метод для получения габаритных, весовых и прочих ограничений пункта приёма по номеру отправления.

        Notes:
            • Метод применим только для работы по схеме FBS.
            • Возвращает ограничения пункта приёма, связанные с указанным отправлением.
            • Ограничения включают габаритные (ширина, высота, длина), весовые (мин./макс. вес) и стоимостные (мин./макс. цена) параметры.
            • Вес указывается в граммах, габариты — в сантиметрах, стоимость — в рублях.
            • Если для какого-то параметра ограничение не установлено, значение будет None.
            • Метод помогает определить, соответствует ли отправление требованиям пункта приёма перед передачей.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetRestrictions

        Args:
            request: Запрос на получение ограничений пункта приёма по номеру отправления по схеме `PostingFBSRestrictionsRequest`

        Returns:
            Ограничения пункта приёма для указанного отправления по схеме `PostingFBSRestrictionsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_restrictions(
                    PostingFBSRestrictionsRequest(
                        posting_number="76673629-0020-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/restrictions",
            json=request.model_dump()
        )
        return PostingFBSRestrictionsResponse(**response["result"])