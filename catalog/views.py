from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from catalog.models import Product, Contact


class ProductList(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"  # Optional: renames 'object_list' to 'articles'
    paginate_by = 2  # Number of items per page


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"


class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "contacts.html"
    success_url = reverse_lazy("catalog:products_list")
