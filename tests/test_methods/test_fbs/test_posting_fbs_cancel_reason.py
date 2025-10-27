import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSCancelReasonResponse


class TestPostingFBSCancelReason:
    """Тесты для метода posting_fbs_cancel_reason."""

    @pytest.mark.asyncio
    async def test_posting_fbs_cancel_reason(self, api, mock_api_request):
        """Тестирует метод posting_fbs_cancel_reason."""

        mock_response_data = {
            "result": [
                {
                    "posting_number": "73837363-0010-3",
                    "reasons": [
                        {
                            "id": 352,
                            "title": "Товар закончился на складе продавца",
                            "type_id": "seller"
                        },
                        {
                            "id": 400,
                            "title": "Остался только бракованный товар",
                            "type_id": "seller"
                        },
                        {
                            "id": 402,
                            "title": "Другое (вина продавца)",
                            "type_id": "seller"
                        }
                    ]
                },
                {
                    "posting_number": "73837363-0011-3",
                    "reasons": [
                        {
                            "id": 665,
                            "title": "Покупатель не забрал заказ",
                            "type_id": "buyer"
                        },
                        {
                            "id": 667,
                            "title": "Заказ утерян службой доставки",
                            "type_id": "seller"
                        }
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v1__posting_fbs_cancel_reason import (
            PostingFBSCancelReasonRequest
        )

        request = PostingFBSCancelReasonRequest(
            related_posting_numbers=["73837363-0010-3", "73837363-0011-3"]
        )

        response = await api.posting_fbs_cancel_reason(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/cancel-reason",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSCancelReasonResponse)
        assert len(response.result) == 2

        first_posting = response.result[0]
        second_posting = response.result[1]

        assert first_posting.posting_number == "73837363-0010-3"
        assert len(first_posting.reasons) == 3

        first_reason = first_posting.reasons[0]
        second_reason = first_posting.reasons[1]
        third_reason = first_posting.reasons[2]

        assert first_reason.id_ == 352
        assert first_reason.title == "Товар закончился на складе продавца"
        assert first_reason.type_id == "seller"

        assert second_reason.id_ == 400
        assert second_reason.title == "Остался только бракованный товар"
        assert second_reason.type_id == "seller"

        assert third_reason.id_ == 402
        assert third_reason.title == "Другое (вина продавца)"
        assert third_reason.type_id == "seller"

        assert second_posting.posting_number == "73837363-0011-3"
        assert len(second_posting.reasons) == 2

        fourth_reason = second_posting.reasons[0]
        fifth_reason = second_posting.reasons[1]

        assert fourth_reason.id_ == 665
        assert fourth_reason.title == "Покупатель не забрал заказ"
        assert fourth_reason.type_id == "buyer"

        assert fifth_reason.id_ == 667
        assert fifth_reason.title == "Заказ утерян службой доставки"
        assert fifth_reason.type_id == "seller"
