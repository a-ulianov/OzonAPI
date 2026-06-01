import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import CargoType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesCreateCargo,
    CargoesCreateCargoValue,
    CargoesCreateItem,
    CargoesCreateRequest,
    CargoesCreateResponse,
)


class TestCargoesCreate:
    """Тесты для метода cargoes_create."""

    @pytest.mark.asyncio
    async def test_cargoes_create(self, api, mock_api_request):
        """Тестирует метод cargoes_create."""

        mock_api_request.return_value = {
            "operation_id": "op-crg-1",
            "errors": {"error_reasons": [], "items_validation": []},
        }

        request = CargoesCreateRequest(
            supply_id=123,
            delete_current_version=True,
            cargoes=[
                CargoesCreateCargo(
                    key="c1",
                    value=CargoesCreateCargoValue(
                        type=CargoType.BOX,
                        items=[CargoesCreateItem(barcode="bc", quantity=1)],
                    ),
                )
            ],
        )

        response = await api.cargoes_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesCreateResponse)
        assert response.operation_id == "op-crg-1"
