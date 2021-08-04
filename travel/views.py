from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Trip,Cab
from .forms import AddTripForm,AddCabForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.db.models import F
from django.contrib import messages
import datetime

def home(request):
    return render(request,'travel/home.html')

class TripListView(LoginRequiredMixin,ListView):
    model=Trip
    paginate_by=5

    def delete_instance(self,instance):
        now=datetime.datetime.now().date()

        if instance.doj < (now-datetime.timedelta(days=5)):
            instance.delete()

    def get_queryset(self):
        user=self.request.user
        for trip in Trip.objects.filter(passenger=user).order_by('doj'):
            self.delete_instance(trip)
        return Trip.objects.filter(passenger=user).order_by('doj')

class TripPartnerListView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    model=Trip
    paginate_by=5
    template_name='travel/tp_list.html'

    def get_queryset(self):
        trip=get_object_or_404(Trip,id=self.kwargs.get('pk'))
        if (trip.train_no==''):
            return Trip.objects.exclude(passenger=trip.passenger).filter(flight_no=trip.flight_no,doj=trip.doj).order_by('passenger')
        return Trip.objects.exclude(passenger=trip.passenger).filter(train_no=trip.train_no,doj=trip.doj).order_by('passenger')

    def test_func(self):
        trip=get_object_or_404(Trip,id=self.kwargs.get('pk'))
        if self.request.user==trip.passenger:
            return True
        return False

class TripCreateView(LoginRequiredMixin,CreateView):
    model=Trip
    form_class=AddTripForm

    def form_valid(self,form):
        form.instance.passenger=self.request.user
        return super().form_valid(form)

class TripUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Trip
    form_class=AddTripForm

    def form_valid(self,form):
        form.instance.passenger=self.request.user
        return super().form_valid(form)

    def test_func(self):
        trip=get_object_or_404(Trip,id=self.kwargs.get('pk'))
        if self.request.user==trip.passenger:
            return True
        return False

class TripDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Trip

    def get_success_url(self,**kwargs):
        return self.object.get_absolute_url()

    def test_func(self):
        trip=get_object_or_404(Trip,id=self.kwargs.get('pk'))
        if self.request.user==trip.passenger:
            return True
        return False

class CabListView(LoginRequiredMixin,ListView):
    model=Cab
    paginate_by=5
    order_by=["doj"]

    def delete_instance(self,instance):
        now=datetime.datetime.now().date()

        if instance.doj < (now-datetime.timedelta(days=5)):
            instance.delete()

    def get_context_data(self,**kwargs):
        for instance in Cab.objects.all():
            self.delete_instance(instance)
        context=super(CabListView,self).get_context_data(**kwargs)
        return context

class CabCreateView(LoginRequiredMixin,CreateView):
    model=Cab
    form_class=AddCabForm

    def form_valid(self,form):
        form.instance.qraiser=self.request.user
        return super().form_valid(form)

class CabUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Cab
    form_class=AddCabForm

    def form_valid(self,form):
        form.instance.qraiser=self.request.user
        return super().form_valid(form)

    def test_func(self):
        cab=get_object_or_404(Cab,id=self.kwargs.get('pk'))
        if self.request.user==cab.qraiser:
            return True
        return False

class CabDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Cab

    def get_success_url(self,**kwargs):
        return self.object.get_absolute_url()

    def test_func(self):
        cab=get_object_or_404(Cab,id=self.kwargs.get('pk'))
        if self.request.user==cab.qraiser:
            return True
        return False

class CabJoinView(LoginRequiredMixin,DetailView):
    model=Cab

    def get_context_data(self,**kwargs):
        context=super(CabJoinView,self).get_context_data(**kwargs)
        self.object.passengers.add(self.request.user)
        self.object.vseats=F('vseats')-1
        self.object.save()
        self.object.refresh_from_db()
        return context

class CabStatusView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model=Cab
    template_name='travel/cab_status.html'

    def test_func(self):
        cab=get_object_or_404(Cab,id=self.kwargs.get('pk'))
        if self.request.user==cab.qraiser:
            return True
        return False





