from distutils.command.upload import upload
from statistics import mode
from venv import create
from django.db import models

# Create your models here.
class Team(models.Model):
  first_name=models.CharField(max_length=100)
  last_name=models.CharField(max_length=100)
  designation=models.CharField(max_length=100)
  photo=models.ImageField(upload_to='photos')
  facebook_link=models.URLField(max_length=100)
  twitter_link=models.URLField(max_length=100)
  google_plus_link=models.URLField(max_length=100)
  create_date=models.DateField(auto_now_add=True)


  def __str__(self):

    return self.first_name 