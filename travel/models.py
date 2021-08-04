from django.db import models
from django.core.exceptions import ValidationError
from account.models import Account
from django.shortcuts import redirect,reverse

class Trip(models.Model):
    train_no=models.CharField(max_length=20,blank=True)
    flight_no=models.CharField(max_length=20,blank=True)
    doj=models.DateField()
    dst=models.CharField(max_length=100)
    ast=models.CharField(max_length=100)
    passenger=models.ForeignKey(Account,on_delete=models.CASCADE)

    def __str__(self):
        return self.dst+" To "+self.ast

    def clean(self):
        if self.train_no and self.flight_no:
            raise ValidationError({'train_no':("You can have a trip either by a flight or a train. Only one field can be set.")})
        elif (not(self.train_no)) and ((self.flight_no)==''):
            raise ValidationError({'train_no':("You should have a trip either by a flight or a train. Enter the details in any one field.")})

    def get_absolute_url(self):
        return reverse('trips')

class Cab(models.Model):
    From=models.CharField(max_length=100)
    To=models.CharField(max_length=100)
    doj=models.DateField()
    time=models.CharField(max_length=20)
    vseats=models.PositiveIntegerField()
    qraiser=models.ForeignKey(Account,on_delete=models.CASCADE)
    passengers=models.ManyToManyField(Account,blank=True,related_name='passenger_account_set')

    def __str__(self):
        return self.From+" To "+self.To

    def get_absolute_url(self):
        return reverse('cabs')
