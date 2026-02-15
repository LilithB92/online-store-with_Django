from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Delete  datas from db"

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
