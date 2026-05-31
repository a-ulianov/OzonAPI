import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    AssemblyFbsPostingListRequest,
    AssemblyFbsPostingListResponse,
)
from src.ozonapi.seller.schemas.fbs_delivery.v1__assembly_fbs_posting_list import (
    AssemblyFbsPostingListFilter,
)


class TestAssemblyFbsPostingList:
    """Тесты для метода assembly_fbs_posting_list."""

    @pytest.mark.asyncio
    async def test_assembly_fbs_posting_list(self, api, mock_api_request):
        """Тестирует метод assembly_fbs_posting_list."""

        mock_response_data = {
            "cursor": "next",
            "cutoff": "2026-06-01T18:00:00Z",
            "postings": [
                {
                    "assembly_code": "AC-9",
                    "posting_number": "33920113-1231-1",
                    "products": [
                        {"offer_id": "ART-1", "product_name": "Товар", "quantity": 1, "sku": 987654}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = AssemblyFbsPostingListRequest(
            filter=AssemblyFbsPostingListFilter(delivery_method_id=999),
            limit=100,
            sort_dir="ASC"
        )

        response = await api.assembly_fbs_posting_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="assembly/fbs/posting/list",
            payload=request.model_dump()
        )

        assert isinstance(response, AssemblyFbsPostingListResponse)
        assert response.cutoff == "2026-06-01T18:00:00Z"
        assert response.postings[0].products[0].offer_id == "ART-1"
