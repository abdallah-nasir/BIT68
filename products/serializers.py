from rest_framework import serializers
from .models import Product


class Product_Serializer (serializers.ModelSerializer):
    category = serializers.SerializerMethodField("get_category")
    seller = serializers.SerializerMethodField("get_seller")

    class Meta:
        model = Product
        fields = "__all__"

    def get_category(self, product):
        return product.category.name

    def get_seller(self, product):
        return product.seller.username


class Create_Product_Serializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {"seller": {"read_only": True}, "category": {"required": True}, "price": {"required": True}}
