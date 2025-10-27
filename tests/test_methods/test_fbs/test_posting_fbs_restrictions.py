import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSRestrictionsResponse


class TestPostingFBSRestrictions:
    """Тесты для метода posting_fbs_restrictions."""

    @pytest.mark.asyncio
    async def test_posting_fbs_restrictions(self, api, mock_api_request):
        """Тестирует метод posting_fbs_restrictions."""

        mock_response_data = {
            "result": {
                "posting_number": "76673629-0020-1",
                "max_posting_weight": 40000,
                "min_posting_weight": 0,
                "width": 500,
                "height": 500,
                "length": 500,
                "max_posting_price": 500000.0,
                "min_posting_price": 0.0
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_restrictions import (
            PostingFBSRestrictionsRequest
        )

        request = PostingFBSRestrictionsRequest(
            posting_number="76673629-0020-1"
        )

        response = await api.posting_fbs_restrictions(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/restrictions",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSRestrictionsResponse)
        assert response.posting_number == "76673629-0020-1"
        assert response.max_posting_weight == 40000
        assert response.min_posting_weight == 0
        assert response.width == 500
        assert response.height == 500
        assert response.length == 500
        assert response.max_posting_price == 500000.0
        assert response.min_posting_price == 0.0
