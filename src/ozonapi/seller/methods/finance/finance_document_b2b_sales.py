from ...core import APIManager
from ...schemas.finance import (
    FinanceDocumentB2BSalesRequest,
    FinanceDocumentB2BSalesResponse,
)


class FinanceDocumentB2BSalesMixin(APIManager):
    """Реализует метод /v1/finance/document-b2b-sales"""

    async def finance_document_b2b_sales(
            self: "FinanceDocumentB2BSalesMixin",
            request: FinanceDocumentB2BSalesRequest
    ) -> FinanceDocumentB2BSalesResponse:
        """Запускает формирование отчёта по продажам юридическим лицам.

        Notes:
            • Возвращает код отчёта; готовый документ доступен после генерации.
            • Для получения данных в JSON используйте `finance_document_b2b_sales_json`.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_CreateDocumentB2BSalesReport

        Args:
            request: Запрос на создание отчёта по схеме `FinanceDocumentB2BSalesRequest`

        Returns:
            Код отчёта по схеме `FinanceDocumentB2BSalesResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_document_b2b_sales(
                    FinanceDocumentB2BSalesRequest(date="2026-04", language="DEFAULT")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/document-b2b-sales",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceDocumentB2BSalesResponse(**response)
