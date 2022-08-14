from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from datetime import datetime


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
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'all_posts'
    paginate_by = 3

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
    when = datetime.now().hour
    if when >= 4 and when <= 11:
        when = 'Morning'
    else:
        when = 'Evening'
    context = {'title': 'About Me', 'when': when}
    return render(request, 'blog/about.html', context)
