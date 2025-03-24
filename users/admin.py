from django.contrib import admin
from .models import User  # Assuming you have a custom User model

admin.site.register(User)  # Register the User model with the admin site