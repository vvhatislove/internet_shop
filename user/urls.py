from django.urls import path

from user.views import RegisterUserView, LoginUserView, logout_user_view

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_user_view, name='logout'),
]
