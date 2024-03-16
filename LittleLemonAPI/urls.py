from django.urls import path

from . import views

urlpatterns = [
    path("menu-items", views.MenuItemsView.as_view({'get': 'list'})),
    path("menu-items/<int:pk>", views.MenuItemsView.as_view({'get': 'retrieve'})),
    path("cart/", views.CartItemsView.as_view({'get': 'list'})),
    path("order/", views.OrderItemsView.as_view({'get': 'list'}))

    # path("login/", views.user_login, name="login"),
    # path("signup/", views.user_signup, name="signup"),
    # path("logout/", views.user_logout, name="logout"),
    # path("signup/", views.CreateUserView.as_view()),
    # path("", views.MenuItemsView.as_view()),
]