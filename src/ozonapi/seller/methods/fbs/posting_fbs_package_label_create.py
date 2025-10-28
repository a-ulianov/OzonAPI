from ...core import APIManager
from ...schemas.fbs import PostingFBSPackageLabelCreateRequest, PostingFBSPackageLabelCreateResponse


class PostingFBSPackageLabelCreateMixin(APIManager):
    """Реализует метод /v2/posting/fbs/package-label/create"""

    async def posting_fbs_package_label_create(
            self: "PostingFBSPackageLabelCreateMixin",
            request: PostingFBSPackageLabelCreateRequest
    ) -> PostingFBSPackageLabelCreateResponse:
        """Метод для создания задания на формирование этикеток для отправлений.

        Notes:
            • Метод применим только для отправлений в статусе «Ожидает отгрузки» — `awaiting_deliver`.
            • Метод может вернуть несколько заданий: на формирование маленькой и большой этикетки.
            • Для получения созданных этикеток используйте метод `posting_fbs_package_label_get()`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_CreateLabelBatchV2

        Args:
            request: Запрос на создание задания на формирование этикеток по схеме `PostingFBSPackageLabelCreateRequest`

        Returns:
            Результат создания задания на формирование этикеток по схеме `PostingFBSPackageLabelCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_package_label_create(
                    PostingFBSPackageLabelCreateRequest(
                        posting_number=["4708216109137", "3697105098026"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/package-label/create",
            payload=request.model_dump()
        )
        return PostingFBSPackageLabelCreateResponse(**response)