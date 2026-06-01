from ...core import APIManager
from ...schemas.invoices import (
    InvoiceGetRequest,
    InvoiceGetResponse,
)


class InvoiceGetMixin(APIManager):
    """Реализует метод /v2/invoice/get"""

    async def invoice_get(
            self: "InvoiceGetMixin",
            request: InvoiceGetRequest
    ) -> InvoiceGetResponse:
        """Возвращает информацию о счёте-фактуре отправления.

        Notes:
            • Возвращает данные счёта-фактуры, созданного методом
              `invoice_create_or_update()`.
            • Если счёт-фактура для отправления не создан, `result` будет пустым.

        References:
            https://docs.ozon.ru/api/seller/#operation/invoice_getV2

        Args:
            request: Запрос информации о счёте-фактуре по схеме `InvoiceGetRequest`

        Returns:
            Информация о счёте-фактуре по схеме `InvoiceGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.invoice_get(
                    InvoiceGetRequest(posting_number="0001-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="invoice/get",
            payload=request.model_dump()
        )
        return InvoiceGetResponse(**response)
