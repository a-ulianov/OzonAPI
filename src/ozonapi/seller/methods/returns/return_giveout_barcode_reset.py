from ...core import APIManager
from ...schemas.returns import ReturnGiveoutBarcodeResetResponse


class ReturnGiveoutBarcodeResetMixin(APIManager):
    """Реализует метод /v1/return/giveout/barcode-reset"""

    async def return_giveout_barcode_reset(
            self: "ReturnGiveoutBarcodeResetMixin"
    ) -> ReturnGiveoutBarcodeResetResponse:
        """Метод для генерации нового штрихкода возвратных отгрузок.

        Notes:
            • Генерирует новый штрихкод; API возвращает JSON с полем `png` —
              содержимым PNG-изображения в виде строки (base64).
            • Предыдущий штрихкод становится недействительным.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutBarcodeReset

        Returns:
            PNG-изображение нового штрихкода по схеме `ReturnGiveoutBarcodeResetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_barcode_reset()
                # result.png — строка base64 с содержимым PNG
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/barcode-reset",
            payload={}
        )
        return ReturnGiveoutBarcodeResetResponse(**response)
