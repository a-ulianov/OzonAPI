from ...core import APIManager
from ...schemas.fbs_delivery import (
    CarriageActDiscrepancyPDFRequest,
    CarriageActDiscrepancyPDFResponse,
)


class CarriageActDiscrepancyPDFMixin(APIManager):
    """Реализует метод /v1/carriage/act-discrepancy/pdf"""

    async def carriage_act_discrepancy_pdf(
            self: "CarriageActDiscrepancyPDFMixin",
            request: CarriageActDiscrepancyPDFRequest
    ) -> CarriageActDiscrepancyPDFResponse:
        """Метод для получения акта о расхождениях по отгрузке FBS.

        Notes:
            • Возвращает PDF-файл акта в поле `content` в виде строки (base64).
            • Декодируйте `content` из base64 для сохранения файла.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageActDiscrepancyPDF

        Args:
            request: Запрос на получение акта о расхождениях по схеме `CarriageActDiscrepancyPDFRequest`

        Returns:
            Акт о расхождениях по схеме `CarriageActDiscrepancyPDFResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_act_discrepancy_pdf(
                    CarriageActDiscrepancyPDFRequest(
                        carriage_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/act-discrepancy/pdf",
            payload=request.model_dump()
        )
        return CarriageActDiscrepancyPDFResponse(**response)
