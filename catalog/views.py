from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.cache import cache
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
from catalog.services import CategoryProductService


class ProductList(ListView):
    model = Product
    context_object_name = "products"  # Optional: renames 'object_list' to 'products'
    paginate_by = 2  # Number of items per page

    def get_queryset(self):
        queryset = cache.get("dogs_list")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("dogs_list", queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset


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


class CategoryProductList(ListView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/category_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs["pk"]
        context["category_name"] = CategoryProductService.get_category_name(category_id)
        context["product_by_categories"] = CategoryProductService.get_products_by_category(category_id)
        return context


class ContactCreateView(CreateView):
    model = Contact
    fields = ["name", "phone", "message"]
    template_name = "contacts.html"
    success_url = reverse_lazy("catalog:products_list")
