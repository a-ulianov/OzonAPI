import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutGetPNGResponse


class TestReturnGiveoutGetPNG:
    """Тесты для метода return_giveout_get_png."""

    @pytest.mark.asyncio
    async def test_return_giveout_get_png(self, api, mock_api_request):
        """Тестирует метод return_giveout_get_png."""

        mock_api_request.return_value = {"png": "iVBORw0KGgo..."}

        response = await api.return_giveout_get_png()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/get-png",
            payload={}
        )

        assert isinstance(response, ReturnGiveoutGetPNGResponse)
        assert response.png == "iVBORw0KGgo..."
