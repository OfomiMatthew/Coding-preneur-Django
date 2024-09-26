from django.contrib import admin
from .models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display=['title','content']
  search_fields =['title']
admin.site.register(Article,ArticleAdmin)
