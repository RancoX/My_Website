from django.urls import path
from .views import seeker, authenticate

urlpatterns = [
    path('',seeker,name='seeker'),
    path('token/<str:uuid>',authenticate,name='check_token'),
]
