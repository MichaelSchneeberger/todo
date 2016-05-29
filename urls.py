from django.conf.urls import url
from . import views

app_name = 'todo'

urlpatterns = [
    # ex: /todo/overview/
    url(r'^overview/$', views.overview),

    # ex: /todo/set_todo_as_done/
    url(r'^set_todo_as_done/$', views.set_todo_as_done, name='set_todo_as_done'),

    # ex: /todo/prostpone_date/
    url(r'^prostpone_date/$', views.prostpone_date, name='prostpone_date'),

    # ex: /todo/alltodo/
    url(r'^alltodo/$', views.alltodo),

	# ex: /todo/addtodo/
    url(r'^addtodo/$', views.addtodo, name='addtodo'),
]
