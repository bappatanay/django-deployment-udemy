from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    re_path(r'^relative/$',views.relative_url_template,name='relative_url_template'),
    re_path(r'^other/$', views.other, name='other'),
    ]
