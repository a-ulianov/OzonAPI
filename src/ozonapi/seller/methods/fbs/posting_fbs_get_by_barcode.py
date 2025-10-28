from ...core import APIManager
from ...schemas.fbs import PostingFBSGetByBarcodeRequest, PostingFBSGetByBarcodeResponse


class PostingFBSGetByBarcodeMixin(APIManager):
    """Реализует метод /v2/posting/fbs/get-by-barcode"""

    async def posting_fbs_get_by_barcode(
            self: "PostingFBSGetByBarcodeMixin",
            request: PostingFBSGetByBarcodeRequest
    ) -> PostingFBSGetByBarcodeResponse:
        """Метод для получения информации об отправлении FBS по штрихкоду.

        Notes:
            • Штрихкод отправления можно получить с помощью методов posting_fbs_get(), posting_fbs_list(), posting_fbs_unfulfilled_list() в массиве barcodes
            • Метод возвращает основную информацию об отправлении: статус, данные о заказе, товары и штрихкоды.
            • Для получения дополнительных данных (финансовой информации, аналитики и т.д.) используйте метод posting_fbs_get().

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_GetFbsPostingByBarcode

        Args:
            request: Запрос на получение информации об отправлении по штрихкоду по схеме `PostingFBSGetByBarcodeRequest`

        Returns:
            Информация об отправлении FBS по схеме `PostingFBSGetByBarcodeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_get_by_barcode(
                    PostingFBSGetByBarcodeRequest(
                        barcode="20325804886000"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/get-by-barcode",
            payload=request.model_dump()
        )
        return PostingFBSGetByBarcodeResponse(**response["result"])
