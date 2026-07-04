from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addTodo, name='add'),
    path('complete/<todo_id>', views.completeTodo, name='complete'),
    path('uncomplete/<todo_id>', views.uncompleteTodo, name='uncomplete'),
    path('delete/<todo_id>', views.deleteTodo, name='delete'),
    path('edit/<todo_id>', views.editTodo, name='edit'),
    path('deletecomplete', views.deleteCompleted, name='deletecomplete'),
    path('deleteall', views.deleteAll, name='deleteall'),
    path('deleteselected', views.deleteSelected, name='deleteselected'),
]
