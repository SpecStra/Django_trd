from django.db import models


class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 이 모델은 DB에 넣기 위함이 아니라, 템플릿으로 사용하기 위함입니다. 그렇기에 아래와 같은 작업이 필요합니다.
    class Meta:
        abstract = True
