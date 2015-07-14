from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserAdmin(admin.ModelAdmin):
   list_display = ('user', 'website', 'picture')
    
admin.site.register(UserProfile,UserAdmin)