from ...core import APIManager
from ...schemas.finance import (
    FinanceDocumentB2BSalesJSONRequest,
    FinanceDocumentB2BSalesJSONResponse,
)


class FinanceDocumentB2BSalesJSONMixin(APIManager):
    """Реализует метод /v1/finance/document-b2b-sales/json"""

    async def finance_document_b2b_sales_json(
            self: "FinanceDocumentB2BSalesJSONMixin",
            request: FinanceDocumentB2BSalesJSONRequest
    ) -> FinanceDocumentB2BSalesJSONResponse:
        """Возвращает отчёт по продажам юридическим лицам в формате JSON.

        Notes:
            • В отличие от `finance_document_b2b_sales`, сразу возвращает данные:
              счета-фактуры с операциями, реквизиты покупателей и продавца.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_CreateDocumentB2BSalesJSONReport

        Args:
            request: Запрос отчёта по схеме `FinanceDocumentB2BSalesJSONRequest`

        Returns:
            Отчёт по продажам юр. лицам по схеме `FinanceDocumentB2BSalesJSONResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_document_b2b_sales_json(
                    FinanceDocumentB2BSalesJSONRequest(date="2026-04")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/document-b2b-sales/json",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceDocumentB2BSalesJSONResponse(**response)
