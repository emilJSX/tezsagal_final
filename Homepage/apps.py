from django.apps import AppConfig


class HomepageConfig(AppConfig):
    name = 'Homepage'
    
    def  ready(self):
        import Homepage.signals #accounts is a name of app
