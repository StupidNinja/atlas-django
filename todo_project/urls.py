from django.contrib import admin
from django.urls import path, include
from todos.views import status_list  
from todos.views import category_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include('todos.urls')),
    path('api/users/', include('users.urls')),
    path('api/statuses/', status_list),
    path('categories/', category_list, name='category-list')  
]
