from django.db import models

class Patient(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.PhoneNumberField()
    diseas = models.CharField(max_length=100)
    payment = models.DecimalField(max_digits=10)


    def __str__(self):
        return self.fname