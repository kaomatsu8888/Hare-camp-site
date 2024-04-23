"""
WSGI config for microblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
# WSGIというwebアプリケーションのためのインターフェースを提供するモジュール
import os
from dj_static import Cling # 静的ファイルを配信するためのモジュール.Heroku使用の為に追加
from django.core.wsgi import get_wsgi_application 

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "microblog.settings")

application = Cling(get_wsgi_application()) 
# WSGIアプリケーションを取得.wsgiアプリケーションはWSGIインターフェースを提供するためのもの.clingは静的ファイルを配信するためのものHeroku使用の為に追加
