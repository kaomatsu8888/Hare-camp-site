# blog/tests.py データベースに反映されなかった為テストケースを作成
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Campsite, Booking
from datetime import date


class BookingTests(TestCase):
    def setUp(self):
        # テスト用のユーザーを作成
        self.user = User.objects.create_user(username="testuser", password="12345")
        # テスト用のキャンプサイトを作成
        self.campsite = Campsite.objects.create(
            name="Test Campsite", location="Test Location", amenities="Basic amenities")
        

    def test_create_booking(self):
        # テスト用のユーザーでログイン
        self.client.login(username="testuser", password="12345")

        # 予約データを作成
        booking_data = {
            "campsite": self.campsite.id,
            "start_date": date.today(),
            "end_date": date.today(),
            "num_people": 4,
        }

        # 予約作成のビューをテスト
        response = self.client.post(
            "/campsite/{}/book/".format(self.campsite.id), booking_data
        )

        # レスポンスコードが302であることを確認（リダイレクトされる）
        self.assertEqual(response.status_code, 302)

        # 予約がデータベースに保存されているか確認
        bookings = Booking.objects.filter(user=self.user)
        self.assertEqual(bookings.count(), 1)
        self.assertEqual(bookings.first().num_people, 4)
