from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="index.html"),
    path("register/", views.register, name="register.html"),
    path("addUser/", views.addUser, name="register.html"),
    # path("user-register/", views.user_register, name="user-register"),
]