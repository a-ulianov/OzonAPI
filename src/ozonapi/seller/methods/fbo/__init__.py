__all__ = ["SellerFBOAPI", ]

from .posting_fbo_cancel_reason_list import PostingFBOCancelReasonListMixin
from .posting_fbo_get import PostingFBOGetMixin
from .posting_fbo_list import PostingFBOListMixin


class SellerFBOAPI(
    PostingFBOCancelReasonListMixin,
    PostingFBOGetMixin,
    PostingFBOListMixin,
):
    """Реализует методы раздела Доставка FBO.

    References:
        https://docs.ozon.com/api/seller/?#tag/FBO
    """
    pass