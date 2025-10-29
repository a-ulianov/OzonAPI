import pytest

from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import FBSPostingProductExemplarStatusResponse


class TestFBSPostingProductExemplarStatus:
    """Тесты для метода fbs_posting_product_exemplar_status."""

    @pytest.mark.asyncio
    async def test_fbs_posting_product_exemplar_status(self, api, mock_api_request):
        """Тестирует метод fbs_posting_product_exemplar_status."""

        mock_response_data = {
            "posting_number": "43658312-0011-1",
            "status": "ship_available",
            "products": [
                {
                    "product_id": "123456789",
                    "exemplars": [
                        {
                            "exemplar_id": 1,
                            "gtd": "10714440/110922/0012345/1",
                            "gtd_check_status": "checked",
                            "gtd_error_codes": [],
                            "is_gtd_absent": False,
                            "is_rnpt_absent": True,
                            "marks": [
                                {
                                    "mark": "010460406349100021N4O0B5A8B1",
                                    "mark_type": "mandatory_mark",
                                    "check_status": "checked",
                                    "error_codes": []
                                }
                            ],
                            "rnpt": None,
                            "rnpt_check_status": "not_required",
                            "rnpt_error_codes": [],
                            "weight": 1.5,
                            "weight_check_status": "checked",
                            "weight_error_codes": []
                        }
                    ]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs_assembly_and_labeling import (
            FBSPostingProductExemplarStatusRequest
        )

        request = FBSPostingProductExemplarStatusRequest(
            posting_number="43658312-0011-1"
        )

        response = await api.fbs_posting_product_exemplar_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="fbs/posting/product/exemplar/status",
            payload=request.model_dump()
        )

        assert isinstance(response, FBSPostingProductExemplarStatusResponse)
        assert response.posting_number == "43658312-0011-1"
        assert response.status == "ship_available"
        assert len(response.products) == 1
        assert response.products[0].product_id == "123456789"
        assert len(response.products[0].exemplars) == 1
        assert response.products[0].exemplars[0].exemplar_id == 1
        assert response.products[0].exemplars[0].gtd == "10714440/110922/0012345/1"
        assert response.products[0].exemplars[0].gtd_check_status == "checked"
        assert response.products[0].exemplars[0].weight == 1.5
        assert response.products[0].exemplars[0].marks[0].mark == "010460406349100021N4O0B5A8B1"
        assert response.products[0].exemplars[0].marks[0].check_status == "checked"