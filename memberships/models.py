from django.db import models


class Membership(models.Model):
    MEMBERSHIP_TYPES = (
        ("Free", "free"),
        ("Professional", "pro"),
        ("Enterprise", "ent"),
    )
    slug = models.SlugField(max_length=128)
    membership_type = models.CharField(
        choices=MEMBERSHIP_TYPES, max_length=54, default="Free"
    )
    stripe_plan_id = models.CharField("Stripe Plan Id", max_length=128)
    price = models.DecimalField("Price", max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return self.membership_type
