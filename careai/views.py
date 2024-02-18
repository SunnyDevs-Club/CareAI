from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Doctor, Organization, Category, Appointment
from .pagination import DefaultPagination
from .filters import DoctorFilter, AppointmentFilter
from .serializers import (DoctorSerializer, OrganizationSerializer, AppointmentSerializer,
                        CategorySerializer, SymptomSerializer)


from ai.disease import symptom_analysis 
from ai.mri import predict_image

class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.select_related('organization', 'category').order_by('-id')
    serializer_class = DoctorSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = DoctorFilter
    search_fields = ['full_name']


class OrganizationViewSet(ModelViewSet):
    queryset = Organization.objects.order_by('-id')
    serializer_class = OrganizationSerializer
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]


class AppointmentViewSet(ModelViewSet):
    queryset = Appointment.objects.select_related('doctor', 'user').order_by('-id')
    serializer_class = AppointmentSerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = AppointmentFilter
    search_fields = ['doctor__full_name',]


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.order_by('-id')
    serializer_class = CategorySerializer
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name',]


'''
{
"symptoms": "temperature is high"
}
'''
@api_view(['POST'])
def analyze_symptoms(request):
    if request.method == 'POST':
        serializer = SymptomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        symptoms = data.get('symptoms', None)
        disease, specialization = symptom_analysis(symptoms)
        print(disease, specialization)
       
        doctors = Doctor.objects.select_related('category').filter(category__name__icontains=specialization.lower()).all()
        doctor_serializer = DoctorSerializer(doctors, many=True)

        return Response({'disease_category': specialization, 'disease':disease, 'recommended_doctors': doctor_serializer.data})
    
@api_view(['POST'])
def analyze_mri_image(request):
    if request.method == 'POST':
        try:
            # Read the image file from the request
            file = request.FILES['image']
            predicted_class, message = predict_image(file)
        except Exception as e:   
            return Response({"error": str(e)})
        
        doctor_list = []
        if predicted_class != 0:
            doctors = Doctor.objects.select_related('category').filter(category__name='Neurologist').all()
            doctor_serializer = DoctorSerializer(doctors, many=True)
            doctor_list = doctor_serializer.data

        # Return the predicted class name as JSON response
        return Response({'patient_condition': message, 'recommended_doctors': doctor_list})