from django.contrib import admin
from .models import Todo, Category, Tag, Comment

admin.site.register(Todo)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)