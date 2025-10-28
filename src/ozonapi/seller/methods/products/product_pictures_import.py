from ...core import APIManager
from ...schemas.products import ProductPicturesImportRequest, ProductPicturesImportResponse


class ProductPicturesImportMixin(APIManager):
    """Реализует метод /v1/product/pictures/import"""

    async def product_pictures_import(
        self: "ProductPicturesImportMixin",
        request: ProductPicturesImportRequest
    ) -> ProductPicturesImportResponse:
        """Загружает или обновляет изображения товара.

        Notes:
            • При каждом вызове метода передавайте все изображения, которые должны быть на карточке товара.
              Например, если вы вызвали метод и загрузили 10 изображений, а затем вызвали метод второй раз
              и загрузили ещё одно, то все 10 предыдущих сотрутся.
            • Для загрузки передайте адрес ссылки на изображение в общедоступном облачном хранилище.
              Формат изображения по ссылке — JPG или PNG.
            • Изображения в массиве `images` располагайте в соответствии с желаемым порядком на сайте.
              Главным будет первое изображение в массиве.
            • Для каждого товара вы можете загрузить до `30` изображений.
            • Для загрузки изображений 360 используйте поле `images360`, для загрузки маркетингового цвета — `color_image`.
            • Если вы хотите изменить состав или порядок изображений, получите информацию с помощью метода
              `product_info_list()` — в нём отображается текущий порядок и состав изображений. Скопируйте
              данные полей `images`, `images360`, `color_image`, измените и дополните состав или порядок
              в соответствии с необходимостью.
            • В ответе метода всегда будет статус `imported` — картинка не обработана. Чтобы посмотреть
              финальный статус, примерно через 10 секунд вызовите метод `product_pictures_info()`.
              `* Примечание: Видимо, артефакт в документации, т.к. по факту метод product_pictures_info() не возвращает статусы.`
            • Финальные статусы загрузки изображений:
                - `uploaded` — изображение загружено;
                - `pending` — при загрузке изображения возникла ошибка. Повторите попытку позже.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductImportPictures

        Args:
            request: Данные для загрузки изображений товара по схеме `ProductPicturesImportRequest`.

        Returns:
            Результат загрузки изображений с временными статусами по схеме `ProductPicturesImportResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_pictures_import(
                    ProductPicturesImportRequest(
                        product_id=123456789,
                        color_image="https://example.com/color.jpg",
                        images=[
                            "https://example.com/image1.jpg",
                            "https://example.com/image2.jpg",
                            "https://example.com/image3.jpg",
                        ],
                        images360=[
                            "https://example.com/360_1.jpg",
                            "https://example.com/360_2.jpg",
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/pictures/import",
            payload=request.model_dump(),
        )
        return ProductPicturesImportResponse(**response)
