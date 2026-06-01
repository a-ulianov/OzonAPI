from ...core import APIManager
from ...schemas.passes import (
    ReturnPassDeleteRequest,
    ReturnPassDeleteResponse,
)


class ReturnPassDeleteMixin(APIManager):
    """Реализует метод /v1/return/pass/delete"""

    async def return_pass_delete(
            self: "ReturnPassDeleteMixin",
            request: ReturnPassDeleteRequest
    ) -> ReturnPassDeleteResponse:
        """Удаляет пропуска на склад для вывоза возвратов.

        Notes:
            • Удаляет пропуска по их идентификаторам.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/returnPassDelete

        Args:
            request: Запрос на удаление пропусков для возврата по схеме
                `ReturnPassDeleteRequest`

        Returns:
            Пустой ответ по схеме `ReturnPassDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.return_pass_delete(
                    ReturnPassDeleteRequest(arrival_pass_ids=[456, 789])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/pass/delete",
            payload=request.model_dump()
        )
        return ReturnPassDeleteResponse(**response)
