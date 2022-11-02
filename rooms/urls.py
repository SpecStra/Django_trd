from django.urls import path
from . import views


urlpatterns = [
    path("", views.Rooms.as_view()),
    path("<int:pk>", views.RoomDetail.as_view()),
    path("amenities/", views.Amenities.as_view()),
    path("amenities/<int:pk>", views.AmenityDetail.as_view())
]

"""
urlpatterns = [
    path("", views.see_all_rooms),
    # 아래와 같이 url 방식으로 이뤄집니다. 꺽쇠열고 자료형:별칭 식으로 지정해줍니다.
    path("<int:room_pk>", views.see_one_room),
]
"""
