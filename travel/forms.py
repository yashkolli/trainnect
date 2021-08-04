from django import forms
from .models import Trip,Cab

class DateInput(forms.DateInput):
    input_type='date'

class AddTripForm(forms.ModelForm):

    class Meta:
        model=Trip
        fields=['train_no','flight_no','doj','dst','ast']
        widgets={
            'doj': DateInput(),
        }

class AddCabForm(forms.ModelForm):

    class Meta:
        model=Cab
        fields=['From','To','doj','time','vseats']
        widgets={
            'doj':DateInput(),
        }




