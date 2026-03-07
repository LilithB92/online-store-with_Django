from django.contrib import admin

from catalog.models import Category
from catalog.models import Contact
from catalog.models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    list_filter = ("category", "status")
    search_fields = ("name", "description")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name", "description")


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False

    list_display = ("id", "name", "phone", "message")
    search_fields = ("name", "message")
