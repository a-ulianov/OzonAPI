import pytest

from src.ozonapi.seller.schemas.questions import (
    QuestionAnswerDeleteRequest,
    QuestionAnswerDeleteResponse,
)


class TestQuestionAnswerDelete:
    """Тесты для метода question_answer_delete."""

    @pytest.mark.asyncio
    async def test_question_answer_delete(self, api, mock_api_request):
        """Тестирует метод question_answer_delete."""

        mock_api_request.return_value = {}

        request = QuestionAnswerDeleteRequest(answer_id="a-1", sku=987654)

        response = await api.question_answer_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/answer/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionAnswerDeleteResponse)
