from django.apps import AppConfig


class MyportfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myportfolio'
    
    def ready(self):
        import myportfolio.translation
