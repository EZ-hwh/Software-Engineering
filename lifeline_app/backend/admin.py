from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Timezone)
admin.site.register(Board)
admin.site.register(Homework)
admin.site.register(Scheduler)
admin.site.register(Todolist)
admin.site.register(Register)
admin.site.register(Takeclass)

