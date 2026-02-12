from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите название категории")
    description = models.TextField(verbose_name="Описание", null=True, blank=True, help_text="Введите описание категории")


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите название продукта")
    description = models.TextField(verbose_name="Описание",null=True, blank=True, help_text="Введите описание продукта")
    img = models.ImageField(upload_to="images/products", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="продукты", verbose_name="Категория", help_text="Введите категория продукта")
    price = models.FloatField(verbose_name="цена", help_text="Введите цена продукта")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]



