from django_filters.rest_framework import FilterSet
from .models import Doctor, Organization, Category, Appointment

class DoctorFilter(FilterSet):
    class Meta:
        model = Doctor
        fields = {
            'category_id': ['exact'],
        }

class AppointmentFilter(FilterSet):
    class Meta:
        model = Appointment
        fields = {
            'doctor_id': ['exact'],
            'user_id': ['exact'],
            'status': ['exact'],
            'status': ['exact'],
            'date_time': ['lte', 'gte', 'exact'],
        }