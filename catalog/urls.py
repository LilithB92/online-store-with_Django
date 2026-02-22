from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductDetailView, ProductList, ContactCreateView, ProductCreateView, ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductList.as_view(), name="products_list"),
    path("contacts/new/", ContactCreateView.as_view(), name="contact_create"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
]
