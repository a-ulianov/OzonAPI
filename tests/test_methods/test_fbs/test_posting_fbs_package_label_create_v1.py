import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingFBSPackageLabelCreateV1Request,
    PostingFBSPackageLabelCreateV1Response,
)


class TestPostingFBSPackageLabelCreateV1:
    """Тесты для метода posting_fbs_package_label_create_v1."""

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label_create_v1(self, api, mock_api_request):
        """Тестирует метод posting_fbs_package_label_create_v1."""

        mock_api_request.return_value = {"result": {"task_id": 42}}

        request = PostingFBSPackageLabelCreateV1Request(posting_number=["123-456-1"])

        response = await api.posting_fbs_package_label_create_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/package-label/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSPackageLabelCreateV1Response)
        assert response.result.task_id == 42
