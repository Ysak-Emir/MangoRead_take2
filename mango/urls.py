from django.urls import path
from mango import views

urlpatterns = [
    path('card_create/', views.MangoCardCreateAPIView.as_view()),
    path('card/', views.MangoCardAPIView.as_view()),
]