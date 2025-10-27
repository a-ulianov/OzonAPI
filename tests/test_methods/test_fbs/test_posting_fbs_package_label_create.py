import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSPackageLabelCreateResponse


class TestPostingFBSPackageLabelCreate:
    """Тесты для метода posting_fbs_package_label_create."""

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label_create(self, api, mock_api_request):
        """Тестирует метод posting_fbs_package_label_create."""

        mock_response_data = {
            "result": {
                "tasks": [
                    {
                        "task_id": 5819327210248,
                        "task_type": "big_label"
                    },
                    {
                        "task_id": 5819327210249,
                        "task_type": "small_label"
                    }
                ]
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_package_label_create import (
            PostingFBSPackageLabelCreateRequest
        )

        request = PostingFBSPackageLabelCreateRequest(
            posting_number=["4708216109137", "3697105098026"]
        )

        response = await api.posting_fbs_package_label_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label/create",
            json=request.model_dump()
        )

        assert isinstance(response, PostingFBSPackageLabelCreateResponse)
        assert len(response.result.tasks) == 2

        first_task = response.result.tasks[0]
        second_task = response.result.tasks[1]

        assert first_task.task_id == 5819327210248
        assert first_task.task_type == "big_label"
        assert second_task.task_id == 5819327210249
        assert second_task.task_type == "small_label"
