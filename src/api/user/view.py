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
        'getUser': reverse('user:getUser',request=request, format=format),
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


@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def signin(request):
    logger.info('Signin')
    try:
        user = User.objects.get(username=request.data.get("username",""))
    except User.DoesNotExist:
        return Response({'Error': "Invalid username"}, status="400")
    if not DEBUG:
        url_ = os.getenv('AUTORIZACION_URL', 'http://10.181.24.239/assets/loginSap.asp')
        params_ = {
            'rut':request.data.get("username",""),
            'clave':request.data.get("password","")
            } 
        logger.info('URL : {} Params : {}'.format(url_,params_))
        exist = requests.get(url = url_, params = params_) 
        logger.info('User {0} Exist {1}'.format(user,exist.content))
        logger.info('Type {}'.format(type(exist.content)))
        if exist.content == b'false':
            return Response({'Error': "Invalid username or password"}, status="400")
    
    aut = UserAuthority.objects.filter(id_user=user).values('id_authority__nombre')
    authorities = [ {'authority': i['id_authority__nombre'] } for i in aut  ]

    token,data = Token.objects.get_or_create(user = user)
   
    is_expired, token = token_expire_handler(token)  
  
    nombre = user.first_name+' '+user.last_name+' '+user.last_name2
    context = {
        'username':user.username,
        'nombre':nombre,
        'expires_in': expires_in(token),
        'token': token.key,
        'date_expire': date_expire(token), 
        'authorities': authorities,
        'cencos': user.profile.cencos
    }
    return Response(context,status=HTTP_200_OK)