from django.contrib import admin
from .models import Blog, Tag, Comment


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id']
    filter_horizontal = ['tags']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id']
