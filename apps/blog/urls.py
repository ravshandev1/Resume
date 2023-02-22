from django.urls import path
from .views import single

urlpatterns = [
    path('single/<int:pk>/', single, name='single')
]
