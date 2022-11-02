from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):

    def __str__(self) -> str:
        # 나중에 유저 수 표시
        return f"Chatting Room"

    user = models.ManyToManyField("users.User", related_name="chatting_rooms")


class Message(CommonModel):

    def __str__(self) -> str:
        return f"{self.user} says : {self.text}"

    text = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    room = models.ForeignKey("direct_messages.ChattingRoom", on_delete=models.CASCADE, related_name="messages")