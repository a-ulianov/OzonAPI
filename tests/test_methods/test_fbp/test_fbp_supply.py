import pytest

from src.ozonapi.seller.schemas.fbp import (
    FbpActFromCreateRequest,
    FbpActFromCreateResponse,
    FbpActFromGetRequest,
    FbpActFromGetResponse,
    FbpActToCreateRequest,
    FbpActToCreateResponse,
    FbpActToGetRequest,
    FbpActToGetResponse,
    FbpArchiveGetRequest,
    FbpArchiveGetResponse,
    FbpArchiveListRequest,
    FbpArchiveListResponse,
    FbpLabelCreateRequest,
    FbpLabelCreateResponse,
    FbpLabelGetRequest,
    FbpLabelGetResponse,
    FbpOrderGetRequest,
    FbpOrderGetResponse,
    FbpOrderListRequest,
    FbpOrderListResponse,
    PostingFbpGetRequest,
    PostingFbpGetResponse,
    PostingFbpListFilter,
    PostingFbpListRequest,
    PostingFbpListResponse,
)


class TestFbpOrderGet:
    """Тесты для метода fbp_order_get."""

    @pytest.mark.asyncio
    async def test_fbp_order_get(self, api, mock_api_request):
        """Тестирует метод fbp_order_get."""
        mock_api_request.return_value = {
            "id": 1,
            "supply_id": "70",
            "status": "READY_TO_SUPPLY",
            "attention_reasons": ["OLD"],
            "delivery_details": {"supply_type": "PICK_UP"},
            "has_label": True,
        }

        request = FbpOrderGetRequest(supply_id="70")
        response = await api.fbp_order_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderGetResponse)
        assert response.status == "READY_TO_SUPPLY"
        assert response.attention_reasons == ["OLD"]
        assert response.delivery_details.supply_type == "PICK_UP"


class TestFbpOrderList:
    """Тесты для метода fbp_order_list."""

    @pytest.mark.asyncio
    async def test_fbp_order_list(self, api, mock_api_request):
        """Тестирует метод fbp_order_list."""
        mock_api_request.return_value = {
            "items": [
                {"id": 1, "supply_id": "70", "status": "CANCELLED",
                 "bundle_summary": {"total_item_count": 2, "total_quantity": 5}}
            ],
            "has_next": False,
            "last_id": 1,
        }

        request = FbpOrderListRequest(count=50)
        response = await api.fbp_order_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/order/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpOrderListResponse)
        assert response.items[0].bundle_summary.total_quantity == 5
        assert response.last_id == 1


class TestFbpArchiveGet:
    """Тесты для метода fbp_archive_get."""

    @pytest.mark.asyncio
    async def test_fbp_archive_get(self, api, mock_api_request):
        """Тестирует метод fbp_archive_get."""
        mock_api_request.return_value = {
            "id": 1,
            "supply_id": "70",
            "status": "COMPLETED",
            "bundle_sku_summary": {"total_items_count": 3, "total_quantity": 9},
            "decline_reason": {"code": "DROP_OFF_POINT_CLOSED", "message": "Закрыт"},
        }

        request = FbpArchiveGetRequest(supply_id="70")
        response = await api.fbp_archive_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/archive/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpArchiveGetResponse)
        assert response.status == "COMPLETED"
        assert response.bundle_sku_summary.total_quantity == 9
        assert response.decline_reason.code == "DROP_OFF_POINT_CLOSED"


class TestFbpArchiveList:
    """Тесты для метода fbp_archive_list."""

    @pytest.mark.asyncio
    async def test_fbp_archive_list(self, api, mock_api_request):
        """Тестирует метод fbp_archive_list."""
        mock_api_request.return_value = {
            "items": [{"supply_id": "70", "status": "COMPLETED", "external_order_id": "ext-1"}],
            "has_next": True,
            "last_id": 70,
        }

        request = FbpArchiveListRequest(count="50")
        response = await api.fbp_archive_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/archive/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpArchiveListResponse)
        assert response.items[0].external_order_id == "ext-1"
        assert response.has_next is True


class TestFbpActFromCreate:
    """Тесты для метода fbp_act_from_create."""

    @pytest.mark.asyncio
    async def test_fbp_act_from_create(self, api, mock_api_request):
        """Тестирует метод fbp_act_from_create."""
        mock_api_request.return_value = {"is_success": True, "file_uuid": "uuid-act", "errors": []}

        request = FbpActFromCreateRequest(supply_id="70")
        response = await api.fbp_act_from_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/act-from/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpActFromCreateResponse)
        assert response.file_uuid == "uuid-act"


class TestFbpActFromGet:
    """Тесты для метода fbp_act_from_get."""

    @pytest.mark.asyncio
    async def test_fbp_act_from_get(self, api, mock_api_request):
        """Тестирует метод fbp_act_from_get."""
        mock_api_request.return_value = {"status": "EXIST", "cdn_url": "https://cdn/act.pdf"}

        request = FbpActFromGetRequest(file_uuid="uuid-act")
        response = await api.fbp_act_from_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/act-from/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpActFromGetResponse)
        assert response.status == "EXIST"
        assert response.cdn_url == "https://cdn/act.pdf"


