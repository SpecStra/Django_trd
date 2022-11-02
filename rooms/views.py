from rest_framework.views import APIView
from django.db import transaction
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, NotAuthenticated, ParseError
from .models import Amenity, Room
from categories.models import Category
from .serializer import AmenitySerializer, RoomSerializer, RoomListSerializer, RoomDetailSerializer


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(all_rooms, many=True)
        return Response(serializer.data)

    def post(self, reqeust):
        # user가 인증되어있는지(로그인 세션의 유저인지) 체크합니다.
        if reqeust.user.is_authenticated:
            # Data Receive
            serializer = RoomDetailSerializer(data=reqeust.data)


            if serializer.is_valid():
                # Category Validate
                category_pk = reqeust.data.get("category")
                if not category_pk :
                    # 400 Bad Request 를 발생시킵니다.
                    raise ParseError
                try :
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        raise ParseError
                except Category.DoesNotExist :
                    raise ParseError("Can't find that category :(")

                # atomic 내부에서 어떠한 오류라도 발생할 경우, DB에 기록되지 않게됩니다. - transaction
                try:
                    with transaction.atomic():
                        # owner=reqeust.user : 이런 형식으로 owner에 적합한 모양의 user를 할당할 수 있습니다.
                        # 정확히는 create 메서드의 validated_data에 자동으로 옵션을 넣어주는 기능입니다.
                        room = serializer.save(
                            owner=reqeust.user,
                            category=category
                        )

                        # amenity의 경우, 없더라도 허가되기 때문에 있을 경우 만들어진 뒤에 넣어주도록 합니다.
                        # Many To Many Field는 API가 다릅니다. add를 써야되고, 지울땐 remove를 씁니다.
                        amenities = reqeust.data.get("amenities")
                        for am in amenities :
                            # 만약 잘못된 am id가 올 경우, 아예 destroy 해버릴지, 아니면 해당 am만 넘어가고 만들지 골라야됩니다.
                            amenity = Amenity.objects.get(pk=am)
                            room.amenities.add(amenity)
                        serializer = RoomDetailSerializer(room)
                        return Response(serializer.data)
                except Exception :
                    raise ParseError("Amenity not found")
            else :
                return Response(serializer.errors)
        else :
            raise NotAuthenticated

class RoomDetail(APIView):
    def get_object(self, pk):
        try :
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound
    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(room)
        return Response(serializer.data)
    def put(self, request):
        pass
    def delete(self, request):
        pass

# /api/v1/rooms/amenities/1
class Amenities(APIView):

    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer =  AmenitySerializer(all_amenities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            # save()는 새롭게 생긴 객체를 자동으로 return합니다.
            new_amenity = serializer.save()
            # 새롭게 만들어졌으니 serializer도 해줘야 합니다.
            return Response(AmenitySerializer(new_amenity).data)
        else :
            return Response(serializer.errors)

class AmenityDetail(APIView):
    def get_object(self, pk):
        # 이 경우엔 404 오류가 생길 수 있으니, 컨트롤 해줘야 합니다.
        try :
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        that_amenity = self.get_object(pk)
        serializer = AmenitySerializer(that_amenity)
        return Response(serializer.data)

    def put(self, request, pk):
        that_amenity = self.get_object(pk)
        # 첫 번쨰 보이는건, DB에 있던 데이터고 두 번째 보이는건, 사용자가 보낸 데이터입니다.
        # partial은 반드시 둘 다 업데이트 되지 않고 둘 중 하나만 업데이트 될 수 있음을 명시합니다.
        serializer = AmenitySerializer(that_amenity, data=request.data, partial=True)
        if serializer.is_valid():
            updated_amenity = serializer.save()
            return Response(AmenitySerializer(updated_amenity).data)
        else :
            return Response(serializer.errors)


    def delete(self, request, pk):
        that_amenity = self.get_object(pk)
        that_amenity.delete()
        return Response(status=HTTP_204_NO_CONTENT)

"""
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request, "all_rooms.html", context={'rooms' : rooms, 'title' : "title for all rooms"})


def see_one_room(request, room_pk):
    try :
        room = Room.objects.get(pk=room_pk)
        print(room)
        return render(request, "room_detali.html", {"room" : room})
    except Room.DoesNotExist :
        return render(request, "maybe_404.html", {'not_found' : True})

"""