from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db import OperationalError, IntegrityError, DataError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from catalog.models import Product, Contact


# Create your views here.
def home(request):
    products = Product.objects.order_by("created_at")
    paginator = Paginator(products, 2)  # 10 элементов на страницу
    page_number = request.GET.get("page")  # Получение номера страницы из URL
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}
    return render(request, "home.html", context)


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
