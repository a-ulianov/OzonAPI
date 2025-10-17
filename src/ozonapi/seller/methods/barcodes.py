from ..core import APIManager
from ..core.method_rate_limiter import method_rate_limit
from ..schemas.barcodes import BarcodeGenerateRequest, BarcodeGenerateResponse
from ..schemas.barcodes import BarcodeAddRequest, BarcodeAddResponse


class SellerBarcodeAPI(APIManager):
    """Реализует методы раздела Штрихкоды товаров.

    References:
        https://docs.ozon.ru/api/seller/#tag/BarcodeAPI
    """

    @method_rate_limit(limit_requests=20, interval_seconds=60)
    async def barcode_add(
        self: "SellerBarcodeAPI",
        request: BarcodeAddRequest
    ) -> BarcodeAddResponse:
        """Если у товара есть штрихкод, который не указан в системе Ozon, привяжите его с помощью этого метода.
        Если штрихкода нет, вы можете создать его через метод `barcode_generate()`.

        Notes:
            • За один запрос вы можете назначить штрихкод не больше чем на `100` товаров.
            • На одном товаре может быть до `100` штрихкодов.
            • С одного аккаунта продавца можно использовать метод не больше `20` раз в минуту.

        References:
            https://docs.ozon.ru/api/seller/#operation/add-barcode

        Args:
            request: Данные для добавления штрих-кодов по схеме `BarcodeAddRequest`

        Returns:
            Ответ с результатом добавления штрих-кодов по схеме `BarcodeAddResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                barcodes = [BarcodeAddItem.model_validate({"barcode": "4321012345678", "sku": 0}), ]

                result = await api.barcode_add(BarcodeAddRequest(barcodes=barcodes))
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="barcode/add",
            json=request.model_dump(),
        )
        return BarcodeAddResponse(**response)

    async def barcode_generate(
        self: "SellerBarcodeAPI",
        request: BarcodeGenerateRequest,
    ) -> BarcodeGenerateResponse:
        """Если у товара нет штрихкода, вы можете создать его с помощью этого метода.
        Если штрихкод уже есть, но он не указан в системе Ozon, вы можете привязать его через метод `barcode_add()`.

        Notes:
            • За один запрос вы можете создать штрихкоды не больше чем для `100` товаров.
            • С одного аккаунта продавца можно использовать метод не больше `20` раз в минуту.

        References:
            https://docs.ozon.ru/api/seller/#operation/generate-barcode

        Args:
            request: Массив с product_id для создания штрих-кодов по схеме `BarcodeGenerateRequest`

        Returns:
            Массив с описанием ошибок при создании штрихкодов по схеме `BarcodeGenerateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.barcode_generate(
                    BarcodeGenerateRequest(
                        product_ids=[12345, 67890, ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="barcode/generate",
            json=request.model_dump(),
        )
        return BarcodeGenerateResponse(**response)
