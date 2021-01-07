from django.contrib import admin

# Register your models here.
from assignment.models import Login, User

admin.site.register(Login)
admin.site.register(User)
