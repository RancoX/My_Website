import re
from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# messages.debug/info/success/warning/error

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pw=form.cleaned_data.get('password1')
            messages.success(request,f"Account successfully created for {username} with pw: {pw}, now able to login!")
            return redirect('user_login')
    
    else:
        form=UserRegisterForm()

    return render(request,'all_users/register.html',{'form':form})

# require user to log in before proceed
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,"Your account has been updated!")
            return redirect('user_profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={'u_form':u_form,'p_form':p_form}

    return render(request,'all_users/profile.html',context)