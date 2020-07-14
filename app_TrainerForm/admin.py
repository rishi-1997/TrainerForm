from django.contrib import admin
from .models import Trainer
# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['first_name','middle_name','last_name','trainer_id','address']

admin.site.register(Trainer,TrainerAdmin)