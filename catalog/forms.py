from django import forms
from django.core.exceptions import ValidationError
from django.db.models.fields import BooleanField

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "created_at",
            "updated_at",
            'status',
            'owner'
        ]

    forbidden_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.help_text

    def clean(self):
        # Список запрещенных слов
        clean_data = super().clean()
        name = clean_data.get("name")
        description = clean_data.get("description")
        for forbidden_word in self.forbidden_words:
            if forbidden_word == name.lower():
                self.add_error("name", f"Имя не может содержать слово {forbidden_word}")
            elif forbidden_word in description.lower():
                self.add_error("description", f"Описание не может содержать слово {forbidden_word}")
        return clean_data

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной")
        return price

    def clean_img(self):
        img = self.cleaned_data.get("img")
        max_size_mb = 5
        extensions = (".png", ".jpg")
        if img and (img.size > (max_size_mb * 1024 * 1024)):
            raise ValidationError(f"Максимальный размер файла - {max_size_mb} МБ.")
        if img and (not img.name.endswith(extensions)):
            raise ValidationError("Неподдерживаемые форматы изображений. Допускаются только JPEG и PNG.")
        return img
