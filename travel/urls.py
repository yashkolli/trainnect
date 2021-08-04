from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="travel-home"),
    path('trips/',views.TripListView.as_view(),name="trips"),
    path('trips/new/',views.TripCreateView.as_view(),name="trip-create"),
    path('trips/<int:pk>/update/',views.TripUpdateView.as_view(),name="trip-update"),
    path('trips/<int:pk>/delete/',views.TripDeleteView.as_view(),name="trip-delete"),
    path('trips/<int:pk>/tp/',views.TripPartnerListView.as_view(),name="trip-partners"),
    path('cabs/',views.CabListView.as_view(),name="cabs"),
    path('cabs/new/',views.CabCreateView.as_view(),name="cabs-create"),
    path('cabs/<int:pk>/delete/',views.CabDeleteView.as_view(),name="cabs-delete"),
    path('cabs/<int:pk>/update/',views.CabUpdateView.as_view(),name="cabs-update"),
    path('cabs/<int:pk>/join/',views.CabJoinView.as_view(),name="cab-join"),
    path('cabs/<int:pk>/status/',views.CabStatusView.as_view(),name="cab-status"),
]
