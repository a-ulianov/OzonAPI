from ...core import APIManager
from ...schemas.products import ProductImportRequest, ProductImportResponse


class ProductImportMixin(APIManager):
    """Реализует метод /v3/product/import"""

    async def product_import(
        self: "ProductImportMixin",
        request: ProductImportRequest
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
            payload=request.model_dump(),
        )
        return ProductImportResponse(**response)
