from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import FileResponse
from django.conf import settings
from .models import Post,BucketList
from datetime import datetime
import os, requests, json
from .forms import BucketListForm

# dummy posts
# posts=[
#     {'author':'Ranco Xu','title':'My first post!','content':'This is my first ever post!','date_posted':'Apr 24, 2022'},
#     {'author':'Claire Gao','title':'Blog post 2','content':'I never know i can post here!','date_posted':'Sep 21, 2019'},
# ]
# Create your views here.
def home(request):
    context = {
        'all_posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'all_posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'all_posts'
    paginate_by = 5

    def get_queryset(self):
        # get all posts associate with a particular user
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # send user back to home page after deletion
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    Coco_Claire = 'media/Coco_Claire.jpg'
    context = {'title': 'About Myself', 'pic1': Coco_Claire}
    return render(request, 'blog/about.html', context)


def contactme(request):
    when = datetime.now().hour
    if when >= 5 and when <= 12:
        when = 'Morning'
    elif when > 12 and when <= 18:
        when = 'Afternoon'
    else:
        when = 'Evening'

    linkedin_pic = 'media/Professional_pic.jpeg'
    context = {'title': 'Contact Me', 'when': when, 'linkedin_pic':linkedin_pic}
    return render(request, 'blog/contactme.html', context)


def portfolio(request):
    return render(request, 'blog/portfolio.html')


def dadjoke(request):
    res=requests.get(r'https://icanhazdadjoke.com',headers={"Accept":"application/json"})
    joke=json.loads(res.text)['joke']
    context={'joke':joke}
    return render(request, 'blog/dadjoke.html',context)

def download_resume(request):
    file_path=settings.BASE_DIR / 'blog/resume_rancoxu_jun_2024.pdf'
    #with open(file_path, 'rb') as pdf_file:
        #pdf_data = pdf_file.read()
    response = FileResponse(open(file_path,'rb'), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Resume_RancoXu.pdf"'
    return response

def bucket_list(request,action=None,item_id=None):
    form = BucketListForm()
    if request.method == 'POST':
        if action == 'create':
            form = BucketListForm(request.POST)
            if form.is_valid():
                new_item = form.save(commit=False)
                # add in user id
                new_item.author = request.user
                new_item.save()

        elif action == 'delete':
            item2del = get_object_or_404(BucketList, id=item_id)
            item2del.delete()

        elif action == 'edit':
            pass

    items = BucketList.objects.all()

    context = {'items': items,'form':form}
    return render(request,'blog/bucket_list.html',context)
