import pytest

from src.ozonapi.seller.common.enumerations.localization import Language
from src.ozonapi.seller.schemas.attributes_and_characteristics import DescriptionCategoryAttributeValuesResponse, \
    DescriptionCategoryAttributeValuesRequest


class TestDescriptionCategoryAttributeValues:
    """Тесты для метода description_category_attribute_values."""

    @pytest.mark.asyncio
    async def test_description_category_attribute_values(self, api, mock_api_request):
        """Тестирует метод description_category_attribute_values."""

        mock_response_data = {
            "result": [
                {
                    "id": 1,
                    "info": "Черный цвет",
                    "picture": "https://example.com/black.jpg",
                    "value": "Черный"
                },
                {
                    "id": 2,
                    "info": "Белый цвет",
                    "picture": "https://example.com/white.jpg",
                    "value": "Белый"
                }
            ],
            "has_next": False
        }
        mock_api_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeValuesRequest(
            attribute_id=85,
            description_category_id=200000933,
            type_id=93080,
            language=Language.DEFAULT,
            last_value_id=0,
            limit=100
        )
        response = await api.description_category_attribute_values(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values",
            payload=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryAttributeValuesResponse)
        assert len(response.result) == 2
        assert response.has_next is False

        first_value = response.result[0]
        assert first_value.id == 1
        assert first_value.value == "Черный"
        assert first_value.info == "Черный цвет"
