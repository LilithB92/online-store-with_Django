from django.contrib import admin
from blogs.models import Blog

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "img", "is_active")
    search_fields = ("title", "content")
