from ...core import APIManager
from ...schemas.fbs import PostingFBSPackageLabelGetRequest, PostingFBSPackageLabelGetResponse


class PostingFBSPackageLabelGetMixin(APIManager):
    """Реализует метод /v1/posting/fbs/package-label/get"""

    async def posting_fbs_package_label_get(
            self: "PostingFBSPackageLabelGetMixin",
            request: PostingFBSPackageLabelGetRequest
    ) -> PostingFBSPackageLabelGetResponse:
        """Метод для получения этикеток после вызова `posting_fbs_package_label_create()`.

        Notes:
            • Метод используется для получения статуса формирования этикеток и ссылки на файл после создания задания.
            • Если статус формирования `COMPLETED`, в ответе будет ссылка на файл с этикетками.
            • Если статус `ERROR`, в ответе будет информация об ошибках для каждого отправления.
            • Рекомендуется выполнять запрос с интервалом в несколько секунд до получения статуса `COMPLETED`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PostingAPI_GetLabelBatch

        Args:
            request: Запрос на получение файла с этикетками по схеме `PostingFBSPackageLabelGetRequest`

        Returns:
            Результат получения файла с этикетками по схеме `PostingFBSPackageLabelGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_package_label_get(
                    PostingFBSPackageLabelGetRequest(
                        task_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/package-label/get",
            payload=request.model_dump()
        )
        return PostingFBSPackageLabelGetResponse(**response)