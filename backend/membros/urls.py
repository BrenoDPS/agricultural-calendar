from django.urls import path
from membros.views import (
    UserRegistrationAPIView,
    UserLoginAPIView,
    UserViewAPI,
    UserLogoutAPIView
)


urlpatterns = [
    path('', UserViewAPI.as_view()),
    path('register/', UserRegistrationAPIView.as_view()),
	path('login/', UserLoginAPIView.as_view()),
	path('logout/', UserLogoutAPIView.as_view()),
]