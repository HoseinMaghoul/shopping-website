from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
    path('category/<slug:slug>/', views.home, name='category_filter')
]