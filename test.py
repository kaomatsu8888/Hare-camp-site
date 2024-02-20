import requests
import json

# JSONファイルを読み込む。検証ツールで取得した天気コード
weather_code_file_path = (
    "/Users/kaorumatsunaga/mybusinessproduct/hare-camp/(API)weathercode.json"
)
with open(weather_code_file_path) as f:
    weather_codes = json.load(f)

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/110000.json"


def get_weather_info(
    code,
):  # 天気コードに基づいて説明とアイコンファイル名を取得します。
    """天気コードに基づいて説明とアイコンファイル名を取得します。"""
    code_str = str(code)
    default_value = {"description": "不明な天気コード", "icon": "不明なアイコン"}
    weather_info = weather_codes.get(code_str, default_value)
    if isinstance(weather_info, list):
        return {"description": weather_info[3], "icon": weather_info[0]}
    else:
        return weather_info


def get_weather_forecast():  # 天気予報を取得する関数
    try:  # 例外処理を追加
        response = requests.get(url)  # APIから天気予報データを取得
        data = response.json()  # JSON形式に変換
        print("データ取得成功")  # データ取得成功のメッセージを出力

        for item in data:  # dataのデータを取得
            for series in item["timeSeries"]:  # timeSeriesのデータを取得
                if "areas" in series:  # areasがある場合
                    for area in series["areas"]:  # areasのデータを取得
                        print(f"----{area['area']['name']}----")  # 地域名の出力
                        # 天気コードとアイコンの出力
                        if "weatherCodes" in area:  # weatherCodesがある場合
                            for i, code in enumerate(area["weatherCodes"]):
                                weather_info = get_weather_info(
                                    code
                                )  # 天気コードに基づいて説明とアイコンファイル名を取得
                                print(
                                    f"{series['timeDefines'][i]}: {weather_info['description']} (アイコン: {weather_info['icon']})"
                                )
                        # 降水確率の出力
                        if "pops" in area:  # pops(降水確率)がある場合
                            pops = area["pops"]
                            for i, pop in enumerate(pops):  # 降水確率の出力
                                print(f"{series['timeDefines'][i]}: 降水確率 {pop}%")
                        # 最低・最高気温の出力
                        if "tempsMin" in area and "tempsMax" in area:
                            temps_min = area["tempsMin"]
                            temps_max = area["tempsMax"]
                            for i, temp_min in enumerate(temps_min):  # 最低気温の出力
                                temp_max = (
                                    temps_max[i]
                                    if i < len(temps_max)
                                    else "不明"  # 最高気温の出力
                                )
                                print(
                                    f"{series['timeDefines'][i]}: 最低気温 {temp_min}度, 最高気温 {temp_max}度"
                                )

    except Exception as error:
        print(f"エラーが発生しました: {error}")


get_weather_forecast()

# 出力結果はこんな感じ.
# ----埼玉県----
# 2021-07-25T06:00:00+09:00: 曇り (アイコン: 03)
# 2021-07-25T09:00:00+09:00: 曇り (アイコン: 03)
