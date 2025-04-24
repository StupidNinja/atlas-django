from django.urls import path
from .views import TodoListCreateView, TodoDetailView, category_list, tag_detail, CommentCreateView
from .views import status_list

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('categories/', category_list, name='category-list'),
    path('tags/<int:pk>/', tag_detail, name='tag-detail'),
    # Optional: Endpoint to create a comment for a todo
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('api/statuses/', status_list, name='status-list')
]