from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^sky/astro_images/$', views.astro_images, name='astro_images'),
#    url(r'^$', views.astro_images, name='astro_images'),    #didnt work
    url(r'^sky/astro_view/$', views.astro_view, name='astro_view'),    
]