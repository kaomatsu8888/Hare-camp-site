# プロジェクトで使うURLを管理するファイル
from django.urls import path
from blog import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # 管理サイトのURL
    path("", views.homepage, name="homepage"),  # トップページのURL
    path(
        "campsites/<int:pk>/", views.campsite_detail, name="campsite_detail"
    ),  # キャンプ場詳細ページのURL
    path(
        "campsite/<int:campsite_id>/book/", views.create_booking, name="create_booking"
    ),  # 予約作成ビューのURL
    path(
        "booking/<int:booking_id>/", views.booking_detail, name="booking_detail"
    ),  # 予約詳細ビューのURL
    path("login/", views.user_login, name="user_login"),  # ログインビューへのパス
    path('logout/', auth_views.LogoutView.as_view(next_page='user_login'), name='user_logout')  # ログアウトビューへのパス
]
"""
/logout/ に対する GET リクエストが許可されていないためです。
Django の LogoutView はデフォルトで POST リクエストのみを受け付けるように設定されています。
"""

# デバッグモードの場合、メディアファイルのURLを追加
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
