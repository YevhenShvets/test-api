from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from .models import Shop
from .serializers import ShopSerializer, get_json


@api_view(['GET'])
def shop_list(request):
    if request.method == 'GET':
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)
        content = get_json()

        return HttpResponse(json.dumps(content, indent=2), content_type='application/json')


@api_view(['GET'])
def shop_detail(request, pk):
    try:
        shop = Shop.objects.get(shop_id=pk)
    except Shop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShopSerializer(shop)
        content = get_json(shop.shop_id)

        return HttpResponse(json.dumps(content, indent=2), content_type='application/json')


