from django.contrib import admin
from .models import SeekerCustomer
from .forms import SeekerCustomerForm


# Register your models here.
@admin.register(SeekerCustomer)
class SeekerCustomerAdmin(admin.ModelAdmin):
    list_display = ['company','contact_name','token','created','used','balance']
    list_filter = ['company','contact_name','created']
    search_fields = ['company','contact_name']
    ordering = ['company','-created']
    form = SeekerCustomerForm