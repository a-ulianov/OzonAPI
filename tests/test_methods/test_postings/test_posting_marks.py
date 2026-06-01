import pytest

from src.ozonapi.seller.schemas.postings import (
    PostingMarksRequest,
    PostingMarksResponse,
)


class TestPostingMarks:
    """Тесты для метода posting_marks."""

    @pytest.mark.asyncio
    async def test_posting_marks(self, api, mock_api_request):
        """Тестирует метод posting_marks."""

        mock_api_request.return_value = {
            "invalid_postings": ["0003-1"],
            "issued_exemplars": [
                {
                    "exemplar_id": 100,
                    "mandatory_marks": ["010290000..."],
                    "posting_number": "0001-1",
                    "sku": 123456,
                }
            ],
            "non_issued_exemplars": [
                {
                    "exemplar_id": 101,
                    "posting_number": "0002-1",
                    "sku": 654321,
                }
            ],
        }

        request = PostingMarksRequest(posting_numbers=["0001-1", "0002-1", "0003-1"])

        response = await api.posting_marks(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/marks",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingMarksResponse)
        assert response.invalid_postings == ["0003-1"]
        assert response.issued_exemplars[0].exemplar_id == 100
        assert response.issued_exemplars[0].mandatory_marks == ["010290000..."]
        assert response.non_issued_exemplars[0].sku == 654321
