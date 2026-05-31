import pytest

from src.ozonapi.seller.schemas.questions import QuestionCountResponse


class TestQuestionCount:
    """Тесты для метода question_count."""

    @pytest.mark.asyncio
    async def test_question_count(self, api, mock_api_request):
        """Тестирует метод question_count."""

        mock_api_request.return_value = {
            "all": 20, "new": 5, "viewed": 3, "processed": 10, "unprocessed": 7
        }

        response = await api.question_count()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/count",
            payload={}
        )

        assert isinstance(response, QuestionCountResponse)
        assert response.all == 20
        assert response.unprocessed == 7
