from django.db import models
from common.models import CommonModel


class Category(CommonModel):

    def __str__(self) -> str:
        return f"{self.kind.title()} : {self.name}"

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    # Room, or Experience Category
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=30, choices=CategoryKindChoices.choices)

    class Meta:
        verbose_name_plural = "categories"
