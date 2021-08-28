from django.urls import path
from . import views

urlpatterns = [
    path('admin_login',views.admin_login,name="admin-login"),
    path('admin_logout',views.admin_logout,name="admin-logout")
]