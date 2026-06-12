import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesDeleteV1Request,
    CargoesDeleteV1Response,
)


class TestCargoesDeleteV1:
    """Тесты для метода cargoes_delete_v1."""

    @pytest.mark.asyncio
    async def test_cargoes_delete_v1(self, api, mock_api_request):
        """Тестирует метод cargoes_delete_v1."""

        mock_api_request.return_value = {
            "operation_id": "op-del-1",
            "errors": {
                "cargo_error_reasons": [],
                "supply_error_reasons": [],
            },
        }

        request = CargoesDeleteV1Request(supply_id=123, cargo_ids=["1", "2"])

        response = await api.cargoes_delete_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/delete",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesDeleteV1Response)
        assert response.operation_id == "op-del-1"
