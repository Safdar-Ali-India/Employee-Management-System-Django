from django.contrib import admin    
from .models import Employee,Title, Department
# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    list_display =['id','name']

admin.site.register(Employee)
admin.site.register(Title,TitleAdmin)
admin.site.register(Department)