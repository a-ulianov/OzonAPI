import datetime
from pydantic import field_validator


class DateTimeSerializationMixin:
    """Миксин для сериализации datetime полей"""

    @classmethod
    def create_datetime_validator(cls, field_names):
        @field_validator(*field_names, mode='after')
        def serialize_datetime(cls, value):
            """Сериализует значение datetime.datetime в строку"""
            if isinstance(value, datetime.datetime):
                if value.tzinfo is None:
                    value = value.replace(tzinfo=datetime.timezone.utc)

                utc_dt = value.astimezone(datetime.timezone.utc)
                return utc_dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            return value

        return serialize_datetime