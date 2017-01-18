from django.conf.urls import url 
from . import views

urlpatterns = [
		
		
		url(r'^joinus/$', views.joinus),
		url(r'^search/$', views.search),
		url(r'^home/$', views.home),
]
