from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductDetailView, ProductList

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductList.as_view(), name="products_list"),
    path("contacts/", contacts, name="contacts"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_details"),
]
