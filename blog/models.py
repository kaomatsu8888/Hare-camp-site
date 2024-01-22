from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField() #textfiledは入力文字数制限なし
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) #auto_now_add=Trueは投稿日時を自動で入力する


class Comment(models.Model):# forms.pyで作成したモデルをここで作成する
    # 投稿1に対してコメントは複数つく。1対多の関係そこでForeignKeyを使う
    # related_nameは連絡先。on_deleteは投稿が削除されたらコメントも削除する
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments") # Cascadeは投稿が削除されたら全ての情報を削除する(本文、email、名前)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) #auto_now_add=Trueは投稿日時を自動で入力する


