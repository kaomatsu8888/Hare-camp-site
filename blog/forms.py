# 新しくform.pyを作成し、PostFormという名前のフォームを作成する
from django import forms
from .models import Comment
from .models import Booking
from .models import Campsite
from django.core.validators import MinValueValidator # 最小値のバリデーションを行うためのモジュールをインポートする

class CommentForm(forms.ModelForm):
    class Meta:
        # コメントをデータベースに保存するためのモデルを指定する
        model = Comment
        # フォームのフィールドを指定する.どういう情報を入力するかを指定する
        fields = ["name", "email", "body"]
        # models.pyへコメントのモデルを作成する→go


class BookingForm(forms.ModelForm):
    num_people = forms.IntegerField(
        widget=forms.NumberInput(attrs={"min": 1}), validators=[MinValueValidator(1)]
    )

    class Meta:
        model = Booking
        fields = ["campsite", "start_date", "end_date", "num_people"]

    def clean_num_people(self):
        num_people = self.cleaned_data["num_people"]
        if num_people < 1:
            raise forms.ValidationError("予約人数は1人以上である必要があります。")
        return num_people


class CampsiteForm(forms.ModelForm):
    class Meta:
        model = Campsite
        fields = [
            "name",
            "location",
            "description",
            "amenities",
            "access_info",
            "price",
            "phone_number",
        ]
        # fields属性にフィールドの順番をリストとして指定する
