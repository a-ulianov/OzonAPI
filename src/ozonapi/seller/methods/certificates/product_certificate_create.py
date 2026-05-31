import aiohttp

from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateCreateRequest,
    ProductCertificateCreateResponse,
)


class ProductCertificateCreateMixin(APIManager):
    """Реализует метод /v1/product/certificate/create"""

    async def product_certificate_create(
            self: "ProductCertificateCreateMixin",
            request: ProductCertificateCreateRequest
    ) -> ProductCertificateCreateResponse:
        """Метод для добавления сертификатов для товаров.

        Notes:
            • Запрос отправляется как `multipart/form-data`: текстовые поля и файлы `files`.
            • Допустимые расширения файлов уточняйте в документации Ozon.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateCreate

        Args:
            request: Запрос на добавление сертификата по схеме `ProductCertificateCreateRequest`

        Returns:
            Идентификатор созданного сертификата по схеме `ProductCertificateCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                with open("cert.pdf", "rb") as f:
                    result = await api.product_certificate_create(
                        ProductCertificateCreateRequest(
                            files=[f.read()],
                            name="Сертификат",
                            number="RU-123",
                            type_code="certificate",
                            issue_date="2026-01-01T00:00:00Z"
                        )
                    )
        """
        form_data = aiohttp.FormData()
        form_data.add_field("name", request.name)
        form_data.add_field("number", request.number)
        form_data.add_field("type_code", request.type_code)
        form_data.add_field("issue_date", request.issue_date)
        if request.accordance_type_code is not None:
            form_data.add_field("accordance_type_code", request.accordance_type_code)
        if request.expire_date is not None:
            form_data.add_field("expire_date", request.expire_date)
        for index, file_content in enumerate(request.files):
            form_data.add_field(
                "files",
                file_content,
                filename=f"certificate_{index}",
                content_type="application/octet-stream",
            )

        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/create",
            form_data=form_data
        )
        return ProductCertificateCreateResponse(**response)
