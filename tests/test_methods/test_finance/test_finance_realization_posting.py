import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceRealizationPostingRequest,
    FinanceRealizationPostingResponse,
)


class TestFinanceRealizationPosting:
    """Тесты для метода finance_realization_posting."""

    @pytest.mark.asyncio
    async def test_finance_realization_posting(self, api, mock_api_request):
        """Тестирует метод finance_realization_posting."""

        mock_api_request.return_value = {
            "header": {"number": "987", "currency_sys_name": "RUB"},
            "rows": [
                {
                    "row_number": 1,
                    "item": {"sku": 222, "offer_id": "art-2"},
                    "order": {"posting_number": "0001-1", "created_date": "2026-04-10"},
                    "legal_entity_document": {"number": "ф-1", "sale_date": "2026-04-11"},
                }
            ],
        }

        request = FinanceRealizationPostingRequest(month=4, year=2026)

        response = await api.finance_realization_posting(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/realization/posting",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceRealizationPostingResponse)
        assert response.header.number == "987"
        assert response.rows[0].order.posting_number == "0001-1"
        assert response.rows[0].legal_entity_document.number == "ф-1"
