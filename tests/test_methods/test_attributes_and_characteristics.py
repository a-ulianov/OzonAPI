import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.methods import SellerCategoryAPI
from src.ozonapi.seller.schemas.attributes_and_characteristics import (
    DescriptionCategoryTreeRequest,
    DescriptionCategoryTreeResponse,
    DescriptionCategoryAttributeRequest,
    DescriptionCategoryAttributeResponse,
    DescriptionCategoryAttributeValuesRequest,
    DescriptionCategoryAttributeValuesResponse,
    DescriptionCategoryAttributeValuesSearchRequest,
    DescriptionCategoryAttributeValuesSearchResponse,
)
from src.ozonapi.seller.common.enumerations.localization import Language


class TestSellerCategoryAPI:
    """Тесты для класса SellerCategoryAPI."""

    @pytest.fixture
    def seller_category_api(self):
        """Фикстура для создания экземпляра SellerCategoryAPI."""
        return SellerCategoryAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerCategoryAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_description_category_tree(self, seller_category_api, mock_api_manager_request):
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
        mock_api_manager_request.return_value = mock_response_data

        request = DescriptionCategoryTreeRequest(language=Language.DEFAULT)
        response = await seller_category_api.description_category_tree(request)

        mock_api_manager_request.assert_called_once_with(
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

    @pytest.mark.asyncio
    async def test_description_category_attribute(self, seller_category_api, mock_api_manager_request):
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
        mock_api_manager_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeRequest(
            description_category_id=200000933,
            type_id=93080,
            language=Language.DEFAULT
        )
        response = await seller_category_api.description_category_attribute(request)

        mock_api_manager_request.assert_called_once_with(
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

    @pytest.mark.asyncio
    async def test_description_category_attribute_values(self, seller_category_api, mock_api_manager_request):
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
        mock_api_manager_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeValuesRequest(
            attribute_id=85,
            description_category_id=200000933,
            type_id=93080,
            language=Language.DEFAULT,
            last_value_id=0,
            limit=100
        )
        response = await seller_category_api.description_category_attribute_values(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values",
            json=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryAttributeValuesResponse)
        assert len(response.result) == 2
        assert response.has_next is False

        first_value = response.result[0]
        assert first_value.id == 1
        assert first_value.value == "Черный"
        assert first_value.info == "Черный цвет"

    @pytest.mark.asyncio
    async def test_description_category_attribute_values_search(self, seller_category_api, mock_api_manager_request):
        """Тестирует метод description_category_attribute_values_search."""

        mock_response_data = {
            "result": [
                {
                    "id": 1,
                    "info": "Красивый цвет",
                    "picture": "https://example.com/beauty.jpg",
                    "value": "Красота"
                },
                {
                    "id": 2,
                    "info": "Очень красивый цвет",
                    "picture": "https://example.com/very-beauty.jpg",
                    "value": "Очень красивый"
                }
            ]
        }
        mock_api_manager_request.return_value = mock_response_data

        request = DescriptionCategoryAttributeValuesSearchRequest(
            attribute_id=85,
            description_category_id=200000933,
            type_id=93080,
            value="Красота",
            limit=50
        )
        response = await seller_category_api.description_category_attribute_values_search(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="description-category/attribute/values/search",
            json=request.model_dump()
        )
        assert isinstance(response, DescriptionCategoryAttributeValuesSearchResponse)
        assert len(response.result) == 2
        assert response.result[0].value == "Красота"
        assert response.result[1].value == "Очень красивый"