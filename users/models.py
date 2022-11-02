from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    class GenderChoice(models.TextChoices) :
        # 튜플의 이름은 프런트엔드에 보이게 될 이름
        # 튜플의 0번 원소는 데이터베이스에 기록될 value
        # 튜플의 1번 원소는 관리자패널에서 보게 될 label입니다.
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoice(models.TextChoices) :
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoice(models.TextChoices) :
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

    first_name = models.CharField(max_length=150, editable=False, )
    last_name = models.CharField(max_length=150, editable=False, )
    name = models.CharField(max_length=150, default="", )
    is_host = models.BooleanField(default=False, )
    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, )
    language = models.CharField(max_length=2, choices=LanguageChoice.choices, )
    currency = models.CharField(max_length=5, choices=CurrencyChoice.choices, )
