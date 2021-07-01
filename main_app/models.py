from django.db import models

# Create your models here.

class Register(models.Model):
    User_Name = models.CharField(max_length=255)
    E_mail = models.CharField(max_length=255)
    Confirm_mail = models.CharField(max_length=255)

    def __str__(self):
        return self.E_mail