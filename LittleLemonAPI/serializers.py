from rest_framework import serializers
from .models import MenuItem, Category, User, Cart, DeliveryCrew, Order
from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model


UserModel = get_user_model()

class OrderSerializer(serializers.ModelSerializer):
    delivery_crew = serializers.PrimaryKeyRelatedField(
        queryset = DeliveryCrew.objects.all(),
        default = serializers.CurrentUserDefault()
    )

    customer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    cart = serializers.PrimaryKeyRelatedField(
        queryset = Cart.objects.all(),
        default = serializers.CurrentUserDefault()
    )

    class Meta:
        model = Order
        fields = ['delivery_status', 'cart', 'customer','delivery_crew']

class CartSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Cart
        fields = ['customer', 'items']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ["id", "username", "password"] 

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'category', 'featured']
        depth = 1 # think of this as category can go into 1 depth
