from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Songs
from .serializers import SongsSerializer

# Create your views here.

@api_view(['GET'])
def cars_list(request):
    songs = Songs.objects.all()

    serializer = SongsSerializer(songs, many=True)

    return Response(serializer.data)



