from django.contrib import admin
from .models import Post, Comment #Commentモデルをインポートする.adminにcommentsの管理画面を追加する

admin.site.register(Post) #adminにpostsの管理画面を追加する
admin.site.register(Comment) #adminにcommentsの管理画面を追加する
