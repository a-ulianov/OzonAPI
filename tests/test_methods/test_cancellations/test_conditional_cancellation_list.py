import pytest

from src.ozonapi.seller.schemas.cancellations import (
    ConditionalCancellationListRequest,
    ConditionalCancellationListResponse,
)


class TestConditionalCancellationList:
    """Тесты для метода conditional_cancellation_list."""

    @pytest.mark.asyncio
    async def test_conditional_cancellation_list(self, api, mock_api_request):
        """Тестирует метод conditional_cancellation_list."""

        mock_api_request.return_value = {
            "counter": 1,
            "last_id": 50,
            "result": [
                {
                    "cancellation_id": 123,
                    "cancellation_initiator": "CLIENT",
                    "cancellation_reason": {"id": 1, "name": "Передумал"},
                    "posting_number": "0001-1",
                    "source_id": 7,
                    "state": {"id": 2, "name": "На рассмотрении", "state": "ON_APPROVAL"},
                    "tpl_integration_type": "ozon",
                }
            ],
        }

        request = ConditionalCancellationListRequest(
            limit=100,
            filters={"state": "ON_APPROVAL", "cancellation_initiator": ["CLIENT"]},
            with_={"counter": True},
        )

        response = await api.conditional_cancellation_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="conditional-cancellation/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ConditionalCancellationListResponse)
        assert response.counter == 1
        assert response.result[0].cancellation_id == 123
        assert response.result[0].state.state == "ON_APPROVAL"
        # `with` reserved word serialised via alias
        assert "with" in request.model_dump(by_alias=True)
