from ...core import APIManager
from ...schemas.returns import ReturnGiveoutBarcodeResponse


class ReturnGiveoutBarcodeMixin(APIManager):
    """Реализует метод /v1/return/giveout/barcode"""

    async def return_giveout_barcode(
            self: "ReturnGiveoutBarcodeMixin"
    ) -> ReturnGiveoutBarcodeResponse:
        """Метод для получения значения штрихкода для возвратных отгрузок.

        Notes:
            • Возвращает штрихкод возвратных отгрузок в текстовом виде.
            • Изображение штрихкода доступно методами `return_giveout_get_pdf()` / `return_giveout_get_png()`.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutBarcode

        Returns:
            Значение штрихкода по схеме `ReturnGiveoutBarcodeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_barcode()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/barcode",
            payload={}
        )
        return ReturnGiveoutBarcodeResponse(**response)
