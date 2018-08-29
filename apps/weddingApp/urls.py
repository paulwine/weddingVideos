from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^portfolio$', views.portfolio),
    url(r'^info$', views.info),
    url(r'^contact$', views.contact)      # This line has changed!
  ]
