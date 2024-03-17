from django.shortcuts import redirect, render
from rest_framework import generics, permissions
from .models import MenuItem, Category, Cart, Order
from .serializers import MenuItemSerializer, UserSerializer, CategorySerializer, CartSerializer, OrderSerializer
from .forms import UserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets 

class MenuItemsView(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price']
    search_fields=['category__name']
    lookup_field = 'name'

    def get_permissions(self):
        if(self.request.method=='GET'):
            return []
    
        return [IsAuthenticated()]


class OrderItemsView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        if(self.request.method=='GET' or self.request.method=='POST'):
            return []

        return [IsAuthenticated()]

class CartItemsView(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user)

    def perform_create(self, serializer):
        item = self.request.data.get('item')
        serializer.save(user=self.request.user)

    def delete(self, request):
        user = self.request.user
        Cart.objects.filter(user=user).delete()
        return Response(status=204)

    def get_permissions(self):
        if(self.request.method=='GET' or self.request.method=='POST'):
            return []

        return [IsAuthenticated()]
    
class ManagerView(viewsets.ModelViewSet):
    def get_permissions(self):
        if(self.request.method=='GET' or self.request.method=='POST'):
            return []

        return [IsAuthenticated()]
        # request.user.groups.filter(name='Manager').exists()
