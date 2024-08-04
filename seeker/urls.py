from django.urls import path
from .views import seeker

urlpatterns = [
    path('',seeker,name='seeker'),
]
