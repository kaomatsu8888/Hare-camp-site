
from django.contrib import admin
from django.urls import path
from blog.views import frontpage, post_detail

# ルーターの役割を担う
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", frontpage),
    # クリックしたら投稿の詳細ページに飛ぶ
    path("<slug:slug>/", post_detail, name="post_detail") #投稿1のURLがpost-1, 投稿2のURLがpost-2となる
]
