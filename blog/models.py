# モデルに関する処理を記述するファイル.モデルとはデータベースのテーブルのようなもの
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


# キャンプ場のモデル
class Campsite(models.Model):
    name = models.CharField("キャンプ場名", max_length=255)
    location = models.CharField("場所", max_length=255)
    description = models.TextField("キャンプ場の説明")
    amenities = models.JSONField("設備")
    image = models.ImageField("画像", upload_to="campsites/")
    access_info = models.TextField("アクセス情報", blank=True)
    price = models.CharField("料金", max_length=255, blank=True)
    phone_number = models.CharField("電話番号", max_length=20, blank=True)
    weather_area = models.CharField("天気予報エリアコード", max_length=10, blank=True)  # 新しいフィールド

    def __str__(self):  # 管理画面で表示する文字列
        return self.name

    # 画像が消えなかったので削除するための処理を追加
    def save(self, *args, **kwargs):
        # 既存のインスタンスを確認して、画像が変更されているかチェック
        if self.pk:  # インスタンスが既存の場合
            old_image = Campsite.objects.get(pk=self.pk).image  # 既存の画像を取得
            if old_image != self.image:  # 画像が変更されている場合
                if os.path.isfile(old_image.path):  # 画像ファイルが存在する場合
                    os.remove(old_image.path)  # 画像ファイルを削除
        super().save(*args, **kwargs)  # 画像を保存


# モデルが削除された後に画像ファイルも削除するためのシグナル
@receiver(post_delete, sender=Campsite)  # Campsiteモデルが削除された後に実行
def submission_delete(sender, instance, **kwargs):  # 画像ファイルを削除
    instance.image.delete(False)  # 画像ファイルを削除


# 予約のモデル
class Booking(models.Model):
    user = models.ForeignKey(
        User, verbose_name="ユーザー", on_delete=models.CASCADE, related_name="bookings"
    )
    campsite = models.ForeignKey(
        Campsite,
        verbose_name="キャンプ場",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    start_date = models.DateField("開始日")
    end_date = models.DateField("終了日")
    num_people = models.IntegerField("人数")

    def __str__(self):
        return f"{self.user.username} - {self.campsite.name}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()  # textfiledは入力文字数制限なし
    body = models.TextField()
    posted_date = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=Trueは投稿日時を自動で入力する


class Comment(models.Model):  # forms.pyで作成したモデルをここで作成する
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )  # Cascadeは投稿が削除されたら全ての情報を削除する(本文、email、名前)
    name = models.CharField(max_length=255) # 名前の文字数制限
    email = models.EmailField()  # emailの形式で入力する
    body = models.TextField()
    posted_date = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add=Trueは投稿日時を自動で入力する

# 天気用のエリアモデル
class WeatherArea(models.Model):
    name = models.CharField(max_length=100, verbose_name="エリア名")
    area_code = models.CharField(max_length=6, verbose_name="エリアコード")

    def __str__(self):
        return self.name
