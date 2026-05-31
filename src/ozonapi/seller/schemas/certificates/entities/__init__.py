"""Общие вложенные модели раздела Сертификаты качества."""
__all__ = [
    "CertificateCodeName",
    "CertificateNameValue",
    "Certificate",
]

from .certificate import Certificate
from .certificate_code_name import CertificateCodeName
from .certificate_name_value import CertificateNameValue
