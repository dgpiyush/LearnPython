from django.urls import path, include
from . import views



urlpatterns = [
    path("",views.index, name="todos"),
    path("create/",views.create, name="create"),
    path("delete/<int:id>/",views.delete, name="delete"),
    path("edit/<int:id>/",views.edit, name="edit"),
    path("update/<int:id>/",views.update, name="update"),
    path("save/",views.save, name="save"),
    # admin docs
]
