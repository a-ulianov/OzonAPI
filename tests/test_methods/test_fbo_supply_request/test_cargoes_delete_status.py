import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesDeleteStatusRequest,
    CargoesDeleteStatusResponse,
)


class TestCargoesDeleteStatus:
    """Тесты для метода cargoes_delete_status."""

    @pytest.mark.asyncio
    async def test_cargoes_delete_status(self, api, mock_api_request):
        """Тестирует метод cargoes_delete_status."""

        mock_api_request.return_value = {
            "errors": {
                "cargo_error_reasons": [],
                "supply_error_reasons": [],
            },
            "status": "SUCCESS",
        }

        request = CargoesDeleteStatusRequest(operation_id="op-del-1")

        response = await api.cargoes_delete_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesDeleteStatusResponse)
        assert response.status == "SUCCESS"
