from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AccountUpdateForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def register(request):

    if request.method=='POST':

        form=UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            first_name=form.cleaned_data.get('first_name')
            messages.success(request,f'Account has been created for { first_name }! You are now able to login.')
            return redirect('login')
    else:
        form=UserRegistrationForm()

    return render(request,'account/register.html',{'form':form})

"""
def login(request):

    if request.method=='POST':

        form=AccountAuthenticationForm(request.POST)

        if form.is_valid():

            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)

            if user:
                auth_login(request,user)
                # return redirect('travel-home')
    else:
        form=AccountAuthenticationForm()

    return render(request,'account/login.html',{'form':form})

def logout(request):
    auth_logout(request)
    return render(request,'account/logout.html')
"""

@login_required
def account(request):

    if request.method=='POST':

        form = AccountUpdateForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('account')

    else:
        form = AccountUpdateForm(instance = request.user)

    return render(request,'account/account.html',{'form':form})
