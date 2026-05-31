import pytest

from src.ozonapi.seller.schemas.finance import (
    FinancePeriod,
    FinanceTransactionListFilter,
    FinanceTransactionListRequest,
    FinanceTransactionListResponse,
)


class TestFinanceTransactionList:
    """Тесты для метода finance_transaction_list."""

    @pytest.mark.asyncio
    async def test_finance_transaction_list(self, api, mock_api_request):
        """Тестирует метод finance_transaction_list."""

        mock_api_request.return_value = {
            "result": {
                "operations": [
                    {
                        "operation_id": 555,
                        "operation_type": "ClientReturnAgentOperation",
                        "amount": -120.5,
                        "items": [{"name": "Товар", "sku": 333}],
                        "posting": {"posting_number": "0002-1", "delivery_schema": "FBO"},
                        "services": [{"name": "MarketplaceServiceItem", "price": -5.0}],
                    }
                ],
                "page_count": 1,
                "row_count": 1,
            }
        }

        request = FinanceTransactionListRequest(
            filter=FinanceTransactionListFilter(
                date=FinancePeriod(
                    from_="2026-04-01T00:00:00.000Z", to="2026-04-30T23:59:59.999Z"
                )
            ),
            page=1,
            page_size=100,
        )

        response = await api.finance_transaction_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="finance/transaction/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceTransactionListResponse)
        assert response.result.row_count == 1
        assert response.result.operations[0].operation_id == 555
        assert response.result.operations[0].items[0].sku == 333
        assert response.result.operations[0].posting.delivery_schema == "FBO"
