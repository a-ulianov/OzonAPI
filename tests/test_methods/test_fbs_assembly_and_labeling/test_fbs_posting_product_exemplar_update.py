import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarUpdateResponse


class TestFBSPostingProductExemplarUpdate:
    """Тесты для метода fbs_posting_product_exemplar_update."""

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_update(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_update."""

        mock_response_data = {}
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            FBSPostingProductExemplarUpdateRequest
        )

        request = FBSPostingProductExemplarUpdateRequest(
            posting_number="43658312-0011-1"
        )

        response = await api.fbs_posting_product_exemplar_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbs/posting/product/exemplar/update",
            payload=request.model_dump()
        )

        assert isinstance(response, FBSPostingProductExemplarUpdateResponse)