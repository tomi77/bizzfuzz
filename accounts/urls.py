from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'accounts.views.index', name='index'),
                       url(r'^edit/(\d+)/$', 'accounts.views.edit', name='edit'),
                       url(r'^view/(\d+)/$', 'accounts.views.view', name='view'),
                       url(r'^del/(\d+)/$', 'accounts.views.delete', name='del'),
                       url(r'^add/$', 'accounts.views.add', name='add'))
