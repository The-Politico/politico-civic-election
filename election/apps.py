from django.apps import AppConfig


class ElectionConfig(AppConfig):
    name = 'election'

    def ready(self):
        from election import signals  # noqa
