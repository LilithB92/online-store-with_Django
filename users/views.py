from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import CustomUserCreationForm


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  # Redirect to the 'login' URL name
    template_name = "users/register.html"
