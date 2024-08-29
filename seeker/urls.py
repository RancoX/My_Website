from django.urls import path
from .views import seeker, authenticate

urlpatterns = [
    path('',seeker,name='seeker'),
    path('token/<uuid:uuid>',authenticate,name='check_token'),
]
