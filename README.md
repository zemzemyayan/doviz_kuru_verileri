# USD/TRY Döviz Kuru İzleme ve Depolama Projesi

Bu proje, Frankfurter API’den günlük USD/TRY döviz kuru verilerini çekip, zaman serisi veritabanı **InfluxDB**’ye kaydeden bir Python uygulamasıdır. Veriler Docker ortamında çalışan InfluxDB ve Grafana ile kolayca görselleştirilebilir.

---

## İçindekiler
- [Genel Bakış](#genel-bakış)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
- [Projede Neler Yapıldı?](#projede-neler-yapıldı)
- [Veri Görselleştirme](#veri-görselleştirme)
- [İletişim](#iletişim)

---

## Genel Bakış

Bu proje, belirlenen başlangıç tarihinden bugüne kadar USD/TRY döviz kuru verilerini Frankfurter API üzerinden çeker ve bu verileri InfluxDB zaman serisi veritabanında saklar. Veritabanındaki veriler, Grafana ile kolayca izlenip analiz edilebilir.

---

## Kullanılan Teknolojiler

- **Python**: API’den veri çekme ve InfluxDB’ye veri yazma işlemleri için.
- **InfluxDB 1.8**: Zaman serisi veritabanı.
- **Docker**: InfluxDB ve Grafana’yı konteyner olarak çalıştırmak için.
- **Grafana**: Verilerin görselleştirilmesi için.
- **Frankfurter API**: Döviz kuru verilerini sağlayan ücretsiz API.

---

## Kurulum ve Çalıştırma

1. Docker’da InfluxDB ve Grafana konteynerlerini çalıştırın:

```bash
docker run -d --name influxdb -p 8086:8086 influxdb:1.8
docker run -d --name grafana -p 3000:3000 grafana/grafana
