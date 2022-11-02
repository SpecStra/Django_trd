from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # 이런식으로 하면 모든 필드 공개입니다. -> fields = "__all__"
        # 아래와 같은 식으로 하면, 제외할 것만 빼고 필드를 보여줍니다.
        fields = (
            "name",
            "kind",
        )
