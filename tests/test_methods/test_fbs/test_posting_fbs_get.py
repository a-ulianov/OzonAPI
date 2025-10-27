import pytest

from src.ozonapi.seller.common.enumerations.localization import CurrencyCode
from src.ozonapi.seller.common.enumerations.postings import PostingStatus, PostingSubstatus, TplIntegrationType, \
    AvailablePostingActions
from src.ozonapi.seller.schemas.fbs import PostingFBSGetResponse


class TestPostingFBSGet:
    """Тесты для метода posting_fbs_get."""

    @pytest.mark.asyncio
    async def test_posting_fbs_get(self, api, mock_api_request):
        """Тестирует метод posting_fbs_get."""

        mock_response_data = {
            "result": {
                "additional_data": [],
                "addressee": None,
                "analytics_data": None,
                "available_actions": [AvailablePostingActions.ARBITRATION],
                "barcodes": None,
                "cancellation": {
                    "cancel_reason_id": 0,
                    "cancel_reason": "",
                    "cancellation_type": "",
                    "cancelled_after_ship": False,
                    "affect_cancellation_rating": False,
                    "cancellation_initiator": ""
                },
                "courier": None,
                "customer": None,
                "delivering_date": None,
                "delivery_method": {
                    "id": 18114520187000,
                    "name": "Ozon Логистика самостоятельно, Москва",
                    "warehouse_id": 18114520187000,
                    "warehouse": "Москва основной",
                    "tpl_provider_id": 24,
                    "tpl_provider": "Ozon Логистика"
                },
                "delivery_price": "",
                "financial_data": None,
                "in_process_at": "2021-11-20T09:14:16Z",
                "is_express": False,
                "is_multibox": False,
                "legal_info": None,
                "multi_box_qty": None,
                "optional": {
                    "products_with_possible_mandatory_mark": [0]
                },
                "order_id": 438764970,
                "order_number": "57195475-0050",
                "parent_posting_number": None,
                "pickup_code_verified_at": "2025-01-17T11:04:59.958Z",
                "posting_number": "57195475-0050-3",
                "product_exemplars": None,
                "products": [
                    {
                        "currency_code": CurrencyCode.RUB,
                        "is_blr_traceable": True,
                        "is_marketplace_buyout": True,
                        "price": "279.0000",
                        "offer_id": "250-7898-1",
                        "name": "Кофе ароматизированный \"Шоколадный апельсин\" 250 гр",
                        "sku": 180550365,
                        "quantity": 1,
                        "jw_uin": [],
                        "dimensions": {
                            "height": "40.00",
                            "length": "240.00",
                            "weight": "260",
                            "width": "140.00"
                        },
                        "has_imei": False
                    }
                ],
                "provider_status": "",
                "prr_option": None,
                "quantum_id": None,
                "related_postings": {
                    "related_posting_numbers": ["57195475-0050-4"]
                },
                "related_weight_postings": [],
                "requirements": {
                    "products_requiring_change_country": [],
                    "products_requiring_gtd": [],
                    "products_requiring_country": [],
                    "products_requiring_jwn": [],
                    "products_requiring_imei": []
                },
                "shipment_date": "2021-11-23T10:00:00Z",
                "shipment_date_without_delay": "2021-11-23T10:00:00Z",
                "status": PostingStatus.AWAITING_PACKAGING,
                "substatus": PostingSubstatus.POSTING_AWAITING_PASSPORT_DATA,
                "previous_substatus": PostingSubstatus.POSTING_TRANSFERRING_TO_DELIVERY,
                "tpl_integration_type": TplIntegrationType.OZON,
                "tracking_number": "",
                "tariffication": {
                    "current_tariff_rate": 0,
                    "current_tariff_type": "",
                    "current_tariff_charge": "",
                    "current_tariff_charge_currency_code": "",
                    "next_tariff_rate": 0,
                    "next_tariff_type": "",
                    "next_tariff_charge": "",
                    "next_tariff_starts_at": "2023-11-13T08:05:57.657Z",
                    "next_tariff_charge_currency_code": ""
                }
            }
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v3__posting_fbs_get import (
            PostingFBSGetRequest,
            PostingFBSGetRequestWith
        )

        request = PostingFBSGetRequest(
            posting_number="57195475-0050-3",
            with_=PostingFBSGetRequestWith(
                analytics_data=False,
                barcodes=False,
                financial_data=False,
                legal_info=False,
                product_exemplars=False,
                related_postings=True,
                translit=False
            )
        )

        response = await api.posting_fbs_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v3",
            endpoint="posting/fbs/get",
            json=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSGetResponse)
        assert response.result.posting_number == "57195475-0050-3"
        assert response.result.order_id == 438764970
        assert response.result.order_number == "57195475-0050"
        assert response.result.status == PostingStatus.AWAITING_PACKAGING
        assert response.result.substatus == PostingSubstatus.POSTING_AWAITING_PASSPORT_DATA
        assert response.result.previous_substatus == PostingSubstatus.POSTING_TRANSFERRING_TO_DELIVERY
        assert response.result.delivery_method.name == "Ozon Логистика самостоятельно, Москва"
        assert response.result.delivery_method.tpl_provider_id == 24
        assert len(response.result.products) == 1
        assert response.result.products[0].sku == 180550365
        assert response.result.products[0].offer_id == "250-7898-1"
        assert response.result.products[0].name == "Кофе ароматизированный \"Шоколадный апельсин\" 250 гр"
        assert response.result.related_postings.related_posting_numbers == ["57195475-0050-4"]
