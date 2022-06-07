from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAsdmin(admin.ModelAdmin):
  list_display=('id','first_name','last_name','car_id','car_title','email','city','create_date','phone')
  list_display_links=('id','first_name','last_name')
  search_fields=('first_name','last_name','email','car_title')
  list_per_page=25
admin.site.register(Contact,ContactAsdmin)  