from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
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
        'signin': reverse('user:signin',request=request, format=format),
        'getUsers': reverse('user:getUsers', request=request, format=format),
        'getUser': reverse('user:getUser',request=request, format=format),
        'signup' : reverse('user:signup',request=request, format=format),
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
def getUser(request):
    pk = request.query_params.get('pk', None)
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

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)



@api_view(['POST'])
# @permission_classes((AllowAny,))
def signin(request):
    from django.contrib.auth import authenticate
    from rest_framework.authtoken.models import Token
    from utils.token import token_expire_handler, expires_in, date_expire
    try:
        username = request.data.get("username","")
        password = request.data.get("password","")
        user = authenticate(username=username, password=password)
        if user:
            token,data = Token.objects.get_or_create(user = user)
            is_expired, token = token_expire_handler(token)  
            context = {
                'username':user.username,
                'expires_in': expires_in(token),
                'token': token.key,
                'date_expire': date_expire(token), 
            }
            return Response(context,status=HTTP_200_OK)
    except Exception as e:
        return Response(status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def signup(request):
    try:
        username = request.data.get("username",None)
        email = request.data.get("email",None)
        password = request.data.get("password",None)
        if None in [username,email,password]:
            context = 'You must write in all fields'
            return Response(context,status=HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
            context = 'Username already exist'
            return Response(context,status=HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            create = {'username':username,'email':email,'password':password}
            user = User.objects.create_user(**create)
            user.save()
            context = 'User Created'
            return Response(context,status=HTTP_200_OK)
    except Exception as e:
        return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def signup_email(request):
    from utils.emailback import send_email 
    try:
        username = request.data.get("username",None)
        email = request.data.get("email",None)
        password = request.data.get("password",None)
        if None in [username,email,password]:
            context = 'You must write in all fields'
            return Response(context,status=HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=username)
            context = 'Username already exist'
            return Response(context,status=HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            create = {'username':username,'email':email,'password':password,'is_active':False}
            user = User.objects.create_user(**create)
            user.save()
            context = 'User Created, Check your email'
            return Response(context,status=HTTP_200_OK)
    except Exception as e:
        return Response(status=HTTP_400_BAD_REQUEST)