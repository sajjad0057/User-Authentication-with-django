from django.shortcuts import render
from .forms import userForm,userInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .models import userInfo




# Create your views here.

def index(request):
    dict={}
    if request.user.is_authenticated:
        current_user = request.user

        user_basic_info = User.objects.get(pk=current_user.pk)
        user_more_info = userInfo.objects.get(user__pk=current_user.pk)

        dict = {'user_basic_info':user_basic_info,'user_more_info':user_more_info}
    return render(request,'index.html',context=dict)

def register(request):
    registered=False
    if request.method == 'POST':
        user_form = userForm(data=request.POST)
        user_info_form = userInfoForm(data=request.POST)
        if user_form.is_valid() and user_info_form.is_valid():
            x = user_form.save()
            x.set_password(x.password)
            x.save()
            y=user_info_form.save(commit=False)
            y.user = x
            if 'profile_pic' in request.FILES:
                y.profile_pic = request.FILES['profile_pic']
            y.save()
            registered=True



    else:
        user_form = userForm()
        user_info_form = userInfoForm()

    dict={'title':'register' , 'user_form':user_form , 'user_info_form' : user_info_form,'registered':registered}
    return render(request,'register.html',context=dict)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('Login_app:index'))
            else:
                return HttpResponse("Your account is not active !")
        else:
            return HttpResponse('Login Details Are Worng!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_app:index'))
