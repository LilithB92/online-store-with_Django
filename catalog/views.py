from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


# Create your views here.
def home(request):
    most_recent_five_products = Product.objects.order_by("-created_at")[:5]
    return render(request, "home.html", {"products": most_recent_five_products})


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"{name} сообщение успешно отправлено!!!")
    return render(request, "contacts.html")
