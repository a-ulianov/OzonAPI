import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.methods import SellerProductAPI
from src.ozonapi.seller.schemas.products import (
    ProductArchiveRequest,
    ProductArchiveResponse,
    ProductImportRequest,
    ProductImportResponse,
    ProductImportInfoRequest,
    ProductImportInfoResponse,
    ProductImportBySkuRequest,
    ProductImportBySkuResponse,
    ProductAttributesUpdateRequest,
    ProductAttributesUpdateResponse,
    ProductsDeleteRequest,
    ProductsDeleteResponse,
    ProductUnarchiveRequest,
    ProductUnarchiveResponse,
    ProductInfoAttributesRequest,
    ProductInfoAttributesResponse,
    ProductInfoListRequest,
    ProductInfoListResponse,
    ProductInfoSubscriptionRequest,
    ProductInfoSubscriptionResponse,
    ProductListRequest,
    ProductListResponse,
    ProductPicturesInfoRequest,
    ProductPicturesInfoResponse,
    ProductRatingBySkuRequest,
    ProductRatingBySkuResponse,
    ProductRelatedSkuGetRequest,
    ProductRelatedSkuGetResponse,
    ProductUpdateOfferIdRequest,
    ProductUpdateOfferIdResponse, ProductPicturesImportResponse, ProductPicturesImportRequest, ProductInfoLimitResponse,
)


