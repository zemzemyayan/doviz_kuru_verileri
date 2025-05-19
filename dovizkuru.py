from influxdb import InfluxDBClient
import requests
from datetime import datetime

# InfluxDB bağlantı ayarları (Docker'da çalıştığı için localhost:8086)
client = InfluxDBClient(
    host="localhost",
    port=8086,
    username="admin",       # Eğer kullanıcı ayarlamadıysan boş bırakabilirsin
    password="admin",       # Yoksa None yaz
    database="last1year"    # Veritabanını önceden oluşturman gerek
)

# Eğer veritabanı yoksa oluştur
dbs = client.get_list_database()
if not any(db['name'] == 'last1year' for db in dbs):
    client.create_database('last1year')
    print("Veritabanı oluşturuldu: last1year")
else:
    print("Veritabanı zaten var.")

# Veritabanına geç
client.switch_database('last1year')

# Tarihler
baslangic_tarihi = "2024-03-01"
bugun = datetime.today().strftime('%Y-%m-%d')

# API'den veri çek
api_url = f"https://api.frankfurter.app/{baslangic_tarihi}..{bugun}?from=USD&to=TRY"
response = requests.get(api_url)
data = response.json()["rates"]

# InfluxDB'ye veri yaz
for tarih, kurlar in data.items():
    rate = kurlar["TRY"]
    json_body = [
        {
            "measurement": "usd_try",
            "time": tarih + "T00:00:00Z",
            "fields": {
                "rate": float(rate)
            }
        }
    ]
    client.write_points(json_body)
    print(f"{tarih} tarihli USD/TRY kuru kaydedildi:", rate)
