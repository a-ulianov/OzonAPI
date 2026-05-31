from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActGetBarcodeTextRequest,
    PostingFBSActGetBarcodeTextResponse,
)


class PostingFBSActGetBarcodeTextMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/get-barcode/text"""

    async def posting_fbs_act_get_barcode_text(
            self: "PostingFBSActGetBarcodeTextMixin",
            request: PostingFBSActGetBarcodeTextRequest
    ) -> PostingFBSActGetBarcodeTextResponse:
        """Метод для получения значения штрихкода для отгрузки отправления.

        Notes:
            • Возвращает штрихкод перевозки в текстовом виде.
            • Изображение штрихкода доступно методом `posting_fbs_act_get_barcode()` (бинарный).

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetBarcodeText

        Args:
            request: Запрос на получение значения штрихкода по схеме `PostingFBSActGetBarcodeTextRequest`

        Returns:
            Значение штрихкода по схеме `PostingFBSActGetBarcodeTextResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_get_barcode_text(
                    PostingFBSActGetBarcodeTextRequest(
                        id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-barcode/text",
            payload=request.model_dump()
        )
        return PostingFBSActGetBarcodeTextResponse(**response)
