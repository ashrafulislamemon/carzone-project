from django.shortcuts import redirect, render

# Create your views here.
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
def home(request):

    team=Team.objects.all()

    car=Car.objects.order_by('-created_date').filter(is_featured=True)
    all_car =Car.objects.order_by('-created_date')

    # search_fields=Car.objects.values('model','body_style','city','year',)

    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style' ,flat=True).distinct()


    context={
        'teams':team,
        'car':car,
        'all_car':all_car,
        # 'search_fields':search_fields

        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search,


    }
    return render(request,'home.html',context)


def about(request):
    team=Team.objects.all()


    context={
        'teams':team
    }
    return render(request,'pages/about.html',context)

def services(request):
    return render(request,'pages/services.html')

def contact(request):

    if request.method=='POST':
        
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        phone=request.POST['phone']
        message=request.POST['message']

        email_sub='you have a message from carzone'+subject
        massage_body='Name:' + name + "email:" +email+ "phone:" +phone+ "message:"+message 
        # admin_info=User.objects.get(is_superuser=True)
        # admin_email=admin_info.email
        
        send_mail(
            email_sub,
            massage_body,
            'ashrafemon111@gmail.com',
            ['to@example.com'],
            fail_silently=False,


            )

        return redirect('contactpage')    
        




    return render(request,'pages/contact.html')

