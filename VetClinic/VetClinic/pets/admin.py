from django.contrib import admin
from django.contrib.auth import get_user_model

from VetClinic.pets.models import Pet, PetStatus, MedicalReport

UserModel = get_user_model()


class VetDoctorFilter(admin.SimpleListFilter):
    title = 'doctor'
    parameter_name = 'doctor'

    def lookups(self, request, model_admin):
        vet_doctors = UserModel.objects.filter(is_vet=True)
        return [(user.id, user.username) for user in vet_doctors]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(doctor_id=self.value())
        return queryset


class PetStatusInline(admin.StackedInline):
    model = PetStatus
    can_delete = False
    verbose_name_plural = 'PetStatuses'

    list_display = ('is_neutered', 'is_vaccinated', 'last_vaccinated_at', 'last_external_deworming', 'last_internal_deworming')


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    inlines = [PetStatusInline,]
    list_display = ('name', 'species', 'breed', 'sex', 'owner', 'date_of_birth', 'date_added')
    list_filter = ('species', 'sex', 'date_added')
    search_fields = ('name', 'species', 'breed', 'owner__username')
    ordering = ('-date_added',)
    readonly_fields = ('date_added',)
    fieldsets = (
        (None, {
            'fields': ('name', 'species', 'breed', 'sex', 'date_of_birth', 'owner', 'date_added'),
        }),
    )


@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pet', 'doctor', 'doctor_name', 'date_added', 'date_updated')
    list_filter = ('date_added', 'date_updated', VetDoctorFilter, 'doctor_name')
    search_fields = ('title', 'description', 'instructions', 'doctor_name', 'pet__name')
    ordering = ('-date_added',)
    readonly_fields = ('date_added', 'date_updated')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'instructions', 'pet', 'doctor', 'doctor_name',
                       'date_added', 'date_updated'),
        }),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "doctor":
            kwargs["queryset"] = UserModel.objects.filter(is_vet=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)