from django.conf.urls import include, url
from django.contrib import admin
from socketio import sdjango


sdjango.autodiscover()

urlpatterns = [
	url(r'^', include('notifications.urls')),
    url(r'^socket\.io', include(sdjango.urls)),
]
