from src.ozonapi.seller.schemas.fbs import (
    PostingFBSTarifficationStep,
    PostingFBSTarifficationCharge,
)


class TestTarifficationStep:
    """Тесты модели шага тарификации (tariffication_steps)."""

    def test_parses_real_money_object_shape(self):
        """Проверяет разбор реальной формы шага: charge — money-объект, rate — число."""
        step = PostingFBSTarifficationStep(
            min_charge=None,
            tariff_charge={"amount": "1472", "currency": "RUB"},
            tariff_deadline_at="2026-06-01T00:09:00Z",
            tariff_rate=3,
            tariff_type="discount",
        )
        assert isinstance(step.tariff_charge, PostingFBSTarifficationCharge)
        assert step.tariff_charge.amount == "1472"
        assert step.tariff_charge.currency == "RUB"
        assert step.tariff_rate == 3.0
        assert step.tariff_type == "discount"
        assert step.min_charge is None
        assert step.tariff_deadline_at is not None

    def test_all_fields_optional(self):
        """Пустой шаг допустим (все поля опциональны)."""
        step = PostingFBSTarifficationStep()
        assert step.tariff_charge is None
        assert step.tariff_type is None
