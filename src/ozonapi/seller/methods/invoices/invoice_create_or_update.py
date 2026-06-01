from ...core import APIManager
from ...schemas.invoices import (
    InvoiceCreateOrUpdateRequest,
    InvoiceCreateOrUpdateResponse,
)


class InvoiceCreateOrUpdateMixin(APIManager):
    """Реализует метод /v2/invoice/create-or-update"""

    async def invoice_create_or_update(
            self: "InvoiceCreateOrUpdateMixin",
            request: InvoiceCreateOrUpdateRequest
    ) -> InvoiceCreateOrUpdateResponse:
        """Создаёт или изменяет счёт-фактуру для отправления.

        Notes:
            • Счёт-фактура нужна для отправлений с таможенным оформлением (экспорт).
            • Ссылку на файл `url` предварительно создайте методом `invoice_file_upload()`.
            • Поле `date` передаётся строкой в формате RFC3339.

        References:
            https://docs.ozon.ru/api/seller/#operation/InvoiceAPI_InvoiceCreateOrUpdateV2

        Args:
            request: Запрос на создание/изменение счёта-фактуры по схеме
                `InvoiceCreateOrUpdateRequest`

        Returns:
            Результат обработки запроса по схеме `InvoiceCreateOrUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.invoice_create_or_update(
                    InvoiceCreateOrUpdateRequest(
                        date="2026-06-01T00:00:00Z",
                        posting_number="0001-1",
                        url="https://cdn.ozone.ru/invoice.pdf",
                        number="INV-1",
                        price=199.99,
                        price_currency="USD"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="invoice/create-or-update",
            payload=request.model_dump()
        )
        return InvoiceCreateOrUpdateResponse(**response)
