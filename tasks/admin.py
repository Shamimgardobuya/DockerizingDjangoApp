from django.contrib import admin

# Register your models here.
from tasks.models import Tasks, Profile

class TaskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Tasks, TaskAdmin)

class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile,ProfileAdmin)