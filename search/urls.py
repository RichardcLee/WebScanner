from django.urls import re_path
from search import views

urlpatterns = [
    re_path(r'^$', views.search, name='search'),
]
