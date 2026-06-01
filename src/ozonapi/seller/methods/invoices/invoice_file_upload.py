from ...core import APIManager
from ...schemas.invoices import (
    InvoiceFileUploadRequest,
    InvoiceFileUploadResponse,
)


class InvoiceFileUploadMixin(APIManager):
    """Реализует метод /v1/invoice/file/upload"""

    async def invoice_file_upload(
            self: "InvoiceFileUploadMixin",
            request: InvoiceFileUploadRequest
    ) -> InvoiceFileUploadResponse:
        """Загружает файл счёта-фактуры и возвращает ссылку на него.

        Notes:
            • Содержимое файла передаётся строкой в кодировке Base64 в поле `base64_content`.
            • Полученную ссылку `url` используйте в методе `invoice_create_or_update()`.
            • Поддерживаются файлы JPEG и PDF; ограничения по размеру — в документации Ozon.

        References:
            https://docs.ozon.ru/api/seller/#operation/invoice_upload

        Args:
            request: Запрос на загрузку счёта-фактуры по схеме `InvoiceFileUploadRequest`

        Returns:
            Ссылка на загруженный файл по схеме `InvoiceFileUploadResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                import base64
                with open("invoice.pdf", "rb") as f:
                    content = base64.b64encode(f.read()).decode()
                result = await api.invoice_file_upload(
                    InvoiceFileUploadRequest(
                        base64_content=content,
                        posting_number="0001-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="invoice/file/upload",
            payload=request.model_dump()
        )
        return InvoiceFileUploadResponse(**response)
