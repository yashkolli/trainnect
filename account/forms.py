from django import forms
from .models import Account
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model=Account
        fields=['email','first_name','year','rollno','branch']

"""
class AccountAuthenticationForm(forms.Form):

    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']
            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid Login")
"""

class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model=Account
        fields=['email','first_name', 'last_name','year','rollno','branch', 'mobileno']

    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
        except Account.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)

    def clean_rollno(self):
        rollno=self.cleaned_data['rollno']
        try:
            account = Account.objects.exclude(pk=self.instance.pk).get(rollno=rollno)
        except Account.DoesNotExist:
            return rollno
        raise forms.ValidationError('rollno "%s" is already in use.' % rollno)

