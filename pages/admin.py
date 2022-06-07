from django.contrib import admin

# Register your models here.
from .models import Team

from django.utils.html import format_html
class teamAdmin(admin.ModelAdmin):

  def thumbnail(self,object):
    return format_html('<img src="{}" width="40" style="border-radius:50px;" />'.format(object.photo.url))
  thumbnail.short_description='photo'


  list_display = ('id','thumbnail','first_name','designation','create_date')
  list_display_links =  ('id','first_name')
  list_filter = ('designation',)
  search_fields =('designation','first_name','last_name')


admin.site.register(Team,teamAdmin)