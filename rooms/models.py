from django.db import models
from common.models import CommonModel


class Room(CommonModel):

    def __str__(self) -> str:
        return f"{self.rooms_name} in {self.city}"

    class RoomKindChoice(models.TextChoices):
        ENTIRE_PLACE = "entire_place", "Entire Place"
        PRIVATE_ROOM = "private_room", "Private Room"
        SHARED_ROOM = "shared_room", "Shared Room"

    # 일단 문자열로 해두고, 나중에 라이브러리로 나라 선택하도록 할게요.
    country = models.CharField(max_length=50, default="Korea", )
    city = models.CharField(max_length=80, default="Seoul", )
    price = models.PositiveIntegerField()
    rooms_name = models.CharField(max_length=180, default="", null=True, )
    rooms_amount = models.PositiveIntegerField()
    toilets_amount = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250, )
    pet_friendly = models.BooleanField(default=True, )
    rooms_kind = models.CharField(max_length=20, choices=RoomKindChoice.choices, )
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="rooms")

    amenities = models.ManyToManyField("rooms.Amenity")
    category = models.ForeignKey("categories.Category", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="rooms")

    def review_rating(self):
        count = self.reviews.count()
        if count == 0 :
            return "No reviews"
        else:
            total_reviews = 0
            for review in self.reviews.all().values("rating"):
                total_reviews += review["rating"]
            return round(total_reviews/self.reviews.count(), 1)


class Amenity(CommonModel):

    def __str__(self) -> str:
        return self.name

    # Amenity Definition

    name = models.CharField(max_length=150, )
    description = models.CharField(max_length=150, null=True, blank=True, )

    class Meta:
        verbose_name_plural = "Amenities"
