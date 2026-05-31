from ...core import APIManager
from ...schemas.finance import (
    FinanceTransactionListRequest,
    FinanceTransactionListResponse,
)


class FinanceTransactionListMixin(APIManager):
    """Реализует метод /v3/finance/transaction/list"""

    async def finance_transaction_list(
            self: "FinanceTransactionListMixin",
            request: FinanceTransactionListRequest
    ) -> FinanceTransactionListResponse:
        """Возвращает постраничный список транзакций за период.

        Notes:
            • Фильтрация по периоду, типам операций, номеру отправления и типу начисления.
            • Пагинация — по номеру страницы (`page`) и размеру (`page_size`).

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_FinanceTransactionListV3

        Args:
            request: Запрос списка транзакций по схеме `FinanceTransactionListRequest`

        Returns:
            Список транзакций по схеме `FinanceTransactionListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_transaction_list(
                    FinanceTransactionListRequest(
                        filter=FinanceTransactionListFilter(
                            date=FinancePeriod(from_="2026-04-01T00:00:00.000Z",
                                               to="2026-04-30T23:59:59.999Z")
                        ),
                        page=1, page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="finance/transaction/list",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceTransactionListResponse(**response)
