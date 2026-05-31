import pytest

from src.ozonapi.seller.schemas.questions import (
    QuestionChangeStatusRequest,
    QuestionChangeStatusResponse,
)


class TestQuestionChangeStatus:
    """Тесты для метода question_change_status."""

    @pytest.mark.asyncio
    async def test_question_change_status(self, api, mock_api_request):
        """Тестирует метод question_change_status."""

        mock_api_request.return_value = {}

        request = QuestionChangeStatusRequest(question_ids=["q-1"], status="PROCESSED")

        response = await api.question_change_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/change-status",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionChangeStatusResponse)
