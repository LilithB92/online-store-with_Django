from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "created_at",
            "updated_at",
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
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной')
        return price
