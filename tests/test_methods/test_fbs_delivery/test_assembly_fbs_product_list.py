import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    AssemblyFbsProductListRequest,
    AssemblyFbsProductListResponse,
)
from src.ozonapi.seller.schemas.fbs_delivery.v1__assembly_fbs_product_list import (
    AssemblyFbsProductListFilter,
)


class TestAssemblyFbsProductList:
    """Тесты для метода assembly_fbs_product_list."""

    @pytest.mark.asyncio
    async def test_assembly_fbs_product_list(self, api, mock_api_request):
        """Тестирует метод assembly_fbs_product_list."""

        mock_response_data = {
            "has_next": False,
            "products_count": 1,
            "products": [
                {
                    "offer_id": "ART-1",
                    "product_name": "Товар",
                    "quantity": 5,
                    "sku": 987654,
                    "postings": [
                        {"posting_number": "33920113-1231-1", "quantity": 5}
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = AssemblyFbsProductListRequest(
            filter=AssemblyFbsProductListFilter(delivery_method_id=999),
            limit=100
        )

        response = await api.assembly_fbs_product_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="assembly/fbs/product/list",
            payload=request.model_dump()
        )

        assert isinstance(response, AssemblyFbsProductListResponse)
        assert response.products_count == 1
        assert response.products[0].postings[0].quantity == 5
