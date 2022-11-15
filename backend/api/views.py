import json
# from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.forms.models import model_to_dict
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """DRF API VIEW"""
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # To save data sent through 'POST' to the db
            # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)