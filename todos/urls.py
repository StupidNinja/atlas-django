from django.urls import path
from .views import TodoListCreateView, TodoDetailView, category_list, tag_detail, CommentCreateView, comment_list

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('categories/', category_list, name='category-list'),
    path('tags/<int:pk>/', tag_detail, name='tag-detail'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('<int:todo_id>/comments/', comment_list, name='comment-list'),  # New endpoint
]