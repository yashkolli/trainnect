from django.contrib import admin
from .models import Trip,Cab

class TripAdmin(admin.ModelAdmin):
    model=Trip
    ordering=('doj',)
    list_display=('train_no','flight_no','doj','dst','ast','passenger')
    search_fields=('train_no','flight_no','doj','dst','ast','passenger',)
    readonly_fields=('passenger',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

class CabAdmin(admin.ModelAdmin):
    model=Cab
    ordering=('doj',)
    list_display=('From','To','doj','time','vseats','qraiser')
    search_fields=('From','To','doj','time','qraiser')
    readonly_fields=('qraiser',)

    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Trip,TripAdmin)
admin.site.register(Cab,CabAdmin)
