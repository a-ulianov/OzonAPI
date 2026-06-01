import pytest

from src.ozonapi.seller.schemas.fbs import (
    PostingGlobalEtgbDate,
    PostingGlobalEtgbRequest,
    PostingGlobalEtgbResponse,
)


class TestPostingGlobalEtgb:
    """Тесты для метода posting_global_etgb."""

    @pytest.mark.asyncio
    async def test_posting_global_etgb(self, api, mock_api_request):
        """Тестирует метод posting_global_etgb."""

        mock_api_request.return_value = {
            "result": [
                {
                    "posting_number": "123-456-1",
                    "etgb": {
                        "number": "ETGB-1",
                        "date": "2026-05-15",
                        "url": "https://example/etgb.pdf",
                    },
                }
            ]
        }

        request = PostingGlobalEtgbRequest(
            date=PostingGlobalEtgbDate(
                from_="2026-05-01T00:00:00Z", to_="2026-06-01T00:00:00Z"
            )
        )

        response = await api.posting_global_etgb(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/global/etgb",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingGlobalEtgbResponse)
        assert response.result[0].etgb.number == "ETGB-1"
        payload = request.model_dump(by_alias=True)
        assert "from" in payload["date"] and "to" in payload["date"]
