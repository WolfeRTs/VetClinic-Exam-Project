from django.apps import AppConfig


class PetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VetClinic.pets'

    def ready(self):
        import VetClinic.pets.signals
