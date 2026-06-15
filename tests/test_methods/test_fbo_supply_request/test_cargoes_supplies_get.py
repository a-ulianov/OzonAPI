import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesSuppliesGetRequest,
    CargoesSuppliesGetResponse,
)


class TestCargoesSuppliesGet:
    """Тесты для метода cargoes_supplies_get."""

    @pytest.mark.asyncio
    async def test_cargoes_supplies_get(self, api, mock_api_request):
        """Тестирует метод cargoes_supplies_get."""

        mock_api_request.return_value = {
            "not_found_supply_ids": [],
            "supplies_cargoes": [
                {
                    "supply_id": 123,
                    "bundle_id": "b-1",
                    "cargoes_without_transport_cargoes": [
                        {"cargo_id": 1, "barcode": "X", "bundle_id": "b-1"}
                    ],
                    "transport_cargoes": [
                        {
                            "transport_cargo_id": 10,
                            "type": "PALLET",
                            "bundle_id": "b-2",
                            "cargoes": [],
                        }
                    ],
                }
            ],
        }

        request = CargoesSuppliesGetRequest(supply_ids=["123"])

        response = await api.cargoes_supplies_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/supplies/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesSuppliesGetResponse)
        assert response.supplies_cargoes[0].supply_id == 123
        assert response.supplies_cargoes[0].transport_cargoes[0].transport_cargo_id == 10
