import pytest

from src.ozonapi.seller.schemas.rfbs_delivery import (
    PostingFbsTimeslotSetNewTimeslot,
    PostingFbsTimeslotSetRequest,
    PostingFbsTimeslotSetResponse,
)


class TestPostingFbsTimeslotSet:
    """Тесты для метода posting_fbs_timeslot_set."""

    @pytest.mark.asyncio
    async def test_posting_fbs_timeslot_set(self, api, mock_api_request):
        """Тестирует метод posting_fbs_timeslot_set."""

        mock_api_request.return_value = {"result": True}

        request = PostingFbsTimeslotSetRequest(
            posting_number="123-456-1",
            new_timeslot=PostingFbsTimeslotSetNewTimeslot(
                from_="2026-06-02T00:00:00Z", to_="2026-06-03T00:00:00Z"
            ),
        )

        response = await api.posting_fbs_timeslot_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/timeslot/set",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFbsTimeslotSetResponse)
        assert response.result is True
        payload = request.model_dump(by_alias=True)
        assert "from" in payload["new_timeslot"] and "to" in payload["new_timeslot"]
