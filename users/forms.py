from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db.models import BooleanField

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "avatar",
            "country",
            "password1",
            "password2",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.help_text

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError("Номер телефона должен содержать только цифры.")
        return phone_number
