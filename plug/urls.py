from django.urls import re_path, path
from plug import views
app_name = 'plug'
urlpatterns = [
    re_path(r'^add_plug$', views.add_plug, name='add_plug'),
    re_path(r'^list/(\S+)$', views.plug_list, name='plug_list'),
    path('upload_script/', views.upload_script, name='upload_script'),
    path('upload_script_done/', views.upload_script_done, name='upload_script_done'),
    path('remove_script/', views.remove_script, name='remove_script'),
    path('upload_json/', views.upload_json, name='upload_json'),
]