from ...core import APIManager, method_rate_limit
from ...schemas.barcodes import BarcodeAddRequest, BarcodeAddResponse


class BarcodeAddMixin(APIManager):
    """Реализует метод /v1/barcode/add"""

    @method_rate_limit(limit_requests=20, interval_seconds=60)
    async def barcode_add(
        self: "BarcodeAddMixin",
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
            payload=request.model_dump(),
        )
        return BarcodeAddResponse(**response)
