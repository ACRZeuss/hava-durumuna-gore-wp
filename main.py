import requests
import ctypes
import datetime
import time
from datetime import date


SPI_SETDESKWALLPAPER = 20
path_to_folder = r"C:\Users\erhan\Desktop\Wallpapers"
#Buraya arka plan resimlerimizin bulunduğu klasörümüzün tam yolunu ekliyoruz.

api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
city = "adana"

url = api_address + city


def main():
    timestamp = datetime.datetime.now().time()
    start_night = datetime.time(18, 1)
    end_night = datetime.time(6, 0)
    start_day = datetime.time(6, 1)
    end_day = datetime.time(18, 0)
    json_data = requests.get(url).json()
    format_data = json_data["weather"][0]["main"]
    print("Looped")

    if date.today().weekday() == 6:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\sunday.jpg", 3)
        time.sleep(120)
        print("Sunday")
        main()
    if format_data == "Rain":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\sainy_night.jpg", 3)
        time.sleep(120)
        print("Rain")
        main()
    elif format_data == "Thunderstorm":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\storm.jpeg", 3)
        time.sleep(120)
        print("Storm")
        main()
    elif format_data == "Drizzle":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\drizzle.jpg", 3)
        time.sleep(120)
        print("Drizzle")
        main()

# Night & Day
    elif format_data == "Clear" and start_night <= timestamp or timestamp <= end_night:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\might.jpeg", 3)
        time.sleep(120)
        print("Night")
        main()
    elif format_data == "Clear" and start_day <= timestamp <= end_day:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\clear.jpeg", 3)
        time.sleep(120)
        print("Day")
        main()

    elif format_data == "Clouds":
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\cloud.jpeg", 3)
        time.sleep(120)
        print("Clouds")
        main()
    else:
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path_to_folder + "\star_wars.png", 3)
        time.sleep(120)
        print("Other")
        main()


main()