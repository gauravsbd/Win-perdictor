from django.urls import path
from .views import predict_win

urlpatterns = [
    path('', predict_win, name='predict_win'),
]