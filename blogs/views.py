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


class BlogUpdateView(UpdateView):
    model = Blog


class BlogDeleteView(DeleteView):
    model = Blog
