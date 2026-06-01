from ...core import APIManager
from ...schemas.receipts import (
    ReceiptsGetRequest,
    ReceiptsGetResponse,
)


class ReceiptsGetMixin(APIManager):
    """Реализует метод /v1/receipts/get"""

    async def receipts_get(
            self: "ReceiptsGetMixin",
            request: ReceiptsGetRequest
    ) -> ReceiptsGetResponse:
        """Возвращает чек в формате PDF.

        Notes:
            • API возвращает JSON с полем `content` — содержимым PDF-файла в виде
              строки base64 (а не бинарным телом ответа).
            • Идентификатор чека `receipt_id` выдаёт метод `receipts_seller_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetReceipt

        Args:
            request: Запрос чека по схеме `ReceiptsGetRequest`

        Returns:
            PDF-файл с чеком по схеме `ReceiptsGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                import base64
                result = await api.receipts_get(
                    ReceiptsGetRequest(receipt_id="123")
                )
                with open("receipt.pdf", "wb") as f:
                    f.write(base64.b64decode(result.content))
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="receipts/get",
            payload=request.model_dump()
        )
        return ReceiptsGetResponse(**response)
