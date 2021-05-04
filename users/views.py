from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def create_user(req):
    if req.method=='POST':
        form =RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(req, f'{username}  logged in')
            return redirect('user_login')
    else:
        form=RegistrationForm()
    return render(req,'users/user_regis_form.html',{'form':form,})
@login_required
def profilepage(req):
    return render(req, 'users/profile.html',{})

