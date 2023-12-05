from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import All

@admin.register(All)
class AllAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_image']

    def display_image(self, obj):
        return mark_safe ('<img src="{}" height="100" />'.format(obj.image_file.url))

    display_image.short_description = 'All'
