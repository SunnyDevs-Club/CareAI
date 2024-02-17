from rest_framework import serializers
from .models import Organization, Doctor, Appointment, Category


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Organization
        fields ='__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields ='__all__'


class DoctorSerializer(serializers.ModelSerializer):
    organization = serializers.CharField()
    category = serializers.CharField()
    geo_location = serializers.SerializerMethodField()

    class Meta():
        model = Doctor
        fields = ['id', 'organization', 'category', 'geo_location', 'full_name', 'rating', 'description', 'price', 'phone_number', 'photo', 'updated_at', 'created_at']

    def get_geo_location(self, obj):
        res = {'longitude': obj.longitude, 'latitude': obj.latitude}
        return res 

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.CharField()
    patient_fullname = serializers.SerializerMethodField()

    class Meta():
        model = Appointment
        fields ='__all__'

    def get_patient_fullname(self, obj):
        return obj.user.get_full_name()
