from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK
)
from rest_framework.response import Response
from utils.paginator import CustomPagination

@api_view(['GET'])
def getUsers(request):
    paginator = CustomPagination()
    paginator.page_size = 10