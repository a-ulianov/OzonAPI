import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    AssemblyCarriageProductListRequest,
    AssemblyCarriageProductListResponse,
)
from src.ozonapi.seller.schemas.fbs_delivery.v1__assembly_carriage_product_list import (
    AssemblyCarriageProductListFilter,
)


class TestAssemblyCarriageProductList:
    """Тесты для метода assembly_carriage_product_list."""

    @pytest.mark.asyncio
    async def test_assembly_carriage_product_list(self, api, mock_api_request):
        """Тестирует метод assembly_carriage_product_list."""

        mock_response_data = {
            "cursor": "next",
            "products": [
                {
                    "offer_id": "ART-1",
                    "product_name": "Товар",
                    "quantity": 3,
                    "sku": 987654,
                    "posting_numbers": ["33920113-1231-1", "33920113-1231-2"]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = AssemblyCarriageProductListRequest(
            filter=AssemblyCarriageProductListFilter(carriage_id=12345),
            limit=100
        )

        response = await api.assembly_carriage_product_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="assembly/carriage/product/list",
            payload=request.model_dump()
        )

        assert isinstance(response, AssemblyCarriageProductListResponse)
        assert response.products[0].sku == 987654
        assert response.products[0].posting_numbers == ["33920113-1231-1", "33920113-1231-2"]
