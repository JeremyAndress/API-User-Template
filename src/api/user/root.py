from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def user_api_root_detail(request, format=None):
    return Response({
        'signin': {
            'url': reverse('user:signin',request=request, format=format),
            'description': 'Login Application',
            'methods': 'POST',
            'parameters': ['username','password']
        },
        'getUsers': {
            'url': reverse('user:getUsers', request=request, format=format),
            'description':'Get all user',
            'methods': 'GET'
        },
        'getUser': {
            'url': reverse('user:getUser',request=request, format=format),
            'description': 'Get One User',
            'methods': ['GET','PUT','DELETE'],
            'parameters': ['pk']
        }

    })

