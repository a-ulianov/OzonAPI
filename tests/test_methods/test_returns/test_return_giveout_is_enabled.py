import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutIsEnabledResponse


class TestReturnGiveoutIsEnabled:
    """Тесты для метода return_giveout_is_enabled."""

    @pytest.mark.asyncio
    async def test_return_giveout_is_enabled(self, api, mock_api_request):
        """Тестирует метод return_giveout_is_enabled."""

        mock_api_request.return_value = {"enabled": True}

        response = await api.return_giveout_is_enabled()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/is-enabled",
            payload={}
        )

        assert isinstance(response, ReturnGiveoutIsEnabledResponse)
        assert response.enabled is True
