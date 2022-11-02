from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"

    # User's review on rooms or experiences
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="reviews")
    room = models.ForeignKey("rooms.Room", null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    experience = models.ForeignKey("experiences.Experience", null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    payload = models.TextField()
    rating = models.PositiveIntegerField()
