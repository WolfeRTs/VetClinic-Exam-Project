from django.contrib import admin
from django.utils.safestring import mark_safe

from VetClinic.images.models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'category', 'date_uploaded')
    list_filter = ('category', 'date_uploaded')
    search_fields = ('category',)
    ordering = ('-date_uploaded',)
    readonly_fields = ('date_uploaded', 'image_preview')
    fieldsets = (
        (None, {
            'fields': ('image', 'image_preview', 'category', 'date_uploaded'),
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px;" />')
        return "No Image"

    image_preview.short_description = "Image Preview"