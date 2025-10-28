import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSProductChangeResponse


class TestPostingFBSProductChange:
    """Тесты для метода posting_fbs_product_change."""

    @pytest.mark.asyncio
    async def test_posting_fbs_product_change(self, api, mock_api_request):
        """Тестирует метод posting_fbs_product_change."""

        mock_response_data = {
            "result": "33920158-0006-1"
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_change import (
            PostingFBSProductChangeRequest,
            PostingFBSProductChangeRequestItem
        )

        request = PostingFBSProductChangeRequest(
            posting_number="33920158-0006-1",
            items=[
                PostingFBSProductChangeRequestItem(
                    sku=1231428352,
                    weight_real=0.3
                )
            ]
        )

        response = await api.posting_fbs_product_change(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/change",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSProductChangeResponse)
        assert response.result == "33920158-0006-1"