class TestSellerProductAPI:
    """Тесты для класса SellerProductAPI."""

    @pytest.fixture
    def seller_product_api(self):
        """Фикстура для создания экземпляра SellerProductAPI."""
        return SellerProductAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerProductAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_product_archive(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_archive."""
        mock_response_data = {
            "result": True
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductArchiveRequest(
            product_id=[123456, 789012]
        )
        response = await seller_product_api.product_archive(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/archive",
            json=request.model_dump()
        )
        assert isinstance(response, ProductArchiveResponse)
        assert response.result is True

    @pytest.mark.asyncio
    async def test_product_import(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_import."""
        mock_response_data = {
            "result": {
                "task_id": 123456789
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductImportRequest(
            items=[]
        )
        response = await seller_product_api.product_import(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/import",
            json=request.model_dump()
        )
        assert isinstance(response, ProductImportResponse)
        assert response.result.task_id == 123456789

    @pytest.mark.asyncio
    async def test_product_import_info(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_import_info."""
        mock_response_data = {
            "result": {
                "items": [],
                "total": 0
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductImportInfoRequest(
            task_id=1234567
        )
        response = await seller_product_api.product_import_info(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import/info",
            json=request.model_dump()
        )
        assert isinstance(response, ProductImportInfoResponse)
        assert response.result.total == 0

    @pytest.mark.asyncio
    async def test_product_import_by_sku(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_import_by_sku."""
        mock_response_data = {
            "task_id": 123456789,
            "unmatched_sku_list": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductImportBySkuRequest(
            items=[]
        )
        response = await seller_product_api.product_import_by_sku(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/import-by-sku",
            json=request.model_dump()
        )
        assert isinstance(response, ProductImportBySkuResponse)
        assert response.task_id == 123456789

    @pytest.mark.asyncio
    async def test_product_attributes_update(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_attributes_update."""
        mock_response_data = {
            "task_id": 123456789
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductAttributesUpdateRequest(
            items=[]
        )
        response = await seller_product_api.product_attributes_update(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/attributes/update",
            json=request.model_dump()
        )
        assert isinstance(response, ProductAttributesUpdateResponse)
        assert response.task_id == 123456789

    @pytest.mark.asyncio
    async def test_products_delete(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод products_delete."""
        mock_response_data = {
            "status": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductsDeleteRequest(
            products=[]
        )
        response = await seller_product_api.products_delete(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="products/delete",
            json=request.model_dump()
        )
        assert isinstance(response, ProductsDeleteResponse)
        assert response.status == []

    @pytest.mark.asyncio
    async def test_product_unarchive(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_unarchive."""
        mock_response_data = {
            "result": True
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductUnarchiveRequest(
            product_id=[125529926]
        )
        response = await seller_product_api.product_unarchive(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/unarchive",
            json=request.model_dump()
        )
        assert isinstance(response, ProductUnarchiveResponse)
        assert response.result is True

    @pytest.mark.asyncio
    async def test_product_info_attributes(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_info_attributes."""
        mock_response_data = {
            "result": [],
            "last_id": "test_last_id",
            "total": 0
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoAttributesRequest()
        response = await seller_product_api.product_info_attributes(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/attributes",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoAttributesResponse)
        assert response.total == 0

    @pytest.mark.asyncio
    async def test_product_info_list(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_info_list."""
        mock_response_data = {
            "items": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoListRequest(
            product_id=[123456789, 987654321]
        )
        response = await seller_product_api.product_info_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/info/list",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoListResponse)
        assert response.items == []

    @pytest.mark.asyncio
    async def test_product_subscription(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_subscription."""
        mock_response_data = {
            "result": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoSubscriptionRequest(
            skus=[123456789, 987654321]
        )
        response = await seller_product_api.product_subscription(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/subscription",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoSubscriptionResponse)
        assert response.result == []

    @pytest.mark.asyncio
    async def test_product_list(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_list."""
        mock_response_data = {
            "result": {
                "items": [],
                "last_id": "test_last_id",
                "total": 0
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductListRequest()
        response = await seller_product_api.product_list(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="product/list",
            json=request.model_dump()
        )
        assert isinstance(response, ProductListResponse)
        assert response.result.total == 0

    @pytest.mark.asyncio
    async def test_product_pictures_info(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_pictures_info."""
        mock_response_data = {
            "items": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductPicturesInfoRequest(
            product_id=[123456789, 987654321]
        )
        response = await seller_product_api.product_pictures_info(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="product/pictures/info",
            json=request.model_dump()
        )
        assert isinstance(response, ProductPicturesInfoResponse)
        assert response.items == []

    @pytest.mark.asyncio
    async def test_product_rating_by_sku(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_rating_by_sku."""
        mock_response_data = {
            "products": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductRatingBySkuRequest(
            skus=[179737222, 179737223]
        )
        response = await seller_product_api.product_rating_by_sku(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/rating-by-sku",
            json=request.model_dump()
        )
        assert isinstance(response, ProductRatingBySkuResponse)
        assert response.products == []

    @pytest.mark.asyncio
    async def test_product_related_sku_get(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_related_sku_get."""
        mock_response_data = {
            "items": [],
            "errors": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductRelatedSkuGetRequest(
            sku=[123456789, 987654321]
        )
        response = await seller_product_api.product_related_sku_get(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/related-sku/get",
            json=request.model_dump()
        )
        assert isinstance(response, ProductRelatedSkuGetResponse)
        assert response.items == []

    @pytest.mark.asyncio
    async def test_product_update_offer_id(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_update_offer_id."""
        mock_response_data = {
            "errors": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductUpdateOfferIdRequest(
            update_offer_id=[]
        )
        response = await seller_product_api.product_update_offer_id(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/update/offer-id",
            json=request.model_dump()
        )
        assert isinstance(response, ProductUpdateOfferIdResponse)
        assert response.errors == []

    @pytest.mark.asyncio
    async def test_product_pictures_import(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_pictures_import."""
        mock_response_data = {
            "result": {
                "pictures": [
                    {
                        "is_360": True,
                        "is_color": False,
                        "is_primary": True,
                        "product_id": 123456789,
                        "state": "imported",
                        "url": "https://example.com/image1.jpg"
                    },
                    {
                        "is_360": False,
                        "is_color": True,
                        "is_primary": False,
                        "product_id": 123456789,
                        "state": "imported",
                        "url": "https://example.com/color.jpg"
                    }
                ]
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductPicturesImportRequest(
            product_id=123456789,
            color_image="https://example.com/color.jpg",
            images=[
                "https://example.com/image1.jpg",
                "https://example.com/image2.jpg",
            ],
            images360=[
                "https://example.com/360_1.jpg",
            ]
        )
        response = await seller_product_api.product_pictures_import(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/pictures/import",
            json=request.model_dump()
        )
        assert isinstance(response, ProductPicturesImportResponse)
        assert len(response.result.pictures) == 2
        assert response.result.pictures[0].product_id == 123456789
        assert response.result.pictures[0].state == "imported"
        assert response.result.pictures[0].is_primary is True
        assert response.result.pictures[1].is_color is True

    @pytest.mark.asyncio
    async def test_product_info_limit(self, seller_product_api, mock_api_manager_request):
        """Тестирует метод product_info_limit."""
        mock_response_data = {
            "daily_create": {
                "limit": 1000,
                "reset_at": "2024-01-01T00:00:00Z",
                "usage": 150
            },
            "daily_update": {
                "limit": 2000,
                "reset_at": "2024-01-01T00:00:00Z",
                "usage": 300
            },
            "total": {
                "limit": 10000,
                "usage": 2500
            }
        }
        mock_api_manager_request.return_value = mock_response_data

        response = await seller_product_api.product_info_limit()

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/limit",
            json={}
        )
        assert isinstance(response, ProductInfoLimitResponse)
        assert response.daily_create.limit == 1000
        assert response.daily_create.usage == 150
        assert response.daily_update.limit == 2000
        assert response.daily_update.usage == 300
        assert response.total.limit == 10000
        assert response.total.usage == 2500