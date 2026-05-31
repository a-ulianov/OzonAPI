from ...core import APIManager
from ...schemas.returns import ReturnGiveoutGetPDFResponse


class ReturnGiveoutGetPDFMixin(APIManager):
    """Реализует метод /v1/return/giveout/get-pdf"""

    async def return_giveout_get_pdf(
            self: "ReturnGiveoutGetPDFMixin"
    ) -> ReturnGiveoutGetPDFResponse:
        """Метод для получения штрихкода возвратной отгрузки в формате PDF.

        Notes:
            • API возвращает JSON с полем `pdf` — содержимым PDF-файла в виде строки (base64).
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutGetPDF

        Returns:
            PDF-файл со штрихкодом по схеме `ReturnGiveoutGetPDFResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_get_pdf()
                # result.pdf — строка base64 с содержимым PDF
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/get-pdf",
            payload={}
        )
        return ReturnGiveoutGetPDFResponse(**response)
