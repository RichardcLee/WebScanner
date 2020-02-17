from django.urls import re_path
from task import views
app_name = 'task'
urlpatterns = [
    re_path(r'^(\d+)$', views.task_index, name='task_index'),
    re_path(r'^task_create$', views.task_create, name="task_create"),
    re_path(r'^task_detail/(\d+)$', views.task_detail, name='task_detail'),
]
