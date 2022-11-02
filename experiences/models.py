from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    def __str__(self) -> str:
        return self.name

    country = models.CharField(max_length=50, default="Korea", )
    city = models.CharField(max_length=80, default="Seoul", )
    name = models.CharField(max_length=250)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="experience")
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250)
    start_at = models.TimeField()
    end_at = models.TimeField()
    description = models.TextField()

    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="experience")


class Perk(CommonModel):

    def __str__(self) -> str:
        return self.name

    # 활동 포함 사항
    name = models.CharField(max_length=100, )
    details = models.CharField(max_length=250, blank=True, null=True, )
    explanation = models.TextField(blank=True, null=True, )

