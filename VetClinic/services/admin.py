from django.contrib import admin

from VetClinic.services.models import ServiceCategory, Service, Medicine


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'category', 'description')
    list_filter = ('category',)
    search_fields = ('name', 'description', 'category__name')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'name_bg', 'name_en', 'description', 'description_bg', 'description_en', 'category',),
        }),
    )


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'dosages',)
    search_fields = ('name', 'description', 'dosages')
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'description_bg', 'description_en', 'dosages',),
        }),
    )
