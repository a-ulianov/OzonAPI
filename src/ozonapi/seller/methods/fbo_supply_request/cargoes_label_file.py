from ...core import APIManager
from ...schemas.fbo_supply_request import CargoesLabelFileResponse


class CargoesLabelFileMixin(APIManager):
    """Реализует метод /v1/cargoes-label/file/{file_guid}"""

    async def cargoes_label_file(
            self: "CargoesLabelFileMixin",
            file_guid: str
    ) -> CargoesLabelFileResponse:
        """Возвращает PDF-файл с этикетками грузомест по идентификатору файла.

        Notes:
            • Метод использует HTTP GET; `file_guid` подставляется в путь запроса.
            • Тело ответа — PDF-файл; содержимое в поле `content` в виде байтов.
            • `file_guid` выдаёт метод `cargoes_label_get()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyDraftAPI_CargoesLabelFile

        Args:
            file_guid: Идентификатор файла с этикетками

        Returns:
            PDF-файл с этикетками по схеме `CargoesLabelFileResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_file("a1b2c3")
                with open("cargo_labels.pdf", "wb") as f:
                    f.write(result.content)
        """
        response = await self._request(
            method="get",
            api_version="v1",
            endpoint=f"cargoes-label/file/{file_guid}",
            payload={},
            response_format="binary"
        )
        return CargoesLabelFileResponse(**response)
