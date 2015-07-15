from django.contrib import admin
from .models import Course,Module,Topic,Activity,Lesson
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'discription')

class ModuleAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'discription')

class TopicAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'discription')

class LessonAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'discription')

class ActivityAdmin(admin.ModelAdmin):
   list_display = ('name', 'code', 'discription')
   
   
admin.site.register(Course,CourseAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Topic,TopicAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Activity,ActivityAdmin)