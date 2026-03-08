from django.db import models

from users.models import CustomUser


class Category(models.Model):
    """
    Класс для категории продуктовЬ
    """

    objects = models.Manager()
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите название категории")
    description = models.TextField(
        verbose_name="Описание", null=True, blank=True, help_text="Введите описание категории"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    """Класс продуктов"""

    objects = models.Manager()
    name = models.CharField(max_length=150, verbose_name="Наименование", help_text="Введите название продукта")
    description = models.TextField(
        verbose_name="Описание", null=True, blank=True, help_text="Введите описание продукта"
    )
    img = models.ImageField(upload_to="images/products", null=True, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="продукты",
        verbose_name="Категория",
        help_text="Введите категория продукта",
    )
    price = models.FloatField(verbose_name="цена", help_text="Введите цена продукта")
    STATUS_CHOICES = [
        ("P", "Pending"),
        ("A", "Approved"),
        ("C", "Cancelled"),
        ("R", "Rejected"),
    ]
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="продукты",
        verbose_name="Владелец",
        help_text="Введите владельца продукта",
    )

    status = models.CharField(
        max_length=1,  # Often a single character is enough
        choices=STATUS_CHOICES,
        default="P",  # Set a default status
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "category", "price"]
        permissions = [("can_unpublish_product", "Can unpublish product")]


class Contact(models.Model):
    """Класс для контакта пользователям"""

    name = models.CharField(max_length=150, verbose_name="Наименование")
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"Контакты от {self.name}"

    class Meta:
        verbose_name = "Данные контакта"
        verbose_name_plural = "Контактные данные"
