import aiohttp

from ...core import APIManager
from ...schemas.receipts import (
    ReceiptsUploadRequest,
    ReceiptsUploadResponse,
)


class ReceiptsUploadMixin(APIManager):
    """Реализует метод /v1/receipts/upload"""

    async def receipts_upload(
            self: "ReceiptsUploadMixin",
            request: ReceiptsUploadRequest
    ) -> ReceiptsUploadResponse:
        """Загружает чек продавца.

        Notes:
            • Запрос отправляется как `multipart/form-data`: файл чека `content`
              и текстовые поля.
            • Чтобы изменить ранее загруженный чек, передайте его идентификатор
              в `parent_receipt_id`.
            • Значение `operation_type` берётся из метода `receipts_seller_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/UploadReceipt

        Args:
            request: Запрос на загрузку чека по схеме `ReceiptsUploadRequest`

        Returns:
            Идентификатор загруженного чека по схеме `ReceiptsUploadResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                with open("receipt.pdf", "rb") as f:
                    result = await api.receipts_upload(
                        ReceiptsUploadRequest(
                            content=f.read(),
                            operation_type="COMMODITY",
                            posting_numbers=["0001-1"],
                            receipt_number="RCPT-1",
                            type="INCOMING"
                        )
                    )
        """
        form_data = aiohttp.FormData()
        form_data.add_field(
            "content",
            request.content,
            filename="receipt",
            content_type="application/octet-stream",
        )
        form_data.add_field("operation_type", request.operation_type)
        form_data.add_field("receipt_number", request.receipt_number)
        form_data.add_field("type", request.type.value)
        if request.parent_receipt_id is not None:
            form_data.add_field("parent_receipt_id", request.parent_receipt_id)
        for posting_number in request.posting_numbers:
            form_data.add_field("posting_numbers", posting_number)

        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="receipts/upload",
            form_data=form_data
        )
        return ReceiptsUploadResponse(**response)
