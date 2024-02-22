from django.contrib import admin
from .models import List

# Register your models here.

class ListAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','list_date')
    list_display_links = ('id','title')
    list_filter = ('city','state','pincode')
    search_fields = ('title','description','address','city','state','pincode','price')
admin.site.register(List, ListAdmin)