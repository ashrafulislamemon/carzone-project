from datetime import datetime
from pyexpat import model
from random import choices
from django.db import models
from datetime import datetime
# Create your models here.
from ckeditor.fields import RichTextField


from multiselectfield import MultiSelectField

state_choice=(
	('Al','Alamba'),
	('Ak','Alaska'),
	('Az','Arkansas'),
	('Ca','Californiya'),
	('Co','Colordo')
)

year_choice=[]

for i in range (2000,(datetime.now().year+1)):
  year_choice.append((i,i))


door_choice=(
  ('1','1'),
  ('2','2'),
  ('3','3'),
  ('4','4'),
  ('5','5'),
  ('6','6'),
)

car_feature=(

  ('Cruise Control','Cruise Control'),
  ('Audio Interface','Audio Interface'),
  ('Airbags','Airbags'),
  ('Air Condition','Air Condition'),
  ('Alam System','Alam System'),
  ('Park Assist','Park Assist'),
  ('Power Steering','Power Steering'),
  ('Direct Fuel Injection','Direct Fuel Injection'),
  ('Auto start/stop','Auto start/stop'),
  ('Wind Defender','Wind Defender'),
  ('Bluetooth Handset','Bluetooth Handset'),
)

class Car(models.Model):
  car_title = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(choices=state_choice ,max_length=100)
  model = models.CharField(max_length=100)
  year = models.IntegerField(('year'),choices=year_choice)
  condition = models.CharField(max_length=100)
  price = models.IntegerField()
  description = RichTextField()

  car_photo = models.ImageField(upload_to='photos/cars')
  car_photo_1 = models.ImageField(upload_to='photos/cars',blank=True)
  car_photo_2 = models.ImageField(upload_to='photos/cars',blank=True)
  car_photo_3 = models.ImageField(upload_to='photos/cars',blank=True)
  car_photo_4 = models.ImageField(upload_to='photos/cars',blank=True)
  features = MultiSelectField(choices=car_feature)
  body_style = models.CharField(max_length=100)
  engine = models.CharField(max_length=100)
  transmission = models.CharField(max_length=100)
  interior = models.CharField(max_length=100)
  miles = models.IntegerField()
  doors = models.CharField(choices=door_choice,max_length=100)
  passengers = models.IntegerField()
  vin_no = models.CharField(max_length=100)
  milage = models.IntegerField()
  fuel_type = models.CharField(max_length=100) 
  no_of_owners = models.CharField(max_length=100)
  is_featured = models.BooleanField(default=False)
  created_date = models.DateTimeField(default=datetime.now(),blank=True)
  def __str__(self) :
      return self.car_title




