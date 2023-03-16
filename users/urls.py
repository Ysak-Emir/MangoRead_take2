from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users import views

urlpatterns = [
    path('register/', views.RegisterUserView.as_view()),
    path('login2/', views.UserLoginAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #jwt login
    path('login_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), #jwt refresh token
    path('login_token/verify/', TokenVerifyView.as_view(), name='token_verify'), #jwt verify token
]