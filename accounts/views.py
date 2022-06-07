from email import message
import imp
from click import confirm
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
  if request.method=='POST':
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)

    if user is not None:
      auth.login(request,user)
      messages.success(request,'You are succesfully loged in')
      return redirect('dashboard')
    else:
      messages.success(request,'invalid login credential')
      return redirect('login')




  return render(request,'accounts/login.html')


def logout(request):
  auth.logout(request)
  return redirect('homepage') 


def register(request):
  if request.method=="POST":

    username=request.POST['username']
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    email=request.POST['email']
    
    password=request.POST['password']
    confirm_password=request.POST['confirm_password']

    if password==confirm_password:
      if User.objects.filter(username=username).exists():
        messages.error(request,'Username already exits')
        return redirect('register')

      else:

        if User.objects.filter(email=email).exists():
          messages.error(request,'email already exits')
          return redirect('register')

        else:
          user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
          auth.login(request,user)
          messages.success(request,'you are registerd successfully')
          
          user.save()
          return redirect('dashboard')
    else:
      messages.error(request,'password already exits')
      return redirect('register')

  return render(request,'accounts/register.html')  

@login_required(login_url='login')
def dashboard(request):

  user_inquery=Contact.objects.order_by("-create_date").filter(user_id=request.user.id)

  data={
    'inquery':user_inquery
  }
  return render(request,'accounts/dashboard.html',data)    