import pytest

from src.ozonapi.seller.schemas.finance import (
    FinanceDocumentB2BSalesRequest,
    FinanceDocumentB2BSalesResponse,
)


class TestFinanceDocumentB2BSales:
    """Тесты для метода finance_document_b2b_sales."""

    @pytest.mark.asyncio
    async def test_finance_document_b2b_sales(self, api, mock_api_request):
        """Тестирует метод finance_document_b2b_sales."""

        mock_api_request.return_value = {"result": {"code": "b2b-42"}}

        request = FinanceDocumentB2BSalesRequest(date="2026-04", language="DEFAULT")

        response = await api.finance_document_b2b_sales(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="finance/document-b2b-sales",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FinanceDocumentB2BSalesResponse)
        assert response.result.code == "b2b-42"
