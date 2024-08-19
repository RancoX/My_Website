from .models import BucketList
from django import forms

class BucketListForm(forms.ModelForm):
    class Meta:
        model = BucketList
        fields= ['name','link']
