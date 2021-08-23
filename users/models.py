from django.db import models
from django.contrib.auth.models import User

class candidateinfo(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_num= models.CharField(max_length=12)
    student_photo= models.ImageField(default='default.jpg', upload_to="images/" , blank=True)
    student_aadhar_photo= models.ImageField(upload_to= 'images/', blank=True)
    email= models.EmailField(max_length=200)
    create_at= models.DateTimeField(auto_now_add=True)
    last_modified_at= models.DateTimeField(auto_now=True)
    ipAddress= models.GenericIPAddressField(blank=True, null=True)
