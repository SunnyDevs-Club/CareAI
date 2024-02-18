from django.core.management.base import BaseCommand
from django.db import models
from careai.models import Doctor, Category, Organization


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Предполагаем, что категории и организации уже созданы и имеют id 1, 2, 3, 4, 5, 6 для категорий и какой-то id для организации

        org1 = Organization.objects.create(name='CareAi')

        category1 = Category.objects.create(name='Dermatologist')
        category2 = Category.objects.create(name='Gastroenterologist')
        category3 = Category.objects.create(name='Allergist')
        category4 = Category.objects.create(name='Urologist')
        category5 = Category.objects.create(name='Infectious Disease Specialist')
        category6 = Category.objects.create(name='Orthopedist')
        category7 = Category.objects.create(name='Neurologist')
        category8 = Category.objects.create(name='Cardiologist')
        category9 = Category.objects.create(name='Pulmonologist')
        category10 = Category.objects.create(name='General Practitioner')

        # Предполагаем, что существует организация с id 1
        organization_id = org1.id

        for category in Category.objects.all():
            for i in range(2):  # Создаем 2 доктора для примера
                Doctor.objects.create(
                    full_name=f"{category.name} Doctor {i+1}",
                    category_id=category.id,
                    organization_id=organization_id,
                    rating=4.5 + i * 0.1,  # Пример рейтинга
                    description=f"Description {category.name} Doctor {i+1}",
                    price=1000.00 + i * 500,  # Пример цены
                    phone_number=f"+123456789{i}",
                    photo="/doctor_photos/doc.jpeg",  # Укажите путь к фотографии
                    latitude=55.7558 + i * 0.01,  # Пример широты
                    longitude=37.6173 + i * 0.01,  # Пример долготы
                )
