from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerLabelGetRequest,
    CarriageContainerLabelGetResponse,
)


class CarriageContainerLabelGetMixin(APIManager):
    """Реализует метод /v1/carriage/container/label/get"""

    async def carriage_container_label_get(
            self: "CarriageContainerLabelGetMixin",
            request: CarriageContainerLabelGetRequest
    ) -> CarriageContainerLabelGetResponse:
        """Метод для получения этикетки по грузоместам.

        Notes:
            • Содержимое этикетки приходит в поле `content.file_content` в виде строки (base64).
            • По грузоместам с ошибками формирования возвращается список `error_containers`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerLabelGet

        Args:
            request: Запрос на получение этикетки по схеме `CarriageContainerLabelGetRequest`

        Returns:
            Этикетка по грузоместам по схеме `CarriageContainerLabelGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_label_get(
                    CarriageContainerLabelGetRequest(
                        container_ids=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/label/get",
            payload=request.model_dump()
        )
        return CarriageContainerLabelGetResponse(**response)
