from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import Product_Serializer, Create_Product_Serializer
from .models import Product
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def products(request):
    products = Product.objects.order_by("-id")
    serializer = Product_Serializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def single_product(request, id):
    product = get_object_or_404(Product, id=id)
    serializer = Product_Serializer(product)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = Create_Product_Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save(seller=request.user)
        message = serializer.data
    else:
        message = serializer.errors
    return Response(message)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def filter_products(request):
    seller = request.GET.get("seller")
    order = request.GET.get("order")
    if seller:
        all_products = Product.objects.filter(seller__username__icontains=seller)
        if order == "high":
            products = all_products.order_by("-price")
        else:
            products = all_products.order_by("price")
        serializer = Product_Serializer(products, many=True)
        message = {"result": f"{products.count()} products found", "products": serializer.data}
    else:
        message = {"message": "invalid username"}
    return Response(message)
