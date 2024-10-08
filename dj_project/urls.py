"""dj_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from all_users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls.base import reverse_lazy
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.myurls')),
    path('register/', user_views.register, name='user_register'),
    path('profile/', user_views.profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='all_users/login.html'),
         name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='all_users/logout.html'), name='user_logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='all_users/password_reset.html', success_url=reverse_lazy("pw_reset_done")), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='all_users/password_reset_done.html'), name='pw_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='all_users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='all_users/password_reset_complete.html'), name='password_reset_complete'),
    path('seeker/',include('seeker.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
