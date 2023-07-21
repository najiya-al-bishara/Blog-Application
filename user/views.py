from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from blog_app.forms import UserAddForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog_app.models import Bloglist

# Create your views here.

def signup(request):
    form=UserAddForm()
    if request.method=='POST':
        form=UserAddForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            if User.objects.filter(username=username).exists():
                messages.info(request,'this user name is alredy taken')
                return redirect('signup')
            
            if User.objects.filter(email=email).exists():
                messages.info(request,'this email is alredy taken')
                return redirect('signup')
            else:
                new_user=form.save()
                new_user.save()
                messages.info(request,'new user created')
                return redirect('signin')
    return render(request,'signup.html',{'form':form})
def signin(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['password']
        user= authenticate(request,username=username,password=password)
        if user is not None:
            request.session['username']=username
            request.session['password']=password
            login(request,user)
            return redirect('first')
        else:
            messages.info(request,'username or password is incorrect')
            return redirect('signin')

    return render(request,'signin.html')
