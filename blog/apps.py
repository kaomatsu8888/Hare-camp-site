from django.apps import AppConfig


class BlogConfig(AppConfig): #blogアプリの設定を行う
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
