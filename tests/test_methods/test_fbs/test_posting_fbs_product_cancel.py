import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSProductCancelResponse


class TestPostingFBSProductCancel:
    """Тесты для метода posting_fbs_product_cancel."""

    @pytest.mark.asyncio
    async def test_posting_fbs_product_cancel(self, api, mock_api_request):
        """Тестирует метод posting_fbs_product_cancel."""

        mock_response_data = {
            "result": "33920113-1231-1"
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_product_cancel import (
            PostingFBSProductCancelRequest,
            PostingFBSProductCancelItem
        )

        request = PostingFBSProductCancelRequest(
            cancel_reason_id=352,
            cancel_reason_message="Product is out of stock",
            items=[
                PostingFBSProductCancelItem(
                    quantity=5,
                    sku=150587396
                )
            ],
            posting_number="33920113-1231-1"
        )

        response = await api.posting_fbs_product_cancel(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/cancel",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSProductCancelResponse)
        assert response.result == "33920113-1231-1"
