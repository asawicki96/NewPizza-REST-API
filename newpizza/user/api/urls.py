from django.urls import path, include
from . import views

urlpatterns = [
    path('user/create', views.UserRegistrationView.as_view(), name='register'),
    path('user/update/<pk>', views.UserUpdateView.as_view(), name='update'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/logout/', views.UserLogoutView.as_view(), name='logout'),
]
