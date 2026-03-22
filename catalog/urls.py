from django.http import JsonResponse
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import CategoryProductList
from catalog.views import ContactCreateView
from catalog.views import ProductCreateView
from catalog.views import ProductDeleteView
from catalog.views import ProductDetailView
from catalog.views import ProductList
from catalog.views import ProductUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path("products/", ProductList.as_view(), name="products_list"),
    path("contacts/new/", ContactCreateView.as_view(), name="contact_create"),
    path("product/<int:pk>/", cache_page(60 * 15)(ProductDetailView.as_view()), name="product_details"),
    path("product/new/", ProductCreateView.as_view(), name="product_create"),
    path("product/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("product/delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("products/category/<int:pk>/", CategoryProductList.as_view(), name="category_product"),
    path(".well-known/appspecific/com.chrome.devtools.json", lambda r: JsonResponse({})),
]
