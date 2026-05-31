import pytest

from src.ozonapi.seller.schemas.questions import QuestionListRequest, QuestionListResponse


class TestQuestionList:
    """Тесты для метода question_list."""

    @pytest.mark.asyncio
    async def test_question_list(self, api, mock_api_request):
        """Тестирует метод question_list."""

        mock_response_data = {
            "has_next": False,
            "last_id": "",
            "questions": [
                {"id": "q-1", "sku": 987654, "text": "Вопрос?", "status": "NEW", "answers_count": 0}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = QuestionListRequest(limit=100)

        response = await api.question_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/list",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionListResponse)
        assert response.questions[0].id == "q-1"
        assert response.questions[0].status == "NEW"
