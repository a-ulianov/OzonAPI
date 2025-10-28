import pytest

from src.ozonapi.seller.schemas.fbs import PostingFBSPackageLabelResponse


class TestPostingFBSPackageLabel:
    """Тесты для метода posting_fbs_package_label."""

    @pytest.mark.asyncio
    async def test_posting_fbs_package_label(self, api, mock_api_request):
        """Тестирует метод posting_fbs_package_label."""

        mock_response_data = {
            "content_type": "application/pdf",
            "file_name": "ticket-170660-2023-07-13T13:17:06Z.pdf",
            "file_content": "%PDF-1.7\n%âãÏÓ\n53 0 obj\n<</MarkInfo<</Marked true/Type/MarkInfo>>/Pages 9 0 R/StructTreeRoot 10 0 R/Type/Catalog>>\nendobj\n8 0 obj\n<</Filter/FlateDecode/Length 2888>>\nstream\nxå[[ݶ\u0011~?¿BÏ\u0005Bs\u001c^\u0000Àwí5ú\u0010 m\u0016Èsà¦)\n;hÒ\u0014èÏïG\u0014)<{äµ] ]?¬¬oIÎ}¤F±óϤñï\u001bÕü×X­´OÏï?^~¹$<ø¨È9q\u0013Y\u0012åñì§_¼|ÿégü\t+\u0012\u001bxª}Æxҿ¿¼_º¼xg¦þ5OkuÌ3ýíògüûå\"Ni\u0016C\u0001°\u000fA9g'r¢\"\u0013YóĪ\u0018NÑ{\u001dÕóZ¬\\Ô\""
        }
        mock_api_request.return_value = mock_response_data

        from src.ozonapi.seller.schemas.fbs.v2__posting_fbs_package_label import (
            PostingFBSPackageLabelRequest
        )

        request = PostingFBSPackageLabelRequest(
            posting_number=["48173252-0034-4", "48173252-0035-4"]
        )

        response = await api.posting_fbs_package_label(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingFBSPackageLabelResponse)
        assert response.content_type == "application/pdf"
        assert response.file_name == "ticket-170660-2023-07-13T13:17:06Z.pdf"
        assert isinstance(response.file_content, str)
        assert len(response.file_content) > 0
        assert response.file_content.startswith("%PDF-1.7")
