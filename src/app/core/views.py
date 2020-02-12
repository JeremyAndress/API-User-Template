from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.shortcuts import render

def email_send(request):
    from utils.emailback import send_email
    '''Bootstrapemail parsea html para ser renderizado por email'''
    #https://bootstrapemail.com
    send_email()
    return render(request,'email/activate.html')

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'User': reverse('user:user_api_root', request=request, format=format),
    })

