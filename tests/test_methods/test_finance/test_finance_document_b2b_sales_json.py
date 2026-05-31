import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceDocumentB2BSalesJSONRequest,
    FinanceDocumentB2BSalesJSONResponse,
)


class TestFinanceDocumentB2BSalesJSON:
    """Тесты для метода finance_document_b2b_sales_json."""

    @pytest.mark.asyncio
    async def test_finance_document_b2b_sales_json(self, api, mock_api_request):
        """Тестирует метод finance_document_b2b_sales_json."""

        mock_api_request.return_value = {
            "date_from": "2026-04-01",
            "date_to": "2026-04-30",
            "invoices": [
                {
                    "buyer_info": {"name": "ООО Покупатель", "inn": "7700000000"},
                    "currency": "RUB",
                    "info": {"number": "сф-1", "status": "SIGNED"},
                    "offer_id": "art-3",
                    "operations": [
                        {"amount": 200.0, "quantity": 2, "vat_rate": 20.0}
                    ],
                    "product_name": "Товар",
                    "sku": 444,
                }
            ],
            "seller_info": {"company_name": "ООО Продавец", "inn": "5000000000"},
        }

        request = FinanceDocumentB2BSalesJSONRequest(date="2026-04")

        response = await api.finance_document_b2b_sales_json(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/document-b2b-sales/json",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceDocumentB2BSalesJSONResponse)
        assert response.seller_info.company_name == "ООО Продавец"
        assert response.invoices[0].buyer_info.inn == "7700000000"
        assert response.invoices[0].operations[0].quantity == 2
