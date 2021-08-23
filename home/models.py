from django.db import models
from PIL import Image

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=60)
    middle_name= models.CharField(max_length=60, blank=True)
    last_name= models.CharField(max_length=60)
    mobile_num= models.CharField(max_length=12)
    student_photo= models.ImageField(upload_to="images/" , blank=True)
    student_aadhar_photo= models.ImageField(upload_to= 'images/', blank=True)
    email= models.EmailField(max_length=200)
    create_at= models.DateTimeField(auto_now_add=True)
    last_modified_at= models.DateTimeField(auto_now=True)
    ipAddress= models.GenericIPAddressField(blank=True, null=True)
