# 見た目に関するビューを記述するファイル
from django.shortcuts import render, redirect, get_object_or_404 # render, redirect, get_object_or_404をインポートする
from .models import Campsite, Booking, WeatherArea  # Campsite, Booking, WeatherAreaモデルをインポートする
from .forms import BookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import requests


def homepage(request):
    campsites = Campsite.objects.all()  # 全てのキャンプ場を取得
    return render(request, "blog/homepage.html", {"campsites": campsites})


    # # WeatherAreaモデルから最初のエリアコードを取得
    # weather_area = WeatherArea.objects.first()
    # if weather_area:
    #     area_code = weather_area.area_code  # エリアコードを取得
    # else:
    #     area_code = "130000"  # デフォルト値（東京）

    # # APIエンドポイントを動的に生成
    # weather_url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"

    # # APIから天気予報データを取得
    # response = requests.get(weather_url)
    # weather_data = response.json()

    # # 天気予報の概要を加工
    # weather_overview = weather_data[0]["publishingOffice"]

    # # 今日の天気予報を加工
    # today_weather = weather_data[0]["timeSeries"][0]["areas"][0]
    # forecasts = {
    #     "weathers": today_weather["weathers"][0],  # 天気情報
    #     "winds": today_weather["winds"][0],  # 風情報
    # }

    # # 東京地方の平均気温と降水量を抽出
    # temp_precip_data = weather_data[-1]  # 最後の要素に平均気温と降水量が含まれています
    # tokyo_data = next(
    #     area
    #     for area in temp_precip_data["tempAverage"]["areas"]
    #     if area["area"]["code"] == "44132"
    # )
    # tokyo_temps = {"min": tokyo_data["min"], "max": tokyo_data["max"]}
    # tokyo_precip = {
    #     "min": temp_precip_data["precipAverage"]["areas"][0]["min"],
    #     "max": temp_precip_data["precipAverage"]["areas"][0]["max"],
    # }

    # # 天気予報のデータをテンプレートに渡す
    # context = {
    #     "weather_overview": weather_overview,
    #     "forecasts": forecasts,
    #     "tokyo_temps": tokyo_temps,
    #     "tokyo_precip": tokyo_precip,
    # }
    # return render(request, "blog/homepage.html", context)


# キャンプ場詳細ページのビュー
def campsite_detail(request, pk):
    campsite = get_object_or_404(Campsite, pk=pk)
    return render(request, "blog/campsite_detail.html", {"campsite": campsite})


# ユーザーのログイン処理
def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("homepage")
        else:
            return render(
                request,
                "blog/login.html",
                {"error": "無効なユーザー名またはパスワードです。"},
            )
    else:
        return render(request, "blog/login.html")


# ユーザーのログアウト処理
def user_logout(request):
    logout(request)
    return redirect("homepage")


# 予約作成ビュー
@login_required
def create_booking(request, campsite_id):
    campsite = get_object_or_404(Campsite, pk=campsite_id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.campsite = campsite
            booking.save()
            return redirect("booking_detail", booking_id=booking.id)
    else:
        form = BookingForm()
    return render(
        request, "blog/create_booking.html", {"form": form, "campsite": campsite}
    )


# 予約詳細ビュー
@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    return render(request, "blog/booking_detail.html", {"booking": booking})
