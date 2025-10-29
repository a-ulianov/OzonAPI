import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarCreateOrGetResponse


class TestFBSPostingProductExemplarCreateOrGet:
    """Тесты для метода fbs_posting_product_exemplar_create_or_get."""

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_create_or_get(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_create_or_get."""

        mock_response_data = {
            "multi_box_qty": 1,
            "posting_number": "43658312-0011-1",
            "products": [
                {
                    "exemplars": [
                        {
                            "exemplar_id": 1,
                            "gtd": "10714440/110922/0012345/1",
                            "is_gtd_absent": False,
                            "is_rnpt_absent": True,
                            "marks": [
                                {
                                    "mark": "010460406349100021N4O0B5A8B1",
                                    "mark_type": "mandatory_mark"
                                }
                            ],
                            "rnpt": None,
                            "weight": 1.5
                        }
                    ],
                    "has_imei": False,
                    "is_gtd_needed": True,
                    "is_jw_uin_needed": False,
                    "is_mandatory_mark_needed": True,
                    "is_mandatory_mark_possible": True,
                    "is_rnpt_needed": False,
                    "product_id": 123456789,
                    "quantity": 1,
                    "is_weight_needed": True,
                    "weight_max": 2.0,
                    "weight_min": 1.0
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            FBSPostingProductExemplarCreateOrGetRequest
        )

        request = FBSPostingProductExemplarCreateOrGetRequest(
            posting_number="43658312-0011-1"
        )

        response = await api.fbs_posting_product_exemplar_create_or_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v6",
            endpoint="fbs/posting/product/exemplar/create-or-get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FBSPostingProductExemplarCreateOrGetResponse)
        assert response.multi_box_qty == 1
        assert response.posting_number == "43658312-0011-1"
        assert len(response.products) == 1

        product = response.products[0]
        assert product.product_id == 123456789
        assert product.quantity == 1
        assert product.has_imei is False
        assert product.is_gtd_needed is True
        assert product.is_jw_uin_needed is False
        assert product.is_mandatory_mark_needed is True
        assert product.is_mandatory_mark_possible is True
        assert product.is_rnpt_needed is False
        assert product.is_weight_needed is True
        assert product.weight_max == 2.0
        assert product.weight_min == 1.0

        assert len(product.exemplars) == 1
        exemplar = product.exemplars[0]
        assert exemplar.exemplar_id == 1
        assert exemplar.gtd == "10714440/110922/0012345/1"
        assert exemplar.is_gtd_absent is False
        assert exemplar.is_rnpt_absent is True
        assert exemplar.rnpt is None
        assert exemplar.weight == 1.5

        assert len(exemplar.marks) == 1
        mark = exemplar.marks[0]
        assert mark.mark == "010460406349100021N4O0B5A8B1"
        assert mark.mark_type == "mandatory_mark"