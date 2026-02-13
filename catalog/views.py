from django.core.exceptions import ValidationError
from django.db import OperationalError, IntegrityError, DataError
from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product, Contact


# Create your views here.
def home(request):
    most_recent_five_products = Product.objects.order_by("-created_at")[:5]
    return render(request, "home.html", {"products": most_recent_five_products})


def contacts(request):
    if request.method == "POST":
        try:
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            Contact(name=name, phone=phone, message=message).save()
            return HttpResponse(f"{name} сообщение успешно отправлено!!!")
        except (ValidationError, OperationalError, IntegrityError, DataError, ValueError):
            return render(request, "contacts.html")
    return render(request, "contacts.html")
