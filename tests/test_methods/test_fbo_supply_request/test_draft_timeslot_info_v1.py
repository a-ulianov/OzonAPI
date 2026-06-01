import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftTimeslotInfoV1Request,
    DraftTimeslotInfoV1Response,
)


class TestDraftTimeslotInfoV1:
    """Тесты для метода draft_timeslot_info_v1."""

    @pytest.mark.asyncio
    async def test_draft_timeslot_info_v1(self, api, mock_api_request):
        """Тестирует метод draft_timeslot_info_v1."""

        mock_api_request.return_value = {
            "drop_off_warehouse_timeslots": [
                {
                    "current_time_in_timezone": "2026-06-01T12:00:00+03:00",
                    "drop_off_warehouse_id": 100,
                    "warehouse_timezone": "Europe/Moscow",
                    "days": [
                        {
                            "date_in_timezone": "2026-06-02",
                            "timeslots": [
                                {
                                    "from_in_timezone": "2026-06-02T09:00:00+03:00",
                                    "to_in_timezone": "2026-06-02T12:00:00+03:00",
                                }
                            ],
                        }
                    ],
                }
            ],
            "requested_date_from": "2026-06-01",
            "requested_date_to": "2026-06-07",
        }

        request = DraftTimeslotInfoV1Request(
            draft_id=123456,
            warehouse_ids=["100"],
            date_from="2026-06-01T00:00:00Z",
            date_to="2026-06-07T00:00:00Z",
        )

        response = await api.draft_timeslot_info_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/timeslot/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftTimeslotInfoV1Response)
        wh = response.drop_off_warehouse_timeslots[0]
        assert wh.drop_off_warehouse_id == 100
        assert wh.days[0].timeslots[0].to_in_timezone == "2026-06-02T12:00:00+03:00"
