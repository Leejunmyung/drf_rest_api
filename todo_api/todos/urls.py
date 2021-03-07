from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/', views.todo_create),
    path('todos/<int:todo_id>', views.todo_detail),
    path('todos/<int:todo_id>', views.todo_update_and_delete),
    path('todos/<int:todo_id>/comment/', views.comment_list),
    path('todos/<int:todo_id>/comment/<int:comment_id>', views.comment_create),
    path('todos/<int:todo_id>/comment/<int:comment_id>', views.comment_update_and_delete),
]