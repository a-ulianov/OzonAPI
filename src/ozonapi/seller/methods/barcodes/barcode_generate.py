from ...core import APIManager
from ...schemas.barcodes import BarcodeGenerateRequest, BarcodeGenerateResponse


class BarcodeGenerateMixin(APIManager):
    """Реализует метод /v1/barcode/generate"""

    async def barcode_generate(
        self: "BarcodeGenerateMixin",
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
            payload=request.model_dump(),
        )
        return BarcodeGenerateResponse(**response)
