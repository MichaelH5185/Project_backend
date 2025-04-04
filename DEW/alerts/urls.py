from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('alert/<str:pk>', views.alert, name="alert"),
    path('delete/<str:pk>', views.delete_alerts, name="delete")
]