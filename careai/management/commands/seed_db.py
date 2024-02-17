from django.core.management.base import BaseCommand
from django.db import models
from careai.models import Doctor, Category, Organization


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Предполагаем, что категории и организации уже созданы и имеют id 1, 2, 3, 4, 5, 6 для категорий и какой-то id для организации

        org1 = Organization.objects.create(name='CareAi')

        category1 = Category.objects.create(name='Neurologist')
        category2 = Category.objects.create(name='Cardiologist')
        category3 = Category.objects.create(name='Dentist')
        category4 = Category.objects.create(name='Therapist')
        category5 = Category.objects.create(name='Surgeon')
        category6 = Category.objects.create(name='Neuropathologist')

        # Категории
        categories = {
            "Neurologist": category1.id,
            "Cardiologist": category2.id,
            "Dentist": category3.id,
            "Therapist": category4.id,
            "Surgeon": category5.id,
            "Neuropathologist": category6.id
        }

        # Предполагаем, что существует организация с id 1
        organization_id = org1.id

        for category_name, category_id in categories.items():
            for i in range(2):  # Создаем 2 доктора для примера
                Doctor.objects.create(
                    full_name=f"{category_name} Doctor {i+1}",
                    category=Category.objects.get(id=category_id),
                    organization=Organization.objects.get(id=organization_id),
                    rating=4.5 + i * 0.1,  # Пример рейтинга
                    description=f"Description {category_name} Doctor {i+1}",
                    price=1000.00 + i * 500,  # Пример цены
                    phone_number=f"+123456789{i}",
                    photo="/doctor_photos/doc.jpeg",  # Укажите путь к фотографии
                    latitude=55.7558 + i * 0.01,  # Пример широты
                    longitude=37.6173 + i * 0.01,  # Пример долготы
                )
