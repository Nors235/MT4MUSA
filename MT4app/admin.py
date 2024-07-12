from django.contrib import admin
from .models import Service
from .models import Review
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

admin.site.register(Review)
admin.site.register(Service)

class admin.py(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

      
