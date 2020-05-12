from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('orderitems', views.OrderItemViewSet)
router.register('orders', views.OrderViewSet)

urlpatterns = [
    path('orders/', views.CreateOrder.as_view(), name='create_order'),
    path('orderitems/', views.CreateOrderItem.as_view(), name='create_orderitem'),
    path('', include(router.urls)),
    
]