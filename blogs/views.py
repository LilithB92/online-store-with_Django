from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blogs.models import Blog


class BlogsListView(ListView):
    model = Blog
    template_name = 'blogs/base.html'

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog

class BlogUpdateView(UpdateView):
    model = Blog

class BlogDeleteView(DeleteView):
    model = Blog
