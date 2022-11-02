from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializer import TinyUserSerializer
from categories.serializer import CategorySerializer

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description"
        )

class RoomSerializer(ModelSerializer):

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

#
class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "pk",
            "rooms_name",
            "country",
            "city",
            "price"
        )

class RoomDetailSerializer(ModelSerializer):

    # readonly속성을 줌으로써 post로 인한 생성 시 직접 작성된 owner의 정보를 요구받지 않게 됩니다.
    owner = TinyUserSerializer(read_only=True)
    # 그리고 이것들은 적어서 post할 수는 있겠지만, DB에 등록되지 않은 타입이라면 오류를 내보낼 것입니다.
    amenities = AmenitySerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Room
        fields = "__all__"
        depth = 1

