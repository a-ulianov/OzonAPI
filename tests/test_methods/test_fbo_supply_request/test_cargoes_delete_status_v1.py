import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesDeleteStatusV1Request,
    CargoesDeleteStatusV1Response,
)


class TestCargoesDeleteStatusV1:
    """Тесты для метода cargoes_delete_status_v1."""

    @pytest.mark.asyncio
    async def test_cargoes_delete_status_v1(self, api, mock_api_request):
        """Тестирует метод cargoes_delete_status_v1."""

        mock_api_request.return_value = {
            "errors": {
                "cargo_error_reasons": [],
                "supply_error_reasons": [],
            },
            "status": "SUCCESS",
        }

        request = CargoesDeleteStatusV1Request(operation_id="op-del-1")

        response = await api.cargoes_delete_status_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesDeleteStatusV1Response)
        assert response.status == "SUCCESS"
