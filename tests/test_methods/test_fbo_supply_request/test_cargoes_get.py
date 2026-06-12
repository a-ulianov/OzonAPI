import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesGetRequest,
    CargoesGetResponse,
    CargoesGetSupplyRequest,
)


class TestCargoesGet:
    """Тесты для метода cargoes_get (v2)."""

    @pytest.mark.asyncio
    async def test_cargoes_get(self, api, mock_api_request):
        """Тестирует метод cargoes_get."""

        mock_api_request.return_value = {
            "supplies": [
                {
                    "bundle_id": "b1",
                    "supply_id": 123,
                    "cargoes_bundle_id": "cb1",
                    "limits": {
                        "max_box_count": 10,
                        "max_pallet_count": 2,
                    },
                    "cargoes": [
                        {
                            "cargo_id": 1,
                            "content_type": "MONO",
                            "placement_zone_type": "TYPE_SINGLE",
                            "type": "BOX",
                            "transport_cargo_id": 10,
                            "tracking_info": {
                                "status": "ON_WAREHOUSE",
                                "type": "ACTUAL_ARRIVAL",
                                "arrival_at": {
                                    "date": "2026-06-01T00:00:00Z",
                                    "timezone_info": {
                                        "iana_name": "Europe/Moscow",
                                        "offset": 10800,
                                    },
                                },
                            },
                        }
                    ],
                    "transport_cargoes": [
                        {
                            "transport_cargo_id": 10,
                            "type": "PALLET",
                            "box_count": 5,
                            "summary_bundle_id": "sb1",
                        }
                    ],
                }
            ]
        }

        request = CargoesGetRequest(
            supplies=[CargoesGetSupplyRequest(supply_id=123, cargo_ids=["1"])]
        )

        response = await api.cargoes_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="cargoes/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesGetResponse)
        assert response.supplies[0].supply_id == 123
        assert response.supplies[0].cargoes[0].cargo_id == 1
        assert response.supplies[0].transport_cargoes[0].transport_cargo_id == 10
