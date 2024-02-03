# 見た目に関するビューを記述するファイル
from django.shortcuts import render, redirect, get_object_or_404 # render, redirect, get_object_or_404をインポートする
from .models import Campsite, Booking
from .forms import BookingForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# トップページのビュー
def homepage(request):
    campsites = Campsite.objects.all()
    return render(request, "blog/homepage.html", {"campsites": campsites})


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
