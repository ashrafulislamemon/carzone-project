from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from .models import Contact
# Create your views here.

def inquiry(request):
  if request.method=="POST":
    car_id=request.POST['car_id']
    car_title=request.POST['car_title']
    user_id=request.POST['user_id']
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    customer_need=request.POST['customer_need']
    city=request.POST['city']
    state=request.POST['state']
    
    email=request.POST['email']
    phone=request.POST['phone']
    message=request.POST['message']

    if request.user.is_authenticated:
      user_id=request.user.id
      has_connected=Contact.objects.all().filter(user_id=user_id,car_id=car_id)
      if has_connected:
        messages.error(request,'You already send a request for this car')

        return redirect('/cars/'+car_id)
    contact=Contact(car_id=car_id,car_title=car_title,user_id=user_id,first_name=first_name,last_name=last_name,customer_need=customer_need,city=city,state=state,email=email,phone=phone,message=message)


    send_mail(
        'New Inventory',
        'You Have new enventory please check the admin panel',
        'ashrafemon111@gmail.com',
        ['to@example.com'],
        fail_silently=False,
        )
    contact.save()

    messages.success(request,'you send a message ')

    return redirect("/cars/"+car_id)
  