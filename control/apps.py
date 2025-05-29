from django.apps import AppConfig


class ControlConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "control"

    def ready(self):
        # Import and initialize GPIO
        from .gpio_setup import init_gpio
        init_gpio()
