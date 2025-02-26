from django.urls import path
from products import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('products/', views.products, name='products'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]