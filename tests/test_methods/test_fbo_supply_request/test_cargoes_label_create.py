import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesLabelCreateCargo,
    CargoesLabelCreateRequest,
    CargoesLabelCreateResponse,
)


class TestCargoesLabelCreate:
    """Тесты для метода cargoes_label_create."""

    @pytest.mark.asyncio
    async def test_cargoes_label_create(self, api, mock_api_request):
        """Тестирует метод cargoes_label_create."""

        mock_api_request.return_value = {
            "operation_id": "op-lbl-1",
            "errors": {"error_reasons": []},
        }

        request = CargoesLabelCreateRequest(
            supply_id=123, cargoes=[CargoesLabelCreateCargo(cargo_id=1)]
        )

        response = await api.cargoes_label_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes-label/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesLabelCreateResponse)
        assert response.operation_id == "op-lbl-1"
