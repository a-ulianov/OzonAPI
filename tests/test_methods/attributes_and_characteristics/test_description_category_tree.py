import pytest

from src.ozonapi.seller.common.enumerations.localization import Language
from src.ozonapi.seller.schemas.attributes_and_characteristics import DescriptionCategoryTreeRequest, \
    DescriptionCategoryTreeResponse


class TestDescriptionCategoryTree:
    """Тесты для метода description_category_tree."""

    @pytest.mark.asyncio
    async def test_description_category_tree(self, api, mock_api_request):
        """Тестирует метод description_category_tree."""

        mock_response_data = {
            "result": [
                {
                    "description_category_id": 200000933,
                    "category_name": "Электроника",
                    "disabled": False,
                    "type_id": 93080,
                    "type_name": "Смартфоны",
                    "children": [
                        {
                            "description_category_id": 200000934,
                            "category_name": "Аксессуары для смартфонов",
                            "disabled": False,
                            "type_id": 93081,
                            "type_name": "Чехлы",
                            "children": []
                        }
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = DescriptionCategoryTreeRequest(language=Language.DEFAULT)
        response = await api.description_category_tree(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/tree",
            json=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryTreeResponse)
        assert len(response.result) == 1
        assert response.result[0].description_category_id == 200000933
        assert response.result[0].category_name == "Электроника"
        assert response.result[0].children[0].category_name == "Аксессуары для смартфонов"