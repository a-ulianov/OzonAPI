import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import CargoesLabelFileResponse


class TestCargoesLabelFile:
    """Тесты для метода cargoes_label_file."""

    @pytest.mark.asyncio
    async def test_cargoes_label_file(self, api, mock_api_request):
        """Тестирует метод cargoes_label_file."""

        mock_api_request.return_value = {"content": b"%PDF-1.4 fake"}

        response = await api.cargoes_label_file("guid-1")

        mock_api_request.assert_called_once_with(
            method="get",
            api_version="v1",
            endpoint="cargoes-label/file/guid-1",
            payload={},
            response_format="binary"
        )

        assert isinstance(response, CargoesLabelFileResponse)
        assert response.content == b"%PDF-1.4 fake"
