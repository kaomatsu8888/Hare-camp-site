# アプリ（はれ☀きゃん）の概要

最適なキャンプ情報をあなたにお届け

# 課題
- 客単価が安く、ネット予約対応が出来ない施設が多い(なっぷ参照)
- キャンプ予約日の天気情報を別に調べなければいけない ☆大切
- 周辺情報(例：温泉、食材を買える場所、ホームセンター、道の駅)を別に調べなければならない
- キャンプ場個別のレコメンド情報が取れない

# 解決策
- 電話予約のキャンプ場をネット予約可に
- 予約ポータルサイトの作成とUIの改善

# ターゲット
- 宿泊費を節約したいオート・モトキャンパー
- お気に入りキャンプ場の詳細情報をすぐ知りたい家族キャンパー
- 費用的なコストで大手サイトに掲載していない施設
- 公営キャンプ場(高コスパ) + キャンプ場大手サイトで単価割れしているプランを掲載

# アプリの概要
- ログインしたユーザーに対してキャンプ場情報を提供 
- 天気情報をAPIで取得。表示
- 日程を表示して予約 予約情報をマイページで確認できる
- 晴れの日で検索サイトできる晴れの日検索を実装

# 市場規模
- 全てのキャンプ場は5000箇所ほど(なっぷ参照)
 オートキャンプ場は827箇所(2023オートキャンプ場雑誌参照)
- 公営キャンプ場は250箇所(試算)岩手では10ほど
# 競合サービス
- 株式会社スペースキー 様
- 楽天トラベル 様


## 使用技術
フロントエンド
- HTML/CSS

バックエンド
- Python 3.11.5
- Django 4.2.6

## 機能一覧
- キャンプ場登録機能
- 天気機能を追加 →OpenWeatherAPIを使用していたが、精度難ありのため
  気象庁のAPIに変更
- 気象庁のAPIを使用して、天気とアイコンは取得出来た。まだビューに反映出来てないです。

## 天気API出力結果例
- データ取得成功
- ----北部----
- 2024-03-18T11:00:00+09:00: 晴 (アイコン: 100.svg)
- 2024-03-19T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-20T00:00:00+09:00: 曇一時雨か雪 (アイコン: 202.svg)
- ----南部----
- 2024-03-18T11:00:00+09:00: 晴 (アイコン: 100.svg)
- 2024-03-19T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-20T00:00:00+09:00: 曇一時雨か雪 (アイコン: 202.svg)
- ----秩父地方----
- 2024-03-18T11:00:00+09:00: 晴 (アイコン: 100.svg)
- 2024-03-19T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-20T00:00:00+09:00: 曇一時雪か雨 (アイコン: 204.svg)
- ----北部----
- 2024-03-18T12:00:00+09:00: 降水確率 0%
- 2024-03-18T18:00:00+09:00: 降水確率 0%
- 2024-03-19T00:00:00+09:00: 降水確率 0%
- 2024-03-19T06:00:00+09:00: 降水確率 0%
- 2024-03-19T12:00:00+09:00: 降水確率 10%
- 2024-03-19T18:00:00+09:00: 降水確率 10%
- ----南部----
- 2024-03-18T12:00:00+09:00: 降水確率 0%
- 2024-03-18T18:00:00+09:00: 降水確率 0%
- 2024-03-19T00:00:00+09:00: 降水確率 0%
- 2024-03-19T06:00:00+09:00: 降水確率 0%
- 2024-03-19T12:00:00+09:00: 降水確率 10%
- 2024-03-19T18:00:00+09:00: 降水確率 10%
- ----秩父地方----
- 2024-03-18T12:00:00+09:00: 降水確率 0%
- 2024-03-18T18:00:00+09:00: 降水確率 0%
- 2024-03-19T00:00:00+09:00: 降水確率 0%
- 2024-03-19T06:00:00+09:00: 降水確率 0%
- 2024-03-19T12:00:00+09:00: 降水確率 10%
- 2024-03-19T18:00:00+09:00: 降水確率 10%
- ----熊谷----
- ----さいたま----
- ----秩父----
- ----埼玉県----
- 2024-03-19T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-20T00:00:00+09:00: 曇一時雨か雪 (アイコン: 202.svg)
- 2024-03-21T00:00:00+09:00: 晴時々曇 (アイコン: 101.svg)
- 2024-03-22T00:00:00+09:00: 晴時々曇 (アイコン: 101.svg)
- 2024-03-23T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-24T00:00:00+09:00: 曇時々晴 (アイコン: 201.svg)
- 2024-03-25T00:00:00+09:00: 曇一時雨 (アイコン: 202.svg)
- 2024-03-19T00:00:00+09:00: 降水確率 %
- 2024-03-20T00:00:00+09:00: 降水確率 50%
- 2024-03-21T00:00:00+09:00: 降水確率 20%
- 2024-03-22T00:00:00+09:00: 降水確率 20%
- 2024-03-23T00:00:00+09:00: 降水確率 30%
- 2024-03-24T00:00:00+09:00: 降水確率 30%
- 2024-03-25T00:00:00+09:00: 降水確率 50%
- ----熊谷----
- 2024-03-19T00:00:00+09:00: 最低気温 度, 最高気温 度
- 2024-03-20T00:00:00+09:00: 最低気温 3度, 最高気温 12度
- 2024-03-21T00:00:00+09:00: 最低気温 3度, 最高気温 11度
- 2024-03-22T00:00:00+09:00: 最低気温 2度, 最高気温 12度
- 2024-03-23T00:00:00+09:00: 最低気温 1度, 最高気温 14度
- 2024-03-24T00:00:00+09:00: 最低気温 6度, 最高気温 19度
- 2024-03-25T00:00:00+09:00: 最低気温 11度, 最高気温 21度




## 現在の状況
- API変更に伴い作成し直し
- ビューページを編集中
- 構成やり直し

スクリーンショット
<img width="1445" alt="スクリーンショット 2024-03-19 11 03 06" src="https://github.com/kaomatsu8888/Hare-camp-site/assets/61591650/3cce2e1e-9976-4906-9dc7-ff6078131f25">
<img width="1395" alt="スクリーンショット 2024-03-18 13 43 33" src="https://github.com/kaomatsu8888/Hare-camp-site/assets/61591650/c9ee1f6d-e5cd-40db-be3a-c165c2a87a8d">
<img width="1418" alt="スクリーンショット 2024-03-18 13 48 06" src="https://github.com/kaomatsu8888/Hare-camp-site/assets/61591650/0bec83c3-00aa-47c9-8cd8-74543ff87faf">



今後実装したい機能

・予約機能
・ログイン時、マイページ確認機能
・晴れ検索
