__all__ = ["SellerBrandAPI", ]

from .brand_company_certification_list import BrandCompanyCertificationListMixin


class SellerBrandAPI(
    BrandCompanyCertificationListMixin,
):
    """Реализует методы раздела «Сертификаты брендов».

    References:
        https://docs.ozon.ru/api/seller/#tag/BrandAPI
    """
    pass
