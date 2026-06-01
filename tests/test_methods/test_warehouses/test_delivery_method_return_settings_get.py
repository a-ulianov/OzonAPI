import pytest

from src.ozonapi.seller.schemas.warehouses import (
    DeliveryMethodReturnSettingsRequest,
    DeliveryMethodReturnSettingsResponse,
)


class TestDeliveryMethodReturnSettingsGet:
    """Тесты для метода delivery_method_return_settings_get."""

    @pytest.mark.asyncio
    async def test_delivery_method_return_settings_get(self, api, mock_api_request):
        """Тестирует метод delivery_method_return_settings_get."""

        mock_api_request.return_value = {
            "settings": {
                "courier_details": {"contact_days": 3},
                "post_office_zipcode": "101000",
                "transport_company_details": {
                    "transport_company_names": ["СДЭК"],
                    "zipcode": "101000",
                },
            }
        }

        request = DeliveryMethodReturnSettingsRequest(delivery_method_id=123)

        response = await api.delivery_method_return_settings_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="delivery-method/return/settings/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DeliveryMethodReturnSettingsResponse)
        assert response.settings.courier_details.contact_days == 3
