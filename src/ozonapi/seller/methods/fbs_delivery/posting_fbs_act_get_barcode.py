from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActGetBarcodeRequest,
    PostingFBSActGetBarcodeResponse,
)


class PostingFBSActGetBarcodeMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/get-barcode"""

    async def posting_fbs_act_get_barcode(
            self: "PostingFBSActGetBarcodeMixin",
            request: PostingFBSActGetBarcodeRequest
    ) -> PostingFBSActGetBarcodeResponse:
        """Метод для получения штрихкода для отгрузки отправления.

        Notes:
            • Возвращает PNG-изображение штрихкода; содержимое в поле `content` в виде байтов.
            • Текстовое значение штрихкода доступно методом `posting_fbs_act_get_barcode_text()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetBarcode

        Args:
            request: Запрос на получение штрихкода по схеме `PostingFBSActGetBarcodeRequest`

        Returns:
            PNG-изображение штрихкода по схеме `PostingFBSActGetBarcodeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_get_barcode(
                    PostingFBSActGetBarcodeRequest(
                        id=12345
                    )
                )
                with open("barcode.png", "wb") as f:
                    f.write(result.content)
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-barcode",
            payload=request.model_dump(),
            response_format="binary"
        )
        return PostingFBSActGetBarcodeResponse(**response)
