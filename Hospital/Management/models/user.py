from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PhoneNumberField()
    password = models.CharField(max_length=8)

    
    def RegisterUser(self):
        return self.save()
    
    @staticmethod
    def IfUserExists(self):
        if User.objects.filter(email=self.email).exists():
            raise ValueError('Email is already exists')
        else:
            pass
    
    @staticmethod
    def Get_user_by_email(email_args):
        try:
            User.objects.filter(email = email_args)
        except:
            raise ValueError('Email does not exists')
        
    def __str__(self):
        return self.fname