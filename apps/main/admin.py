from django.contrib import admin
from .models import Carousel, Contact, Category


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
