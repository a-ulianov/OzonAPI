import pytest

from src.ozonapi.seller.schemas.passes import (
    ReturnPassDeleteRequest,
    ReturnPassDeleteResponse,
)


class TestReturnPassDelete:
    """Тесты для метода return_pass_delete."""

    @pytest.mark.asyncio
    async def test_return_pass_delete(self, api, mock_api_request):
        """Тестирует метод return_pass_delete."""

        mock_api_request.return_value = {}

        request = ReturnPassDeleteRequest(arrival_pass_ids=[456, 789])

        response = await api.return_pass_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/pass/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnPassDeleteResponse)
