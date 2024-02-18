from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register(r'doctors', views.DoctorViewSet, basename='doctors')
router.register(r'organizations', views.OrganizationViewSet, basename='organizations')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'appointments', views.AppointmentViewSet, basename='appointments')


urlpatterns = [
    path('',include(router.urls)),
    path('symptom-analysis/', views.analyze_symptoms),
]