from ast import keyword
from pickle import TRUE
from pyexpat import model
from django.shortcuts import render,get_object_or_404

from .models import Car
from django.core.paginator import Paginator
# Create your views here.
def cars(request):
    car=Car.objects.order_by('-created_date')
    paginator = Paginator(car,2) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style',flat=True).distinct()
    context={
        'car':page_obj,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search,

    }
    
    return render(request,'cars/cars.html',context)
    
def car_details(request,id):
    single_car= get_object_or_404(Car,pk=id)

    context={
        'single_car':single_car
    }
    return render(request,'cars/car_details.html',context)


def search(request):
    car=Car.objects.order_by('-created_date')
    model_search=Car.objects.values_list('model',flat=True).distinct()
    year_search=Car.objects.values_list('year',flat=True).distinct()
    location_search=Car.objects.values_list('city',flat=True).distinct()
    body_style_search=Car.objects.values_list('body_style' ,flat=True).distinct()
    transmission_search=Car.objects.values_list('transmission' ,flat=True).distinct()


    if 'keyword' in request.GET:
        keyword=request.GET['keyword']

        if keyword:
            car=car.filter(description__icontains=keyword)


    if 'model' in request.GET:
        model=request.GET['model']
        if model:
            car=car.filter(model__iexact=model)

    if 'year' in request.GET:
        year=request.GET['year']
        if year:
            car=car.filter(year__iexact=year)


    if 'body_style' in request.GET:
        body_style=request.GET['body_style']
        if body_style:
            car=car.filter(body_style__iexact=body_style)

    if 'city' in request.GET:
        city=request.GET['city']
        if city:
            car=car.filter(city__iexact=city)

    if 'min_price' in request.GET:
        min_price=request.GET['min_price']
        max_price=request.GET['max_price']

        if min_price:
            car=car.filter(price__gte=min_price,price__lte=max_price)
    
    context={
        'car':car,
        'model_search':model_search,
        'year_search':year_search,
        'location_search':location_search,
        'body_style_search':body_style_search,
        'transmission_search':transmission_search
    }
    

    return render(request,'cars/serach.html',context)    