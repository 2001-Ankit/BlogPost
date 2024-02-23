from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.register(Permission)