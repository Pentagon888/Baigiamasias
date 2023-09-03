from django.core.management.base import BaseCommand
from .models import RepairCategory, AutoService


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Создание объектов категорий
        diagnostika_category = RepairCategory.objects.create(name='diagnostika')
        brake_repair_category = RepairCategory.objects.create(name='Brake Repair')
        oil_change_category = RepairCategory.objects.create(name='Oil Change')
        kebulo_darbai_category = RepairCategory.objects.create(name='Kebulo darbai')

        # Создание объектов автосервисов и их связь с категориями
        service1 = AutoService.objects.create(name='Geriausias Diagnostikos Servisas', location_lat=54.75271573295219, location_lon=25.24918544483979, phone_number='+37000000', address='P. Žadeikos g. 1B, Vilnius')
        service1.category.add(diagnostika_category)

        service2 = AutoService.objects.create(name='ABS', location_lat=54.72916349319593, location_lon=25.243707874329832, phone_number='+37011111', address='Test address 2')
        service2.category.add(brake_repair_category, oil_change_category)

        service3 = AutoService.objects.create(name='KEbuliniai', location_lat=54.7430686557557,  location_lon=25.226604212464995, phone_number='+37022222', address='Test address 3')
        service3.category.add(kebulo_darbai_category)