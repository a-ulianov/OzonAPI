import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSPackageLabelGetResponse


class TestPostingFBSPackageLabelGet:
    """Тесты для метода posting_fbs_package_label_get."""

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label_get(self, api, mock_api_request):
        """Тестирует метод posting_fbs_package_label_get."""

        mock_response_data = {
            "result": {
                "error": "",
                "status": "completed",
                "file_url": "https://cdn1.ozone.ru/s3/ord-tmp-12/small_label/ticket-00-0000-0000.pdf",
                "printed_postings_count": 1,
                "unprinted_postings_count": 0,
                "unprinted_postings": []
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_package_label_get import (
            PostingFBSPackageLabelGetRequest
        )

        request = PostingFBSPackageLabelGetRequest(
            task_id=5819327210248
        )

        response = await api.posting_fbs_package_label_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/package-label/get",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSPackageLabelGetResponse)
        assert response.result.error == ""
        assert response.result.status == "completed"
        assert response.result.file_url == "https://cdn1.ozone.ru/s3/ord-tmp-12/small_label/ticket-00-0000-0000.pdf"
        assert response.result.printed_postings_count == 1
        assert response.result.unprinted_postings_count == 0
        assert response.result.unprinted_postings == []
