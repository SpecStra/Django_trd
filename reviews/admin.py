from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "Filter by words"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("great", "Great"),
            ("awesome", "Awesome"),
        ]

    def queryset(self, request, reviews):
        if self.value() is not None:
            return reviews.filter(payload__contains=self.value())
        else :
            return reviews


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        # 모델의 str 메서드를 볼 수도 있습니다.
        "__str__",
        "payload"
    )
    list_filter = (
        "rating",
        "user__is_host",
        "room__category",
        WordFilter,
    )
