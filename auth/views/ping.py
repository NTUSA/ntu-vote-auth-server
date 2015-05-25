from django.conf import settings
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from core.views.utils import check_prerequisites, error, logger

@api_view(['POST'])
@check_prerequisites('station')
def ping(request):
    pass
