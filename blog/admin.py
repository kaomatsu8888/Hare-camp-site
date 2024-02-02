# 管理者ツール
from django.contrib import admin  # adminモジュールをインポートする
from .models import (
    Post,
    Comment,
)  # Commentモデルをインポートする.adminにcommentsの管理画面を追加する
from .models import (
    Campsite,
    Booking,
)  # Campsiteモデルをインポートする.adminにcampsitesの管理画面を追加する

admin.site.register(Post)  # adminにpostsの管理画面を追加する
admin.site.register(Comment)  # adminにcommentsの管理画面を追加する


# Register your models here.
@admin.register(Campsite)  # adminにcampsitesの管理画面を追加する
class CampsiteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "description",
        "amenities",
    )  # リストに表示するフィールド
    search_fields = ("name", "location")  # 検索可能なフィールド
    list_filter = ("location",)  # リストフィルタとして使用するフィールド


# Bookingモデルのadmin登録
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "campsite", "start_date", "end_date", "num_people")
    list_filter = ("campsite", "start_date", "end_date")
    search_fields = ("user__username", "campsite__name")
