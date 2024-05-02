from django.apps import AppConfig


class SchdapiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "schdapi"

    def ready(self):
        import schdapi.signals
