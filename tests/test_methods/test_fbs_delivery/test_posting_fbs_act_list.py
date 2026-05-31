import pytest

from src.ozonapi.seller.schemas.fbs_delivery import PostingFBSActListRequest, PostingFBSActListResponse
from src.ozonapi.seller.schemas.fbs_delivery.v2__posting_fbs_act_list import PostingFBSActListFilter


class TestPostingFBSActList:
    """Тесты для метода posting_fbs_act_list."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_list(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_list."""

        mock_response_data = {
            "result": [
                {
                    "id": 12345,
                    "delivery_method_id": 999,
                    "status": "awaiting_deliver",
                    "containers_count": 2,
                    "related_docs": {
                        "act_of_acceptance": {"created_at": "2026-06-01T10:00:00Z", "document_status": "FORMED"},
                        "act_of_mismatch": {"created_at": None, "document_status": "FORMING"}
                    }
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActListRequest(
            limit=100,
            filter=PostingFBSActListFilter(status=["awaiting_deliver"])
        )

        response = await api.posting_fbs_act_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/list",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSActListResponse)
        assert response.result[0].id == 12345
        assert response.result[0].related_docs.act_of_acceptance.document_status == "FORMED"
