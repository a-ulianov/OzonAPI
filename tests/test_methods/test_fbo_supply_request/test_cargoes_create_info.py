import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesCreateInfoRequest,
    CargoesCreateInfoResponse,
)


class TestCargoesCreateInfo:
    """Тесты для метода cargoes_create_info."""

    @pytest.mark.asyncio
    async def test_cargoes_create_info(self, api, mock_api_request):
        """Тестирует метод cargoes_create_info."""

        mock_api_request.return_value = {
            "errors": {"error_reasons": [], "items_validation": []},
            "result": {"cargoes": [{"key": "c1", "value": {"cargo_id": 555}}]},
            "status": "SUCCESS",
        }

        request = CargoesCreateInfoRequest(operation_id="op-crg-1")

        response = await api.cargoes_create_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="cargoes/create/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesCreateInfoResponse)
        assert response.status == "SUCCESS"
        assert response.result.cargoes[0].value.cargo_id == 555
