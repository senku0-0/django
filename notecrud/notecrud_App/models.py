from django.db import models
# Create your models here.

class Contact_Us_Feedback(models.Model):
    info_type=models.CharField(max_length=20,blank=False)
    Fullname_ursername=models.CharField( max_length=50,blank=False)
    Email=models.EmailField(blank=False)
    Issue_quriy=models.TextField(blank=False)

class Contact_Us_Issues(models.Model):
    info_type=models.CharField(max_length=20,blank=False)
    Fullname_ursername=models.CharField( max_length=50,blank=False)
    Email=models.EmailField(blank=False)
    Issue_quriy=models.TextField(blank=False)

class Contact_Us_Quiry(models.Model):
    info_type=models.CharField(max_length=20,blank=False)
    Fullname_ursername=models.CharField( max_length=50,blank=False)
    Email=models.EmailField(blank=False)
    Issue_quriy=models.TextField(blank=False)
