from django.urls import path
from todo_app import views

urlpatterns = [
    path('',views.todo_list, name="todo-list"),
    path('todo-delete/<int:id>/',views.todo_delete,name="todo-delete"),
    path('todo-create/',views.todo_create,name="todo-create"),
    path('todo-update/<int:id>/',views.todo_update,name="todo-update"),
]
