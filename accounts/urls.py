from django.conf.urls import url

from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit/(\d+)/$', views.edit, name='edit'),
    url(r'^view/(\d+)/$', views.details, name='details'),
    url(r'^del/(\d+)/$', views.delete, name='del'),
    url(r'^add/$', views.add, name='add'),
]
