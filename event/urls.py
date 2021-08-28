from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.login,name="admin_login"),
    path('events',views.events,name="events"),
    path('event_details/<event_id>',views.event_details,name="event-details"),
    path('bootcamp',views.bootcamp,name="bootcamp"),
    path('concert',views.concert,name="concert"),
    path('register/<event_id>',views.register,name="register"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('create_event',views.create_event,name="create-event"),
    path('update_events', views.update_events,name="update_events"),
    path('edit_event/<event_id>',views.edit_event,name="edit-event"),
    path('delete_event/<event_id>',views.delete_event,name="delete_event"),
    path('data_students/<event_id',views.data_students,name="data_students"),
]