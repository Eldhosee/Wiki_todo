from django.urls import path

from encyclopedia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>",views.input ,name="title"),
    path("search", views.search, name="search"),
    path("newpage",views.newpage,name="newpage"),
    path("submit",views.submit,name="submit"),
    path("edit",views.edit,name="edit"),
    path("save",views.save,name="save"),
    path("randompage",views.randompage,name="randompage"),

]
