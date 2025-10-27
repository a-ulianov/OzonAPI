import pytest

from src.ozonapi.seller.common.enumerations.localization import Language
from src.ozonapi.seller.schemas.attributes_and_characteristics import DescriptionCategoryAttributeRequest, \
    DescriptionCategoryAttributeResponse


class TestDescriptionCategoryAttribute:
    """Тесты для метода description_category_attribute."""

    @pytest.mark.asyncio
    async def test_description_category_attribute(self, api, mock_api_request):
        """Тестирует метод description_category_attribute."""

        mock_response_data = {
            "result": [
                {
                    "category_dependent": True,
                    "description": "Цвет товара",
                    "dictionary_id": 85,
                    "group_id": 1,
                    "group_name": "Основные характеристики",
                    "id": 85,
                    "is_aspect": True,
                    "is_collection": False,
                    "is_required": True,
                    "name": "Цвет",
                    "type": "string",
                    "attribute_complex_id": 0,
                    "max_value_count": 1,
                    "complex_is_collection": False
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeRequest(
            description_category_id=200000933,
            type_id=93080,
            language=Language.DEFAULT
        )
        response = await api.description_category_attribute(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute",
            json=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryAttributeResponse)
        assert len(response.result) == 1
        attribute = response.result[0]
        assert attribute.id == 85
        assert attribute.name == "Цвет"
        assert attribute.is_required is True
        assert attribute.is_aspect is True
        assert attribute.dictionary_id == 85
