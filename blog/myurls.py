from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # '' path means /home
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('contactme/', views.contactme, name='blog-contactme'),
    path('portfolio/', views.portfolio, name='blog-portfolio'),
    path('dadjoke/',views.dadjoke,name='dadjoke'),
    path('get-my-resume',views.download_resume,name='download_resume'),
    path('bucketlist/',views.bucket_list,name='bucket_list_all'),
    path('bucketlist/<action>/<int:item_id>/',views.bucket_list,name='bucket_list'),
]
