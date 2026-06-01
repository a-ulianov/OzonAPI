import pytest

from src.ozonapi.seller.schemas.rfbs_delivery import (
    PostingFbsTimeslotChangeRestrictionsRequest,
    PostingFbsTimeslotChangeRestrictionsResponse,
)


class TestPostingFbsTimeslotChangeRestrictions:
    """Тесты для метода posting_fbs_timeslot_change_restrictions."""

    @pytest.mark.asyncio
    async def test_posting_fbs_timeslot_change_restrictions(self, api, mock_api_request):
        """Тестирует метод posting_fbs_timeslot_change_restrictions."""

        mock_api_request.return_value = {
            "delivery_interval": {
                "begin": "2026-06-01T00:00:00Z",
                "end": "2026-06-05T00:00:00Z",
            },
            "remaining_changes_count": 2,
        }

        request = PostingFbsTimeslotChangeRestrictionsRequest(
            posting_number="123-456-1"
        )

        response = await api.posting_fbs_timeslot_change_restrictions(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/timeslot/change-restrictions",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFbsTimeslotChangeRestrictionsResponse)
        assert response.remaining_changes_count == 2
        assert response.delivery_interval.begin == "2026-06-01T00:00:00Z"
