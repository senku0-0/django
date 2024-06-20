from django.db import models

# Create your models here.
class Login_Register_db(models.Model):
    First_name=models.CharField(max_length=50)
    Middle_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Date_Of_Brith=models.DateField()
    Roll_No=models.IntegerField()
    Phone_No=models.BigIntegerField()
    PEmail_ID=models.EmailField()
    CEmail_ID=models.EmailField()
    Password=models.CharField(max_length=50)
    Confrimed_Password=models.CharField(max_length=50)
