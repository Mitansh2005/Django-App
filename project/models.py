from django.db import models

# Create your models here.
class UserForm(models.Model):
    name=models.CharField(max_length=100)
    surname=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    email=models.EmailField()
    phone_number=models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.name} {self.surname}"
    
    