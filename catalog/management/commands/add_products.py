from django.core.management.base import BaseCommand

from catalog.models import Category
from catalog.models import Product


class Command(BaseCommand):
    help = "Add test category and products to the database"

    def handle(self, *args, **kwargs):
        category, _ = Category.objects.get_or_create(name="electronic")

        products = [
            {"name": "phone", "description": "not bad phone", "price": 57000, "category": category},
            {"name": "headphone", "description": "good headphone", "price": 23000, "category": category},
            {"name": "computer", "price": 210000, "category": category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Successfully added student: {product.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Student already exists: {product.name}"))
