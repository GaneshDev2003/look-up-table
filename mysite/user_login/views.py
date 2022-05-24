from django.shortcuts import render,redirect
from .models import UserLogin
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from entries.models import EntriesModel
from entries.forms import EntryForm
from django.db.models import Q

# Create your views here.

def user_detail_view(request):
    user_obj = UserLogin.objects.get(id = 1);
    context = {
        'user' : user_obj
    }
    return render(request,'user_login/detail.html',context)

def user_register_view(request):
    if(request.method == "POST"):
        username = request.POST['username']
        password = request.POST['password']
        isEditor = False
        if(request.POST.get('isEditor',False)=="on"):
            isEditor = True
        if(User.objects.filter(username = username).exists()):
            raise forms.ValidationError("This username already exists")
        else:
            obj = UserLogin.objects.create(username = username,password = password, isEditor = isEditor)
            obj.save()
            user = User.objects.create_user(username=username,password=password)
            user.save()
            return redirect('home')
    return render(request,'signup.html',{})

def user_signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(request, user)
            obj = UserLogin.objects.get(username = username)
            print(obj.isEditor)
            return render(request,'search.html',{})
    return render(request,'signin.html',{})

def user_search_view(request):
    if request.method == "POST":
        searched = request.POST['searched']
        current_user = request.user
        lookups = EntriesModel.objects.filter(Q(name__icontains = searched) | Q(country__icontains = searched) | Q(company__icontains = searched) | Q(branch__icontains = searched) | Q(batch__icontains = searched))
        obj = UserLogin.objects.get(username=current_user.username)
        return render(request, 'search.html' ,{"entries":lookups,"searched":searched,"isEditor":obj.isEditor})
    return render(request, 'search.html' ,{})

def user_update_view(request,user_id):
    entry = EntriesModel.objects.get(pk=user_id)
    form = EntryForm(request.POST or None,instance=entry)
    if form.is_valid():
        form.save()
        return redirect('search-user')
    return render(request,'user_login/update.html',{"form":form,"user":entry})

def user_logout_view(request):
    if(request.method=='POST'):
        logout(request)
        return redirect('home')
    return render(request,'logout.html',{})