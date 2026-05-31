from ...core import APIManager
from ...schemas.reports import (
    FinanceCashFlowStatementListRequest,
    FinanceCashFlowStatementListResponse,
)


class FinanceCashFlowStatementListMixin(APIManager):
    """Реализует метод /v1/finance/cash-flow-statement/list"""

    async def finance_cash_flow_statement_list(
            self: "FinanceCashFlowStatementListMixin",
            request: FinanceCashFlowStatementListRequest
    ) -> FinanceCashFlowStatementListResponse:
        """Метод для получения финансового отчёта (отчёта о движении денежных средств).

        Notes:
            • Возвращает суммы реализации, возвратов, комиссий и услуг за период.
            • Постраничный вывод через `page` и `page_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceCashFlowStatementList

        Args:
            request: Запрос на получение финансового отчёта по схеме `FinanceCashFlowStatementListRequest`

        Returns:
            Финансовый отчёт по схеме `FinanceCashFlowStatementListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_cash_flow_statement_list(
                    FinanceCashFlowStatementListRequest(
                        date=FinanceCashFlowPeriod(from_="2026-01-01T00:00:00Z", to="2026-02-01T00:00:00Z"),
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/cash-flow-statement/list",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceCashFlowStatementListResponse(**response)
