import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSProductTraceableAttributeRequest,
    PostingFBSProductTraceableAttributeResponse,
)


class TestPostingFBSProductTraceableAttribute:
    """Тесты для метода posting_fbs_product_traceable_attribute."""

    @pytest.mark.asyncio
    async def test_posting_fbs_product_traceable_attribute(self, api, mock_api_request):
        """Тестирует метод posting_fbs_product_traceable_attribute."""

        mock_response_data = {
            "products": [
                {"sku": 987654, "required_attributes": ["mark_code", "gtd"]}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSProductTraceableAttributeRequest(posting_number="33920113-1231-1")

        response = await api.posting_fbs_product_traceable_attribute(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/product/traceable/attribute",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSProductTraceableAttributeResponse)
        assert response.products[0].sku == 987654
        assert response.products[0].required_attributes == ["mark_code", "gtd"]
