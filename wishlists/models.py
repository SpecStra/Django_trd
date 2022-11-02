from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):

    def __str__(self) -> str:
        return self.name

    # Rooms와 Exper의 즐겨찾기 같은겁니다.
    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField("rooms.Room", related_name="wishlists")
    experiences = models.ManyToManyField("experiences.Experience", related_name="wishlists")
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="wishlists")