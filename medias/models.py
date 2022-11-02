from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    def __str__(self) -> str:
        return "Photo File"

    file = models.ImageField()
    description = models.CharField(max_length=140)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, null=True, blank=True, related_name="medias")
    experience = models.ForeignKey("experiences.Experience", on_delete=models.CASCADE, null=True, blank=True,
                                   related_name="medias")


class Video(CommonModel):

    def __str__(self) -> str:
        return "Video File"

    file = models.FileField()
    # One To One : 연결을 고유하게 만들 때 사용. 여러개가 되어선 안되는 상호연결 데이터에 사용됩니다.
    experience = models.OneToOneField("experiences.Experience", on_delete=models.CASCADE)