from django.contrib import admin
from .models import Doctor, Organization, Appointment


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Organization, OrganizationAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name',)

admin.site.register(Doctor, DoctorAdmin)


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('doctor',)

admin.site.register(Appointment, AppointmentAdmin)





