import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSCancelReasonListResponse


class TestPostingFBSCancelReasonList:
    """Тесты для метода posting_fbs_cancel_reason_list."""

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel_reason_list(self, api, mock_api_request):
        """Тестирует метод posting_fbs_cancel_reason_list."""

        mock_response_data = {
            "result": [
                {
                    "id": 352,
                    "title": "Товар закончился на складе продавца",
                    "type_id": "seller",
                    "is_available_for_cancellation": True
                },
                {
                    "id": 401,
                    "title": "Продавец отклонил арбитраж",
                    "type_id": "seller",
                    "is_available_for_cancellation": False
                },
                {
                    "id": 402,
                    "title": "Другое (вина продавца)",
                    "type_id": "seller",
                    "is_available_for_cancellation": True
                },
                {
                    "id": 666,
                    "title": "Возврат из службы доставки: нет доставки в указанный регион",
                    "type_id": "seller",
                    "is_available_for_cancellation": False
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        response = await api.posting_fbs_cancel_reason_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/cancel-reason/list",
        )

        assert isinstance(response, PostingFBSCancelReasonListResponse)
        assert len(response.result) == 4

        first_reason = response.result[0]
        second_reason = response.result[1]
        third_reason = response.result[2]
        fourth_reason = response.result[3]

        assert first_reason.id_ == 352
        assert first_reason.title == "Товар закончился на складе продавца"
        assert first_reason.type_id == "seller"
        assert first_reason.is_available_for_cancellation is True

        assert second_reason.id_ == 401
        assert second_reason.title == "Продавец отклонил арбитраж"
        assert second_reason.type_id == "seller"
        assert second_reason.is_available_for_cancellation is False

        assert third_reason.id_ == 402
        assert third_reason.title == "Другое (вина продавца)"
        assert third_reason.type_id == "seller"
        assert third_reason.is_available_for_cancellation is True

        assert fourth_reason.id_ == 666
        assert fourth_reason.title == "Возврат из службы доставки: нет доставки в указанный регион"
        assert fourth_reason.type_id == "seller"
        assert fourth_reason.is_available_for_cancellation is False
