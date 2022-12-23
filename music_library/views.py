from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Songs
from .serializers import SongsSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def song_detail(request, pk):
    try:
        song = Songs.objects.get(pk=pk)
        serializer = SongsSerializer(song)
        return Response(serializer.data)
    except Songs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
