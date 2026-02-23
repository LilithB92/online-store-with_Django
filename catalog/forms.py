from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "created_at",
            "updated_at",
        ]

    def clean(self):
        # Список запрещенных слов
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
        clean_data = super().clean()
        name = clean_data.get("name")
        description = clean_data.get("description")
        for forbidden_word in forbidden_words:
            if forbidden_word == name.lower():
                self.add_error("name", f"Имя не может содержать слово {forbidden_word}")
            elif forbidden_word in description.lower():
                self.add_error("description", f"Описание не может содержать слово {forbidden_word}")
        return clean_data
