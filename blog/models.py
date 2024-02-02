# モデルに関する処理を記述するファイル.モデルとはデータベースのテーブルのようなもの
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# キャンプ場のモデル
class Campsite(models.Model):
    name = models.CharField('キャンプ場名', max_length=255)  # キャンプ場名は文字列で保存
    location = models.CharField('場所', max_length=255)  # 場所は文字列で保存
    description = models.TextField('説明')
    amenities = models.JSONField('アメニティ')  # アメニティはJSON形式で保存
    image = models.ImageField('画像', upload_to='campsites/')  # 画像はcampsites/ディレクトリにアップロード

    def __str__(self): # 管理画面で表示する文字列
        return self.name

# 予約のモデル
class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name='ユーザー', on_delete=models.CASCADE, related_name='bookings')
    campsite = models.ForeignKey(Campsite, verbose_name='キャンプ場', on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField('開始日')
    end_date = models.DateField('終了日')
    num_people = models.IntegerField('人数')

    def __str__(self):
        return f"{self.user.username} - {self.campsite.name}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField() #textfiledは入力文字数制限なし
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) #auto_now_add=Trueは投稿日時を自動で入力する

class Comment(models.Model):# forms.pyで作成したモデルをここで作成する
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # Cascadeは投稿が削除されたら全ての情報を削除する(本文、email、名前)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) #auto_now_add=Trueは投稿日時を自動で入力する