class TestFbpActToCreate:
    """Тесты для метода fbp_act_to_create."""

    @pytest.mark.asyncio
    async def test_fbp_act_to_create(self, api, mock_api_request):
        """Тестирует метод fbp_act_to_create."""
        mock_api_request.return_value = {"code": "code-1"}

        request = FbpActToCreateRequest(supply_id="70")
        response = await api.fbp_act_to_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/act-to/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpActToCreateResponse)
        assert response.code == "code-1"


class TestFbpActToGet:
    """Тесты для метода fbp_act_to_get."""

    @pytest.mark.asyncio
    async def test_fbp_act_to_get(self, api, mock_api_request):
        """Тестирует метод fbp_act_to_get."""
        mock_api_request.return_value = {"state": "FINISHED", "label_url": "https://cdn/note.pdf"}

        request = FbpActToGetRequest(supply_id="70", code="code-1")
        response = await api.fbp_act_to_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/act-to/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpActToGetResponse)
        assert response.state == "FINISHED"


class TestFbpLabelCreate:
    """Тесты для метода fbp_label_create."""

    @pytest.mark.asyncio
    async def test_fbp_label_create(self, api, mock_api_request):
        """Тестирует метод fbp_label_create."""
        mock_api_request.return_value = {"code": "label-1"}

        request = FbpLabelCreateRequest(supply_id="70")
        response = await api.fbp_label_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/label/create",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpLabelCreateResponse)
        assert response.code == "label-1"


class TestFbpLabelGet:
    """Тесты для метода fbp_label_get."""

    @pytest.mark.asyncio
    async def test_fbp_label_get(self, api, mock_api_request):
        """Тестирует метод fbp_label_get."""
        mock_api_request.return_value = {"state": "FINISHED", "label_url": "https://cdn/label.pdf"}

        request = FbpLabelGetRequest(supply_id="70", code="label-1")
        response = await api.fbp_label_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="fbp/label/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, FbpLabelGetResponse)
        assert response.label_url == "https://cdn/label.pdf"


class TestPostingFbpList:
    """Тесты для метода posting_fbp_list."""

    @pytest.mark.asyncio
    async def test_posting_fbp_list(self, api, mock_api_request):
        """Тестирует метод posting_fbp_list."""
        mock_api_request.return_value = {
            "postings": [
                {
                    "posting_number": "P-1",
                    "status": "delivered",
                    "products": [
                        {"sku": 123, "name": "Товар", "quantity": 2,
                         "price": {"amount": "100.00", "currency": "RUB"}}
                    ],
                    "financial_data": {
                        "delivery_amount": 50.0,
                        "products": [
                            {"product_id": 123, "price": 100.0,
                             "actions": [{"action_id": "a1", "discount_value": 10.0}]}
                        ],
                    },
                }
            ],
            "cursor": "next",
        }

        request = PostingFbpListRequest(
            filter=PostingFbpListFilter(since="2026-06-01T00:00:00Z", to="2026-06-30T00:00:00Z"),
            limit=100,
        )
        response = await api.posting_fbp_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbp/list",
            payload=request.model_dump(),
        )
        assert isinstance(response, PostingFbpListResponse)
        assert response.cursor == "next"
        assert response.postings[0].posting_number == "P-1"
        assert response.postings[0].products[0].price.amount == "100.00"
        assert response.postings[0].financial_data.products[0].actions[0].action_id == "a1"


class TestPostingFbpGet:
    """Тесты для метода posting_fbp_get."""

    @pytest.mark.asyncio
    async def test_posting_fbp_get(self, api, mock_api_request):
        """Тестирует метод posting_fbp_get."""
        mock_api_request.return_value = {
            "posting": {
                "posting_number": "P-1",
                "order_id": 12345,
                "order_number": "O-1",
                "status": 3,
                "substatus": "posting_transferred_to_delivery",
                "tpl_provider_id": 24,
                "analytics_data": {"city": "Москва", "warehouse_id": 42},
                "cancellation": {"cancel_reason_id": 0, "cancel_reason": ""},
                "products": [
                    {
                        "sku": 123,
                        "name": "Товар",
                        "offer_id": "art-1",
                        "quantity": 2,
                        "has_imei": False,
                        "marketplace_seller_price": {"amount": "100.00", "currency": "RUB"},
                    }
                ],
                "financial_data": {
                    "delivery_amount": 50.0,
                    "products": [
                        {
                            "sku": 123,
                            "quantity": 2,
                            "old_price": 120.0,
                            "commissions_price": {"amount": "10.00", "currency": "RUB"},
                            "posting_commission": {"amount": 10.0, "payout": 90.0, "percent": 10.0},
                            "actions": [{"action_id": 1, "discount_value": 20.0}],
                        }
                    ],
                },
            }
        }

        request = PostingFbpGetRequest(posting_number="P-1")
        response = await api.posting_fbp_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/fbp/get",
            payload=request.model_dump(),
        )
        assert isinstance(response, PostingFbpGetResponse)
        assert response.posting.posting_number == "P-1"
        assert response.posting.status == 3
        assert response.posting.products[0].marketplace_seller_price.amount == "100.00"
        assert response.posting.financial_data.products[0].posting_commission.payout == 90.0
        assert response.posting.financial_data.products[0].actions[0].action_id == 1
