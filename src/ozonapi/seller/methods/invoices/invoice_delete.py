from ...core import APIManager
from ...schemas.invoices import (
    InvoiceDeleteRequest,
    InvoiceDeleteResponse,
)


class InvoiceDeleteMixin(APIManager):
    """Реализует метод /v1/invoice/delete"""

    async def invoice_delete(
            self: "InvoiceDeleteMixin",
            request: InvoiceDeleteRequest
    ) -> InvoiceDeleteResponse:
        """Удаляет ссылку на счёт-фактуру отправления.

        Notes:
            • Удаляет ранее созданный счёт-фактуру для указанного отправления.

        References:
            https://docs.ozon.ru/api/seller/#operation/invoice_delete

        Args:
            request: Запрос на удаление ссылки на счёт-фактуру по схеме
                `InvoiceDeleteRequest`

        Returns:
            Результат обработки запроса по схеме `InvoiceDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.invoice_delete(
                    InvoiceDeleteRequest(posting_number="0001-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="invoice/delete",
            payload=request.model_dump()
        )
        return InvoiceDeleteResponse(**response)
