import datetime
import pytest

from src.ozonapi.seller.common.enumerations.postings import PostingStatus
from src.ozonapi.seller.common.enumerations.requests import SortingDirection
from src.ozonapi.seller.schemas.fbo import PostingFBOListResponse


class TestPostingFBOList:
    """Тесты для метода posting_fbo_list."""

    @pytest.mark.asyncio
    async def test_posting_fbo_list(self, api, mock_api_request):
        """Тестирует метод posting_fbo_list."""

        mock_response_data = {
            "result": [
                {
                    "additional_data": [],
                    "analytics_data": {
                        "city": "Москва",
                        "delivery_type": "courier",
                        "is_legal": False,
                        "is_premium": False,
                        "payment_type_group_name": "card",
                        "region": "Москва",
                        "warehouse_id": 123456789,
                        "warehouse_name": "Основной склад"
                    },
                    "cancel_reason_id": None,
                    "created_at": "2025-09-01T10:00:00Z",
                    "financial_data": None,
                    "in_process_at": "2025-09-01T11:00:00Z",
                    "legal_info": None,
                    "order_id": 123456789,
                    "order_number": "ORDER-123",
                    "posting_number": "4567890123",
                    "products": [
                        {
                            "digital_codes": [],
                            "name": "Тестовый товар",
                            "offer_id": "TEST-001",
                            "currency_code": "RUB",
                            "price": 1500,
                            "is_marketplace_buyout": False,
                            "quantity": 1,
                            "sku": 987654321
                        }
                    ],
                    "status": PostingStatus.DELIVERED
                },
                {
                    "additional_data": [],
                    "analytics_data": {
                        "city": "Санкт-Петербург",
                        "delivery_type": "pickup",
                        "is_legal": True,
                        "is_premium": True,
                        "payment_type_group_name": "cash",
                        "region": "Ленинградская область",
                        "warehouse_id": 987654321,
                        "warehouse_name": "Склад СПб"
                    },
                    "cancel_reason_id": None,
                    "created_at": "2025-09-02T10:00:00Z",
                    "financial_data": None,
                    "in_process_at": "2025-09-02T11:00:00Z",
                    "legal_info": None,
                    "order_id": 123456790,
                    "order_number": "ORDER-124",
                    "posting_number": "4567890124",
                    "products": [
                        {
                            "digital_codes": ["CODE123", "CODE456"],
                            "name": "Цифровой товар",
                            "offer_id": "DIGITAL-001",
                            "currency_code": "RUB",
                            "price": "2000.0000",
                            "is_marketplace_buyout": True,
                            "quantity": 2,
                            "sku": 987654322
                        }
                    ],
                    "status": PostingStatus.DELIVERED
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbo import PostingFBOListRequest
        from src.ozonapi.seller.schemas.entities.postings import PostingFilter, PostingFilterWith
        # noinspection PyArgumentList
        request = PostingFBOListRequest(
            dir=SortingDirection.ASC,
            filter=PostingFilter(
                since=datetime.datetime(2025, 9, 1),
                to_=datetime.datetime(2025, 11, 17, 10, 44, 12, 828000),
                status=PostingStatus.DELIVERED
            ),
            limit=100,
            offset=0,
            translit=False,
            with_=PostingFilterWith(
                analytics_data=True,
                financial_data=False,
                legal_info=True
            )
        )

        response = await api.posting_fbo_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbo/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBOListResponse)
        assert len(response.result) == 2

        first_posting = response.result[0]
        second_posting = response.result[1]

        assert first_posting.posting_number == "4567890123"
        assert first_posting.order_id == 123456789
        assert first_posting.status == PostingStatus.DELIVERED
        assert first_posting.analytics_data.warehouse_name == "Основной склад"
        assert len(first_posting.products) == 1
        assert first_posting.products[0].offer_id == "TEST-001"
        assert first_posting.products[0].price == 1500

        assert second_posting.posting_number == "4567890124"
        assert second_posting.analytics_data.warehouse_name == "Склад СПб"
        assert second_posting.products[0].is_marketplace_buyout is True
        assert second_posting.products[0].digital_codes == ["CODE123", "CODE456"]