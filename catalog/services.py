from catalog.models import Category
from catalog.models import Product


class CategoryProductService:

    @staticmethod
    def get_products_by_category(category_id):
        """Получаем все продукты по категориям"""
        products_by_category = Product.objects.filter(category_id=category_id)
        return products_by_category

    @staticmethod
    def get_category_name(category_id):
        """Получаем все категория по ключу категории"""
        category_name = Category.objects.get(id=category_id)
        return category_name
