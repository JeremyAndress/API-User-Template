from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK, HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from rest_framework.reverse import reverse
from utils.paginator import CustomPagination
from app.user.models import User
from .controller import userController
from .serializers import UserSerializer

@api_view(['GET'])
def user_api_root(request, format=None):
    return Response({
        'getUsers': reverse('user:getUsers', request=request, format=format),
        'getUser': reverse('user:getUser', request=request, format=format),
    })

@api_view(['GET'])
def getUsers(request):
    paginator = CustomPagination()
    paginator.page_size = 3

    queryset = userController.getUsers()

    user = UserSerializer(queryset,many=True).data
    result_page = paginator.paginate_queryset(user, request)

    return paginator.get_paginated_response(result_page)

@api_view(['GET', 'PUT', 'DELETE'])
def getUser(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)