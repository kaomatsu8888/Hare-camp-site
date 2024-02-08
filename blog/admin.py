# 管理者ツール
from django.contrib import admin  # adminモジュールをインポートする
from .models import (
    Post,
    Comment,
)  # PostモデルとCommentモデルをインポートする.adminにpostsとcommentsの管理画面を追加する
from .models import (
    Campsite,
    Booking,
    WeatherArea,
)  # CampsiteモデルとBookingモデルをインポートする.adminにcampsitesとbookingsの管理画面を追加する

admin.site.register(Post)  # adminにpostsの管理画面を追加する
admin.site.register(Comment)  # adminにcommentsの管理画面を追加する


# Register your models here.
@admin.register(Campsite)
class CampsiteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "location",
        "description",
        "amenities",
        "access_info",
        "price",
        "phone_number",
    )  # 新しいフィールドをリスト表示に追加
    search_fields = (
        "name",
        "location",
        "price",
        "phone_number",
    )  # 電話番号と料金を検索フィールドに追加する場合
    list_filter = ("location", "weather_area",)  # 既存のリストフィルタ


# Bookingモデルのadmin登録
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("user", "campsite", "start_date", "end_date", "num_people")
    list_filter = ("campsite", "start_date", "end_date")
    search_fields = ("user__username", "campsite__name")

# WeatherAreaモデルのadmin登録
@admin.register(WeatherArea)
class WeatherAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "area_code")
    search_fields = ("name",)
