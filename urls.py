from django.conf.urls import url
from . import views

app_name = 'todo'

urlpatterns = [
    # ex: /todo/overview/
    url(r'^overview/$', views.overview),
    # ex: /todo/alltodo/
    url(r'^alltodo/$', views.alltodo),
	# ex: /todo/addtodo/
    url(r'^addtodo/$', views.addtodo, name='addtodo'),
]
