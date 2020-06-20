from django.urls import path
from . import views

urlpatterns = [
    path('', views.toDo, name="ToDo"),
    path("add_toDo/", views.add_toDo, name="add_toDo"),
    path("del_toDo/<int:todo_id>/", views.del_toDo, name="del_toDo"),
]