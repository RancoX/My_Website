from django.urls import path, register_converter
from django.http import Http404
from .views import seeker, authenticate
import uuid

class MyUUIDConverter:
    regex = '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}'

    def to_python(self, value):
        try: 
            converted=uuid.UUID(value)
        except ValueError:
            return Http404('Invalid license key')
        return converted

    def to_url(self, value):
        return str(value)
    

register_converter(MyUUIDConverter,'myuuid')

urlpatterns = [
    path('',seeker,name='seeker'),
    path('token/<myuuid:uuid>/',authenticate,name='check_token'),
]
