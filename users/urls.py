from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import path

from .apps import UsersConfig
from .views import RegisterView

app_name = UsersConfig.name


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="catalog:products_list"), name="logout"),
]
