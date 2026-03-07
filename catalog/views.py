from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from catalog.forms import ProductForm
from catalog.models import Product, Contact


class ProductList(ListView):
    model = Product
    context_object_name = "products"  # Optional: renames 'object_list' to 'articles'
    paginate_by = 2  # Number of items per page


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def test_func(self):
        product = self.get_object()
        return product.owner == self.request.user



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")


class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "contacts.html"
    success_url = reverse_lazy("catalog:products_list")
