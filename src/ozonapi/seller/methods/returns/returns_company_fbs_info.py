from ...core import APIManager
from ...schemas.returns import (
    ReturnsCompanyFbsInfoRequest,
    ReturnsCompanyFbsInfoResponse,
)


class ReturnsCompanyFbsInfoMixin(APIManager):
    """Реализует метод /v1/returns/company/fbs/info"""

    async def returns_company_fbs_info(
            self: "ReturnsCompanyFbsInfoMixin",
            request: ReturnsCompanyFbsInfoRequest
    ) -> ReturnsCompanyFbsInfoResponse:
        """Метод для получения количества возвратов FBS по drop-off пунктам.

        Notes:
            • Возвращает drop-off пункты с количеством возвратов, коробок и пропусков.
            • Постраничный вывод через `pagination` (`limit` и `last_id`).

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsCompanyFbsInfo

        Args:
            request: Запрос на получение количества возвратов по схеме `ReturnsCompanyFbsInfoRequest`

        Returns:
            Информация о drop-off пунктах по схеме `ReturnsCompanyFbsInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_company_fbs_info(
                    ReturnsCompanyFbsInfoRequest(
                        pagination=ReturnsCompanyFbsInfoPagination(limit=100)
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/company/fbs/info",
            payload=request.model_dump()
        )
        return ReturnsCompanyFbsInfoResponse(**response)
