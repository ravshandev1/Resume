from django.contrib import admin
from .models import About, Resume, Skill, Service, Project


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id']
    filter_horizontal = ['category']
