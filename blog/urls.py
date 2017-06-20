from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success/$', views.success, name='success'),
    url(r'^post/(?P<pk>\d+)/$', views.post, name='post'),
]
