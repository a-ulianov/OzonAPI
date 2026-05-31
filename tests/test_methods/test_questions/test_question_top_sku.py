import pytest

from src.ozonapi.seller.schemas.questions import QuestionTopSkuRequest, QuestionTopSkuResponse


class TestQuestionTopSku:
    """Тесты для метода question_top_sku."""

    @pytest.mark.asyncio
    async def test_question_top_sku(self, api, mock_api_request):
        """Тестирует метод question_top_sku."""

        mock_api_request.return_value = {"sku": [987654, 123456]}

        request = QuestionTopSkuRequest(limit=10)

        response = await api.question_top_sku(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="question/top-sku",
            payload=request.model_dump()
        )

        assert isinstance(response, QuestionTopSkuResponse)
        assert response.sku == [987654, 123456]
