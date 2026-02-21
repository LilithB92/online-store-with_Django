from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogsListView(ListView):
    model = Blog

    def get_queryset(self):
        # Получаем только активные объекты
        return Blog.objects.filter(is_active=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.viewcount += 1
        obj.save()
        return obj


#
class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "content", "img"]
    success_url = reverse_lazy("blogs:blogs_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["title", "content", "img", "is_active"]

    def get_success_url(self):
        return reverse_lazy("blogs:blog_detail", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blogs:blogs_list")
