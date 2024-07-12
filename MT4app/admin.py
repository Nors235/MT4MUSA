from django.contrib import admin
from .models import Service
from .models import Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Review)
admin.site.register(Service)

      
