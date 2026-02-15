from django.core.exceptions import ValidationError
from django.db import OperationalError, IntegrityError, DataError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Contact


# Create your views here.
def home(request):
    products = Product.objects.order_by("created_at")
    context = {"products": products}
    return render(request, "home.html", context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_details.html", context)


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
