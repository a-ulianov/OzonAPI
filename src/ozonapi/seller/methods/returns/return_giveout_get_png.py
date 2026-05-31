from ...core import APIManager
from ...schemas.returns import ReturnGiveoutGetPNGResponse


class ReturnGiveoutGetPNGMixin(APIManager):
    """Реализует метод /v1/return/giveout/get-png"""

    async def return_giveout_get_png(
            self: "ReturnGiveoutGetPNGMixin"
    ) -> ReturnGiveoutGetPNGResponse:
        """Метод для получения штрихкода возвратной отгрузки в формате PNG.

        Notes:
            • API возвращает JSON с полем `png` — содержимым PNG-изображения в виде строки (base64).
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutGetPNG

        Returns:
            PNG-изображение штрихкода по схеме `ReturnGiveoutGetPNGResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_get_png()
                # result.png — строка base64 с содержимым PNG
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/get-png",
            payload={}
        )
        return ReturnGiveoutGetPNGResponse(**response)
