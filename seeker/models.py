from django.db import models
import uuid

# Create your models here.
class SeekerCustomer(models.Model):
    token = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    company = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=100,blank=True)
    contact_email = models.EmailField(blank=True,null=True)
    contact_number = models.CharField(max_length=50,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    expiry = models.DateField(null=True)
    used = models.IntegerField(default=0)
    balance = models.IntegerField(default=50_000)

    class Meta:
        db_table = 'customer_tokens'
        indexes = [
            models.Index(fields=['token',]),
        ]

    def __str__(self):
        return f"{self.company}: {self.balance} queries left"