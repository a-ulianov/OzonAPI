import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import PostingFBSShipPackageResponse


class TestPostingFBSShipPackage:
    """Тесты для метода posting_fbs_ship_package."""

    @pytest.mark.asyncio
    async def test_posting_fbs_ship_package(self, api, mock_api_request):
        """Тестирует метод posting_fbs_ship_package."""

        mock_response_data = {
            "result": "89491381-0072-2"
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            PostingFBSShipPackageRequest,
            PostingFBSShipPackageProduct
        )

        request = PostingFBSShipPackageRequest(
            posting_number="89491381-0072-1",
            products=[
                PostingFBSShipPackageProduct(
                    product_id="185479045",
                    quantity=1,
                    exemplars_ids=["12345"]
                ),
                PostingFBSShipPackageProduct(
                    product_id="185479046",
                    quantity=1,
                    exemplars_ids=["12347"]
                )
            ]
        )

        response = await api.posting_fbs_ship_package(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="posting/fbs/ship/package",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSShipPackageResponse)
        assert response.result == "89491381-0072-2"