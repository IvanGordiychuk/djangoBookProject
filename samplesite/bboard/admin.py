from django.contrib import admin

from .models import Bb
from .models import Rubric
admin.site.register(Rubric)


class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )
    list_display = ('title', 'content', 'price', 'published', 'rubric')

admin.site.register(Bb, BbAdmin)# Register your models here.
