from django.urls import path
from mango import views

urlpatterns = [
    path('card_list/', views.MangoCardListAPIView.as_view()),
    path('card_create/', views.MangoCardCreateAPIView.as_view()),
    path('card_detail/<int:id>', views.MangoCardDetailAPIView.as_view()),
    path('review_create/', views.ReviewCreateAPIView.as_view()),
    path('review_list/', views.ReviewListAPIView.as_view()),
]