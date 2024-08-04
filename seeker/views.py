from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .seek_crawler import get_all_pages, API_URL, headers, file_name_formatter
from django.conf import settings
from .forms import SeekerForm

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
