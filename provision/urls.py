from django.conf.urls import url
from . import views

app_name = 'provision'
urlpatterns = [
    url(r'^box_details/$', views.IndexView, name='index'),
    url(r'^$', views.AddBoxView, name='add_box'),
]
