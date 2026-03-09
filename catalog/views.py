from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from catalog.forms import ProductForm
from catalog.forms import ProductModeratorForm
from catalog.models import Contact
from catalog.models import Product


class ProductList(ListView):
    model = Product
    context_object_name = "products"  # Optional: renames 'object_list' to 'articles'
    paginate_by = 2  # Number of items per page


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.add_product"

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        elif user.has_perm(
            "catalog.can_unpublish_product"
        ):  # elif user.groups.filter(name="Модератор продуктов").exists():
            return ProductModeratorForm
        else:
            return HttpResponseForbidden


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")
    permission_required = "catalog.delete_product"

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return obj.owner == self.request.user or user.groups.filter(name="Модератор продуктов").exists()


class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "contacts.html"
    success_url = reverse_lazy("catalog:products_list")
