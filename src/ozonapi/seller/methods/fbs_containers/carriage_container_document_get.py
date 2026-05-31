from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerDocumentGetRequest,
    CarriageContainerDocumentGetResponse,
)


class CarriageContainerDocumentGetMixin(APIManager):
    """Реализует метод /v1/carriage/container/document/get"""

    async def carriage_container_document_get(
            self: "CarriageContainerDocumentGetMixin",
            request: CarriageContainerDocumentGetRequest
    ) -> CarriageContainerDocumentGetResponse:
        """Метод для получения документов по грузоместам — ТрН и лист отгрузки.

        Notes:
            • Содержимое файла приходит в поле `file_content` в виде строки (base64);
              декодируйте его для сохранения файла.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerDocumentGet

        Args:
            request: Запрос на получение документов по схеме `CarriageContainerDocumentGetRequest`

        Returns:
            Документы по грузоместам по схеме `CarriageContainerDocumentGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_document_get(
                    CarriageContainerDocumentGetRequest(
                        container_ids=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/document/get",
            payload=request.model_dump()
        )
        return CarriageContainerDocumentGetResponse(**response)
