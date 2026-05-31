from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSActGetContainerLabelsRequest,
    PostingFBSActGetContainerLabelsResponse,
)


class PostingFBSActGetContainerLabelsMixin(APIManager):
    """Реализует метод /v2/posting/fbs/act/get-container-labels"""

    async def posting_fbs_act_get_container_labels(
            self: "PostingFBSActGetContainerLabelsMixin",
            request: PostingFBSActGetContainerLabelsRequest
    ) -> PostingFBSActGetContainerLabelsResponse:
        """Метод для получения этикеток для грузового места.

        Notes:
            • Возвращает PDF-файл с этикетками; содержимое в поле `content` в виде байтов.
            • Доступно после формирования документов методом `posting_fbs_act_create()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFBSActGetContainerLabels

        Args:
            request: Запрос на получение этикеток по схеме `PostingFBSActGetContainerLabelsRequest`

        Returns:
            PDF-файл с этикетками по схеме `PostingFBSActGetContainerLabelsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_act_get_container_labels(
                    PostingFBSActGetContainerLabelsRequest(
                        id=12345
                    )
                )
                with open("labels.pdf", "wb") as f:
                    f.write(result.content)
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-container-labels",
            payload=request.model_dump(),
            response_format="binary"
        )
        return PostingFBSActGetContainerLabelsResponse(**response)
