from tortoise import fields
from tortoise.models import Model


class Tariff(Model):
    cargo_type = fields.CharField(max_length=100)
    rate = fields.DecimalField(max_digits=5, decimal_places=5)
    date = fields.DateField()

    class Meta:
        table = "tariffs"
