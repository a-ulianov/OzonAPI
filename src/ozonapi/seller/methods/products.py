from ..core import APIManager
from ..schemas.products import ProductArchiveResponse, ProductArchiveRequest, ProductUnarchiveRequest, \
    ProductUnarchiveResponse, ProductImportRequest, ProductImportResponse, ProductImportInfoRequest, \
    ProductImportInfoResponse, ProductImportBySkuRequest, ProductImportBySkuResponse, ProductAttributesUpdateRequest, \
    ProductAttributesUpdateResponse, ProductsDeleteRequest, ProductsDeleteResponse, ProductInfoAttributesRequest, \
    ProductInfoAttributesResponse, ProductInfoListRequest, ProductInfoListResponse, ProductInfoSubscriptionRequest, \
    ProductInfoSubscriptionResponse, ProductListRequest, ProductListResponse, ProductPicturesInfoRequest, \
    ProductPicturesInfoResponse, ProductRatingBySkuRequest, ProductRatingBySkuResponse, ProductRelatedSkuGetRequest, \
    ProductRelatedSkuGetResponse, ProductUpdateOfferIdRequest, ProductUpdateOfferIdResponse


class SellerProductAPI(APIManager):
    """Реализует методы раздела Загрузка и обновление товаров.

    References:
        https://docs.ozon.ru/api/seller/?__rr=1#tag/ProductAPI
    """

    async def product_archive(
        self: "SellerProductAPI", request: ProductArchiveRequest
    ) -> ProductArchiveResponse:
        """Перемещает товарные карточки в архив.

        Notes:
            • Вы можете передать до `100` идентификаторов за раз.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductArchive

        Args:
            request: Список `product_id` по схеме `ProductArchiveRequest`.

        Returns:
            Логическое значение выполнения операции по схеме `ProductArchiveResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_archive(
                    ProductArchiveRequest(
                        product_id=[1234567, ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/archive",
            json=request.model_dump(),
        )
        return ProductArchiveResponse(**response)

    async def product_import(
        self: "SellerProductAPI", request: ProductImportRequest
    ) -> ProductImportResponse:
        """
        Формирует задачу на создание товаров и обновление информации о них.

        Notes:
            • В сутки можно создать или обновить определённое количество товаров. Чтобы узнать лимит, используйте `product_info_limit()`. Если количество загрузок и обновлений товаров превысит лимит, появится ошибка `item_limit_exceeded`.
            • В одном запросе можно передать до `100` товаров. Каждый товар — это отдельный элемент в массиве `items`. Укажите всю информацию о товаре: его характеристики, штрихкод, изображения, габариты, цену и валюту цены.
            • При обновлении товара передайте в запросе всю информацию о нём.
            • Указанная валюта должна совпадать с той, которая установлена в настройках личного кабинета. По умолчанию передаётся `RUB` — российский рубль. Например, если у вас установлена валюта юань, передавайте значение `CNY`, иначе вернётся ошибка.
            • Товар не будет создан или обновлён, если вы заполните неправильно или не укажете:
                - Обязательные характеристики: характеристики отличаются для разных категорий — их можно посмотреть в `Базе знаний продавца` или получить методом `description_category_attribute()`.
                - Реальные объёмно-весовые характеристики: `depth`, `width`, `height`, `dimension_unit`, `weight`, `weight_unit`. Не пропускайте эти параметры в запросе и не указывайте `0`.
            • Для некоторых характеристик можно использовать HTML-теги.
            • После модерации товар появится в вашем личном кабинете, но не будет виден пользователям, пока вы не выставите его на продажу.
            • Каждый товар в запросе — отдельный элемент массива `items`.
            • Чтобы объединить две карточки, для каждой передайте `9048` в массиве `attributes`. Все атрибуты в этих карточках, кроме размера или цвета, должны совпадать.
            • Запросы обрабатываются очередями.
            • Для получения детализированной информации о результате выполнения операции используйте метод `product_import_info()`.

            **Загрузка изображений**

            • Для загрузки передайте в запросе ссылки на изображения в общедоступном облачном хранилище. Формат изображения по ссылке — `JPG` или `PNG`.
            • Изображения в массиве `images` располагайте в соответствии с желаемым порядком на сайте. Для загрузки главного изображения товара используйте параметр `primary_image`. Если не передать значение primary_image, главным будет первое изображение в массиве images.
            • Для каждого товара вы можете загрузить до `30` изображений, включая главное. Если передать значение `primary_image`, максимальное количество изображений в `images` — `29`. Если параметр `primary_image` пустой, то в `images` можно передать до `30` изображений.
            • Для загрузки изображений 360 используйте поле `images360`, для загрузки маркетингового цвета — `color_image`.
            • Если вы хотите изменить состав или порядок изображений, получите информацию с помощью метода `product_info_list` — в нём отображается текущий порядок и состав изображений. Скопируйте данные полей `images`, `images360`, `color_image`, измените и дополните состав или порядок в соответствии с необходимостью.

            **Загрузка видео**

            Для загрузки передайте в запросе ссылки на видео.
            Для этого в параметре `complex_attributes` передайте объект. В нём в массиве `attributes` передайте 2 объекта с `complex_id = 100001`:
            • В первом укажите `id = 21841` и в массиве `values` передайте объект со ссылкой на видео.
            • Во втором укажите значение `id = 21837` и в массиве `values` передайте объект с названием видео.

            Если вы хотите загрузить несколько видео, передавайте значения для каждого видео в разных объектах массива `values`.

                values = [
                    ProductAttribute(
                        complex_id=100001, id=21837,
                        values=[ProductAttributeValue(value="videoName_1"), ProductAttributeValue(value="videoName_2")]
                    ),
                    ProductAttribute(
                        complex_id=100001, id=21841,
                        values=[ProductAttributeValue(value="https://www.youtube.com/watch?v=ZwM0iBn03dY"), ProductAttributeValue(value="https://www.youtube.com/watch?v=dQw4w9WgXcQ")]
                    )
                ]

            **Загрузка таблицы размеров**

            Вы можете добавить в карточку товара таблицу размеров, созданную с помощью конструктора (https://table-constructor.ozon.ru/visual-editor). Передайте её в массиве `attributes` в формате `JSON` как Rich-контент `id = 13164`.
            Конструктор в формате JSON: https://table-constructor.ozon.ru/schema.json
            Подробнее о конструкторе в `Базе знаний продавца`: https://docs.ozon.ru/global/products/requirements/size-table-constructor/

            **Загрузка видеообложки**

            Вы можете загрузить видеообложку через `complex_attributes`:

                complex_attributes=[
                    ProductAttribute(
                        id=21845, complex_id=100002,
                        values=[ProductAttributeValue(dictionary_value_id=0, value="https://v.ozone.ru/vod/video-10/01GFATWQVCDE7G5B721421P1231Q7/asset_1.mp4")]
                    ),
                ]

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ImportProductsV3

        Args:
            request: Массив товаров с детальными характеристиками (полный перечень в `ProductImportItem`)

        Returns:
            Айдишник таски, результаты выполнения которой затем можно проверить методом `product_import_info()

        Example:
            items = [
                ProductImportItem(
                    attributes=[
                        ProductAttribute( complex_id=0, id=5076, values=[ProductAttributeValue(dictionary_value_id=971082156, value="Стойка для акустической системы")]),
                        ProductAttribute(complex_id=0, id=9048, values=[ProductAttributeValue(value="Комплект защитных плёнок для X3 NFC. Темный хлопок")]),
                        ProductAttribute(complex_id=0, id=8229, values=[ProductAttributeValue(dictionary_value_id=95911, value="Комплект защитных плёнок для X3 NFC. Темный хлопок")]),
                        ProductAttribute(complex_id=0, id=85, values=[ProductAttributeValue(dictionary_value_id=5060050, value="Samsung")]),
                        ProductAttribute(complex_id=0, id=10096, values=[ProductAttributeValue(dictionary_value_id=61576, value="серый")])
                    ],
                    barcode="112772873170",
                    description_category_id=17028922,
                    new_description_category_id=0,
                    color_image="",
                    complex_attributes=[],
                    currency_code=CurrencyCode.RUB,
                    depth=10,
                    dimension_unit="mm",
                    height=250,
                    images=[],
                    images360=[],
                    name="Комплект защитных плёнок для X3 NFC. Темный хлопок",
                    offer_id="143210608",
                    old_price="1100",
                    pdf_list=[],
                    price="1000",
                    primary_image="",
                    promotions=[ProductImportRequestItemPromotion(operation=PromotionOperation.UNKNOWN, type=PromotionType.REVIEWS_PROMO)],
                    type_id=91565,
                    vat=VAT.PERCENT_10,
                    weight=100,
                    weight_unit="g",
                    width=150
                )
            ]

            async with SellerAPI(**credentials) as api:
                result = await api.product_import(
                    ProductImportRequest(items=items)
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/import",
            json=request.model_dump(),
        )
        return ProductImportResponse(**response)

    async def product_import_info(
        self: "SellerProductAPI", request: ProductImportInfoRequest
    ) -> ProductImportInfoResponse:
        """Получает информацию об обработке задачи загрузки или обновления товарных карточек.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_GetImportProductsInfo

        Args:
            request: Айдишник задачи по схеме `ProductImportInfoRequest`

        Returns:
            Массив с информаций об обработанных товарах и их кол-ве по схеме `ProductImportInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_import_info(
                    ProductImportInfoRequest(task_id=1234567),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import/info",
            json=request.model_dump(),
        )
        return ProductImportInfoResponse(**response)

    async def product_import_by_sku(
        self: "SellerProductAPI", request: ProductImportBySkuRequest
    ) -> ProductImportBySkuResponse:
        """Создаёт копию карточки товара с указанным SKU.

        Notes:
            • Создать копию не получится, если продавец запретил копирование своих карточек.
            • Обновить товар по SKU нельзя.
            • Запросы обрабатываются очередями.
            • Для получения детализированной информации о результате выполнения операции используйте метод `product_import_info()`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ImportProductsBySKU

        Args:
            request: SKU с которого делается копия и ряд свойств для нового товара по схеме `ProductImportBySkuRequest`

        Returns:
            Айдишник таски для `product_import_info()` и список `product_id` по схеме `ProductImportBySkuResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_import_by_sku(
                    ProductImportBySkuRequest(
                        items=[
                            ProductImportBySkuRequestItem(
                                sku=298789742,
                                name="Новый товар",
                                offer_id="article-12345",
                                currency_code=CurrencyCode.RUB,
                                old_price="2590.00",
                                price="2300.00",
                                vat=VAT.TEN_PERCENT
                            ),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/import-by-sku",
            json=request.model_dump(),
        )
        return ProductImportBySkuResponse(**response)

    async def product_attributes_update(
        self: "SellerProductAPI", request: ProductAttributesUpdateRequest
    ) -> ProductAttributesUpdateResponse:
        """Формирует задание на обновление товаров и их характеристик.

        Notes:
            • Запросы обрабатываются очередями.
            • Для получения детализированной информации о результате выполнения операции используйте метод `product_import_info()`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductUpdateAttributes

        Args:
            request: Список товарных идентификаторов с характеристиками, которые нужно обновить по схеме `ProductAttributesUpdateRequest`.

        Returns:
            Айдишник таски, результаты выполнения которой затем можно проверить методом `product_import_info()

        Example:
            attributes = [
                ProductAttributesUpdateItemAttribute(
                    complex_id=0, id=1,
                    values=[ProductAttributesUpdateItemAttributeValue(dictionary_value_id=0, value="string"), ]
                ),
            ]

            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_attributes_update(
                    ProductAttributesUpdateRequest(
                        items=[ProductAttributesUpdateItem(offer_id="article-12345", attributes=attributes), ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/attributes/update",
            json=request.model_dump(),
        )
        return ProductAttributesUpdateResponse(**response)

    async def products_delete(
        self: "SellerProductAPI", request: ProductsDeleteRequest
    ) -> ProductsDeleteResponse:
        """Удаляет архивные товары без SKU из системы Ozon.

        Notes:
            • В одном запросе можно передать до `500` идентификаторов товаров.
            • Удалить можно только товары без SKU из архива.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_DeleteProducts

        Args:
            request: Список товаров для удаления по схеме `ProductsDeleteRequest`.

        Returns:
            Статус обработки запроса для каждого товара по схеме `ProductsDeleteResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.products_delete(
                    ProductsDeleteRequest(
                        products=[
                            ProductDeleteRequestItem(offer_id="033"),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="products/delete",
            json=request.model_dump(),
        )
        return ProductsDeleteResponse(**response)

    async def product_unarchive(
        self: "SellerProductAPI", request: ProductUnarchiveRequest
    ) -> ProductUnarchiveResponse:
        """Восстанавливает товары из архива.

        Notes:
            • В одном запросе можно передать до `100` идентификаторов товаров.
            • В сутки можно восстановить из архива не больше `10` товаров, которые были архивированы автоматически.
            • Лимит обновляется в `03:00` по московскому времени.
            • На разархивацию товаров, перенесённых в архив вручную, ограничений нет.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductUnarchive

        Args:
            request: Список `product_id` для восстановления из архива по схеме `ProductUnarchiveRequest`.

        Returns:
            Результат обработки запроса по схеме `ProductUnarchiveResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_unarchive(
                    ProductUnarchiveRequest(
                        product_id=[125529926]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/unarchive",
            json=request.model_dump(),
        )
        return ProductUnarchiveResponse(**response)

    async def product_info_attributes(
        self: "SellerProductAPI", request: ProductInfoAttributesRequest=ProductInfoAttributesRequest.model_construct(),
    ) -> ProductInfoAttributesResponse:
        """Получает описание характеристик товаров по идентификаторам и видимости.

        Notes:
            • Можно не передавать идентификаторы, фильтр, можно вообще ничего не передавать - выберет всё по максимальному лимиту.
            • Товар можно искать по `offer_id`, `product_id` или `sku`.
            • Можно передавать до `1000` значений в фильтре.
            • Для пагинации используйте параметр `last_id` из ответа предыдущего запроса.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductAttributesV4

        Args:
            request: Фильтр и параметры запроса для получения характеристик товаров по схеме `ProductInfoAttributesRequest`.

        Returns:
            Описание характеристик товаров с пагинацией по схеме `ProductInfoAttributesResponse`.

        Examples:
            Базовый пример использования:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_attributes()

            Пример с фильтрацией выборки:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_attributes(
                        ProductInfoAttributesRequest(
                            filter=ProductInfoAttributesFilter(
                                product_id=[213761435],
                                offer_id=["testtest5"],
                                sku=[123495432],
                                visibility=Visibility.ALL
                            ),
                            limit=100,
                            sort_dir=SortingDirection.ASC
                        ),
                    )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="product/info/attributes",
            json=request.model_dump(),
        )
        return ProductInfoAttributesResponse(**response)

    async def product_info_list(
        self: "SellerProductAPI", request: ProductInfoListRequest
    ) -> ProductInfoListResponse:
        """Получает информацию о товарах по их идентификаторам.

        Notes:
            • В запросе можно использовать что-то одно - либо `offer_id`, либо `product_id`, либо `sku`.
            • В одном запросе можно передать не больше `1000` идентификаторов.
            • 12 ноября 2025 отключим параметр `marketing_price` в ответе метода.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductInfoList

        Args:
            request: Идентификаторы товаров для получения информации по схеме `ProductInfoListRequest`.

        Returns:
            Информация о товарах по схеме `ProductInfoListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_info_list(
                    ProductInfoListRequest(
                        product_id=[123456789, 987654321],
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/info/list",
            json=request.model_dump(),
        )
        return ProductInfoListResponse(**response)

    async def product_subscription(
        self: "SellerProductAPI", request: ProductInfoSubscriptionRequest
    ) -> ProductInfoSubscriptionResponse:
        """Получает по SKU количество пользователей, подписавшихся на уведомление о поступлении товара.

        Notes:
            • Метод возвращает количество пользователей, которые нажали «Узнать о поступлении» на странице товара.
            • Вы можете передать несколько товаров в одном запросе.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductInfoSubscription

        Args:
            request: Список SKU товаров для получения информации о подписках по схеме `ProductInfoSubscriptionRequest`.

        Returns:
            Количество подписавшихся пользователей для каждого товара по схеме `ProductInfoSubscriptionResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_subscription(
                    ProductInfoSubscriptionRequest(
                        skus=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/info/subscription",
            json=request.model_dump(),
        )
        return ProductInfoSubscriptionResponse(**response)

    async def product_list(
        self: "SellerProductAPI", request: ProductListRequest = ProductListRequest.model_construct()
    ) -> ProductListResponse:
        """Получает список всех товаров продавца.

        Notes:
            • Можно использовать без параметров - выводит всё по максимальному лимиту.
            • Если вы используете фильтр по идентификатору `offer_id` или `product_id`, остальные параметры заполнять не обязательно.
            • За один раз можно использовать только одну группу идентификаторов, не больше 1000 товаров.
            • Для пагинации используйте параметр `last_id` из ответа предыдущего запроса.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductList

        Args:
            request: Фильтр и параметры пагинации для получения списка товаров по схеме `ProductListRequest`.

        Returns:
            Список товаров с информацией об остатках и пагинацией по схеме `ProductListResponse`.

        Example:
            Базовый пример выборки:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_list()

            Пример выборки с фильтрацией:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_list(
                        ProductListRequest(
                            filter=ProductListFilter(
                                offer_id=["136748"],
                                product_id=[223681945],
                                visibility=Visibility.ALL
                            ),
                            limit=100,
                            last_id=""
                        ),
                    )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/list",
            json=request.model_dump(),
        )
        return ProductListResponse(**response)

    async def product_pictures_info(
        self: "SellerProductAPI", request: ProductPicturesInfoRequest
    ) -> ProductPicturesInfoResponse:
        """Получает информацию об изображениях товаров.

        Notes:
            • В одном запросе можно передать до `1000` идентификаторов товаров.
            • Метод возвращает ссылки на все типы изображений товара: основные фото, образцы цвета и изображения 360°.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductInfoPicturesV2

        Args:
            request: Список `product_id` для получения информации об изображениях по схеме `ProductPicturesInfoRequest`.

        Returns:
            Информация об изображениях товаров с возможными ошибками загрузки по схеме `ProductPicturesInfoResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_pictures_info(
                    ProductPicturesInfoRequest(
                        product_id=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="product/pictures/info",
            json=request.model_dump(),
        )
        return ProductPicturesInfoResponse(**response)

    async def product_rating_by_sku(
        self: "SellerProductAPI", request: ProductRatingBySkuRequest
    ) -> ProductRatingBySkuResponse:
        """Получает по SKU контент-рейтинг товаров и рекомендации по его увеличению.

        Notes:
            • Контент-рейтинг товара рассчитывается от `0` до `100`.
            • Метод возвращает детальную информацию по группам характеристик, влияющим на рейтинг.
            • В ответе содержатся рекомендации по заполнению атрибутов для улучшения рейтинга.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductRatingBySku

        Args:
            request: Список SKU товаров для получения контент-рейтинга по схеме `ProductRatingBySkuRequest`.

        Returns:
            Контент-рейтинг товаров с детализацией по группам характеристик по схеме `ProductRatingBySkuResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_rating_by_sku(
                    ProductRatingBySkuRequest(
                        skus=[179737222, 179737223]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/rating-by-sku",
            json=request.model_dump(),
        )
        return ProductRatingBySkuResponse(**response)

    async def product_related_sku_get(
        self: "SellerProductAPI", request: ProductRelatedSkuGetRequest
    ) -> ProductRelatedSkuGetResponse:
        """Получает единый SKU по старым идентификаторам SKU FBS и SKU FBO.

        Notes:
            • В ответе возвращаются все SKU, связанные с переданными.
            • Метод может обработать любые SKU, даже скрытые или удалённые.
            • В одном запросе можно передать до 200 SKU.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductGetRelatedSKU

        Args:
            request: Список SKU для получения связанных идентификаторов по схеме `ProductRelatedSkuGetRequest`.

        Returns:
            Информация о связанных SKU и возможные ошибки обработки по схеме `ProductRelatedSkuGetResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_related_sku_get(
                    ProductRelatedSkuGetRequest(
                        sku=[123456789, 987654321]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/related-sku/get",
            json=request.model_dump(),
        )
        return ProductRelatedSkuGetResponse(**response)

    async def product_update_offer_id(
        self: "SellerProductAPI", request: ProductUpdateOfferIdRequest
    ) -> ProductUpdateOfferIdResponse:
        """Изменяет артикулы товаров в системе продавца.

        Notes:
            • Метод позволяет изменить несколько `offer_id` в одном запросе.
            • Рекомендуется передавать до `250` пар артикулов в одном запросе.
            • Длина нового артикула не должна превышать `50` символов.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductUpdateOfferID

        Args:
            request: Список пар текущий/новый артикул для изменения по схеме `ProductUpdateOfferIdRequest`.

        Returns:
            Информация об ошибках изменения артикулов по схеме `ProductUpdateOfferIdResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_update_offer_id(
                    ProductUpdateOfferIdRequest(
                        update_offer_id=[
                            ProductUpdateOfferIdRequestItem(
                                offer_id="old-article-123",
                                new_offer_id="new-article-456"
                            ),
                            ProductUpdateOfferIdRequestItem(
                                offer_id="old-article-789",
                                new_offer_id="new-article-012"
                            ),
                        ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/update/offer-id",
            json=request.model_dump(),
        )
        return ProductUpdateOfferIdResponse(**response)