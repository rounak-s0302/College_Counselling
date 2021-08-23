from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("registration/", views.registration, name="registration"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete")
    ]
