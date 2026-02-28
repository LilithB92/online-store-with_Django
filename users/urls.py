from django.urls import path
from .apps import UsersConfig


app_name = UsersConfig.name



urlpatterns = [
    # path('', BlogsListView.as_view(), name='blogs_list'),
    # path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    # path('new/', BlogCreateView.as_view(), name='blog_create'),

]