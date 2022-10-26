
from django.shortcuts import render,HttpResponseRedirect
from .forms import Student
from .models import ChatGroup,User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login as lk,logout
# Create your views here.
def signup(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.set_level(request,5)
            messages.info(request,"your response is submitted")
            fm=UserCreationForm()
    else:
        fm=UserCreationForm()
    return render(request,"home.html",{"res":fm})

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/home/profile")
    if request.method=="POST":
        fm=AuthenticationForm(request,data=request.POST)
        if fm.is_valid():
            usernm=fm.cleaned_data["username"]
            paaswrd=fm.cleaned_data["password"]
            print("username is ",usernm)
            print("passwrd is ",paaswrd)
            user=authenticate(username=usernm,password=paaswrd)
            print("user is ",user)
            if user is not None:
                lk(request,user)
                messages.set_level(request,5)
                messages.info(request,"welcome to profile page")
                return HttpResponseRedirect("/home/profile/")
    else:
        fm=AuthenticationForm()
    return render(request,"login.html",{"res":fm})

def profile(request):
    if request.user.is_authenticated:
        #uer=User.objects.get(pk=request.user.id)
        user_group_ids=ChatGroup.user.through.objects.filter(user_id=request.user.id).values_list("chatgroup_id",flat=True)
        print("group is ",user_group_ids)
        user_group_names=ChatGroup.objects.filter(id__in=user_group_ids)
        print("group is ",user_group_names)
        return render(request,"profile.html",{"groups":user_group_names})
    else:
        messages.info(request,"phle login kr bhai")
        return HttpResponseRedirect("/home/login/")

def log__out(request):
    logout(request)
    return HttpResponseRedirect("/home/login/")

def join_group(request,group_name):
    return render(request,"group.html",{"group_name":group_name,"user_id":request.user.id})
