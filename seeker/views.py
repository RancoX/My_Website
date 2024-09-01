from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .seek_crawler import get_all_pages, API_URL, headers, file_name_formatter
from django.conf import settings
from .forms import SeekerForm
from .models import SeekerCustomer
from django.core.exceptions import ValidationError

# Create your views here.
@login_required
def seeker(request):
    if request.method == 'POST':
        form = SeekerForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            subclassification = form.cleaned_data['subclassification']
            location = form.cleaned_data['location']
            pages_to_parse = form.cleaned_data['pages_to_parse']
            filename = file_name_formatter(keyword,subclassification,location).split('.')[0]

            # call seeker function
            SAVE_DIR = settings.BASE_DIR / 'seeker/data'
            outputs, _ = get_all_pages(API_URL,headers,keyword,subclassification,location,pages_to_parse,SAVE_DIR)
            # GET request
            context = {
                'title': filename,
                'outputs': outputs
            }
    else:
        form = SeekerForm()
        context = {
            'title': 'Seeker Bulletin Board',
            'form': form,
        }
    return render(request,'seeker/homepage.html',context)

def authenticate(request,uuid=None):
    if request.method == 'GET':
        # if there is uuid included in request body
        # verify existing token
        try:
            customer = SeekerCustomer.objects.get(pk=uuid)
        except SeekerCustomer.DoesNotExist:
            # correct format, wrong key
            return JsonResponse({'query_allowed':False})

        # if found token, check if balance is sufficient
        if customer.balance>0:
            return JsonResponse({'query_allowed':True,'queries_remaining':customer.balance})
        return JsonResponse({'query_allowed':False,'queries_remaining':0})
        # if no uuid, create one


def spent_one_query(request,uuid=None):
    if request.method == 'GET':
        # if there is uuid included in request body
        # verify existing token
        try:
            customer = SeekerCustomer.objects.get(pk=uuid)
        except SeekerCustomer.DoesNotExist:
            # correct format, wrong key
            return JsonResponse({'query_allowed':False})

        # if found token, check if balance is sufficient
        if customer.balance>0:
            customer.used += 1
            customer.balance -= 1
            customer.save()
            return JsonResponse({'query_allowed':True,'queries_remaining':customer.balance})
        return JsonResponse({'query_allowed':False,'queries_remaining':0})