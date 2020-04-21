from django.urls import path, include
from . import views

urlpatterns = [
    path('user/create', views.UserRegistrationView.as_view(), name='register'),
    path('user/update/<pk>', views.UserUpdateView.as_view(), name='update'),
]
