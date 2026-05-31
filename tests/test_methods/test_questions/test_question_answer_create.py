import pytest

from src.ozonapi.seller.schemas.questions import (
    QuestionAnswerCreateRequest,
    QuestionAnswerCreateResponse,
)


class TestQuestionAnswerCreate:
    """Тесты для метода question_answer_create."""

    @pytest.mark.asyncio
    async def test_question_answer_create(self, api, mock_api_request):
        """Тестирует метод question_answer_create."""

        mock_api_request.return_value = {"answer_id": "a-1"}

        request = QuestionAnswerCreateRequest(question_id="q-1", sku=987654, text="Да, совместим.")

        response = await api.question_answer_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/answer/create",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionAnswerCreateResponse)
        assert response.answer_id == "a-1"
