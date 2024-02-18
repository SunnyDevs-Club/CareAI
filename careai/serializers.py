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
    doctor_id = serializers.IntegerField()
    doctor = serializers.CharField(read_only=True)
    patient_fullname = serializers.SerializerMethodField()
    doctor_category = serializers.SerializerMethodField()
    doctor_price = serializers.SerializerMethodField()
    class Meta():
        model = Appointment
        fields ='__all__'

    def get_patient_fullname(self, obj):
        return obj.user.get_full_name()
    
    def get_doctor_category(self, obj):
        return obj.doctor.category.name
    
    def get_doctor_price(self, obj):
        return str(obj.doctor.price)


class SymptomSerializer(serializers.Serializer):
    symptoms = serializers.CharField()