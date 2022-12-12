from django.contrib import admin
from myapp import models

# Register your models here.
admin.site.register(models.Tabla_test, admin.ModelAdmin)
admin.site.register(models.Project, admin.ModelAdmin)