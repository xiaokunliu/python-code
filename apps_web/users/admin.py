# Register your models here.
from django.contrib import admin
from users.models import Users,UsersAdditional

admin.site.register(Users)
admin.site.register(UsersAdditional)


