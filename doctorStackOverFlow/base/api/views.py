from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getRoutes(requests):
    routes = ['GET api/rooms',
              'GET api/rooms/:id'
              ]
    return Response(routes)


@api_view(['GET'])
def getRooms(requests):
    rooms = Room.objects.all()
    return Response(RoomSerializer(rooms, many=True).data)


@api_view(['GET'])
def getRoom(requests, pk):
    room = Room.objects.get(id=pk)
    return Response(RoomSerializer(room).data)
