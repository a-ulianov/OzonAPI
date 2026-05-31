import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    AssemblyCarriagePostingListRequest,
    AssemblyCarriagePostingListResponse,
)
from src.ozonapi.seller.schemas.fbs_delivery.v1__assembly_carriage_posting_list import (
    AssemblyCarriagePostingListFilter,
)


class TestAssemblyCarriagePostingList:
    """Тесты для метода assembly_carriage_posting_list."""

    @pytest.mark.asyncio
    async def test_assembly_carriage_posting_list(self, api, mock_api_request):
        """Тестирует метод assembly_carriage_posting_list."""

        mock_response_data = {
            "can_print_mass_label": True,
            "cursor": "next",
            "postings": [
                {
                    "assembly_code": "AC-1",
                    "can_print_label": True,
                    "posting_number": "33920113-1231-1",
                    "products": [
                        {"offer_id": "ART-1", "product_name": "Товар", "quantity": 2, "sku": 987654}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = AssemblyCarriagePostingListRequest(
            filter=AssemblyCarriagePostingListFilter(carriage_id=12345),
            limit=100
        )

        response = await api.assembly_carriage_posting_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="assembly/carriage/posting/list",
            payload=request.model_dump()
        )

        assert isinstance(response, AssemblyCarriagePostingListResponse)
        assert response.postings[0].posting_number == "33920113-1231-1"
        assert response.postings[0].products[0].sku == 987654
