import pytest

from src.ozonapi.seller.schemas.questions import QuestionInfoRequest, QuestionInfoResponse


class TestQuestionInfo:
    """Тесты для метода question_info."""

    @pytest.mark.asyncio
    async def test_question_info(self, api, mock_api_request):
        """Тестирует метод question_info."""

        mock_response_data = {
            "id": "q-1",
            "sku": 987654,
            "text": "Совместим ли товар?",
            "author_name": "Покупатель",
            "answers_count": 1,
            "status": "PROCESSED"
        }
        mock_api_request.return_value = mock_response_data

        request = QuestionInfoRequest(question_id="q-1")

        response = await api.question_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/info",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionInfoResponse)
        assert response.id == "q-1"
        assert response.answers_count == 1
