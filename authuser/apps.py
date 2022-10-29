from django.apps import AppConfig


class AuthuserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "authuser"

    def ready(self):
        from . import signals
