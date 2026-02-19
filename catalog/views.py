from django.core.exceptions import ValidationError
from django.db import OperationalError, IntegrityError, DataError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from catalog.models import Product, Contact


class ProductList(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"  # Optional: renames 'object_list' to 'articles'
    paginate_by = 2  # Number of items per page


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"


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
