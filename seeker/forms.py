from django import forms
from .seek_crawler import classifications

classification_choices = [(k,k) for k in classifications.keys()]

class SeekerForm(forms.Form):
    keyword = forms.CharField(max_length=200)
    subclassification = forms.ChoiceField(choices=classification_choices,widget=forms.Select,label='Classification',required=False)
    location = forms.CharField(max_length=100, initial='brisbane')
    pages_to_parse = forms.IntegerField(min_value=1,max_value=30,initial=3,label='Pages to parse')
    expiry = forms.IntegerField(min_value=1,max_value=60,initial=14,label='Exclude jobs from n days ago')