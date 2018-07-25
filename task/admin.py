from django.contrib import admin
from .models import TaskResult, Task, CaseFile, Case

admin.site.register(TaskResult, admin.ModelAdmin)
admin.site.register(Task, admin.ModelAdmin)
admin.site.register(CaseFile, admin.ModelAdmin)
admin.site.register(Case, admin.ModelAdmin)