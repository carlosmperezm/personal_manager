from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_index, name = 'todo_index'),
    path('add', views.create_todo, name = 'create_todo'),
    path('update/<int:id>', views.update_todo, name = 'update_todo'),
    path('view/<int:id>', views.view_todo, name = 'view_todo'),
    path('delete/<int:id>', views.delete_todo, name = 'delete_todo'),
]
