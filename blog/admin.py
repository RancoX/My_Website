from django.contrib import admin
from .models import Post,BucketList

# Register your models here.
# so that user created data tables(models) appears on admin page
admin.site.register(Post)
admin.site.register(BucketList)
