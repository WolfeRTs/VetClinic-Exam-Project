from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VetClinic.accounts'

    def ready(self):
        import VetClinic.accounts.signals
