# 新しくform.pyを作成し、PostFormという名前のフォームを作成する
from django import forms
from .models import Comment #Commentモデルをインポートする

class CommentForm(forms.ModelForm): 
    class Meta:
        # コメントをデータベースに保存するためのモデルを指定する
        model = Comment
        # フォームのフィールドを指定する.どういう情報を入力するかを指定する
        fields = ["name", "email", "body"]
        # models.pyへコメントのモデルを作成する→go
