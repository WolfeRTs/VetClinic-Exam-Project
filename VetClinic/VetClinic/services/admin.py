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
    filter_horizontal = ('reports',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'reports'),
        }),
    )


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'description', 'dosages',)
    search_fields = ('name', 'description', 'dosages')
    ordering = ('name',)
    filter_horizontal = ('reports',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'dosages',),
        }),
    )
