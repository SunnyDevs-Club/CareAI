from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import filters

from .models import Doctor, Organization, Category, Appointment
from .serializers import DoctorSerializer, OrganizationSerializer, AppointmentSerializer, CategorySerializer
from .pagination import DefaultPagination
from .filters import DoctorFilter, AppointmentFilter


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
