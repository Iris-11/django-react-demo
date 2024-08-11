from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_data(request):
    data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    return Response(data)
