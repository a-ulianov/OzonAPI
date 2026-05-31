import pytest

from src.ozonapi.seller.schemas.questions import (
    QuestionAnswerListRequest,
    QuestionAnswerListResponse,
)


class TestQuestionAnswerList:
    """Тесты для метода question_answer_list."""

    @pytest.mark.asyncio
    async def test_question_answer_list(self, api, mock_api_request):
        """Тестирует метод question_answer_list."""

        mock_response_data = {
            "last_id": "",
            "answers": [
                {"id": "a-1", "question_id": "q-1", "sku": 987654, "text": "Ответ",
                 "author_name": "Продавец", "status_publication": "PUBLISHED"}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = QuestionAnswerListRequest(question_id="q-1", sku=987654)

        response = await api.question_answer_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/answer/list",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionAnswerListResponse)
        assert response.answers[0].id == "a-1"
        assert response.answers[0].status_publication == "PUBLISHED"
