# TEKNİK RAPOR: Smart Expense & Notification Management System

## 1. Projenin Amacı ve Mimari Yapısı
Bu proje, bir kullanıcının finansal verilerini otonom bir şekilde yöneten uçtan uca bir sistem simülasyonudur. Projenin temel amacı, ham verinin işlenmesinden analizine ve gerekli durumlarda kullanıcıya otomatik bildirim gönderilmesine kadar olan tüm süreci profesyonel yazılım prensipleriyle kurgulamaktır.

Sistem, modern yazılım dünyasında **"Sorumlulukların Ayrılması" (Separation of Concerns)** olarak bilinen modüler mimari ile inşa edilmiştir:

* **models.py:** Veri yapılarını ve iş mantığını (Harcama ve Bütçe sınıfları) yönetir.
* **notifications.py:** Bildirim kanallarını OOP prensipleriyle simüle eder.
* **utils.py:** Kullanıcı etkileşimi, veri girişi ve yardımcı fonksiyonları içerir.

---

## 2. Nesne Yönelimli Programlama (OOP) Prensiplerinin Uygulanması
Projede OOP'nin tüm temel direkleri stratejik olarak kullanılmıştır:

* **Kalıtım (Inheritance):** Email ve SMS bildirim sınıfları, temel `Notification` sınıfından türetilmiştir. Bu sayede mesaj yönetimi merkezi bir noktadan kontrol edilir.
* **Çok Biçimlilik (Polymorphism):** Farklı bildirim kanallarının her biri `send()` metoduna sahiptir. Ancak her kanal (Email veya SMS), bu metoda kendi işleyişine uygun farklı tepkiler verir.
* **Özel Metotlar (Dunder Methods):** `__str__` metodu kullanılarak harcama nesneleri ekrana basıldığında anlamlı ve okunabilir bir finansal özet sunulması sağlanmıştır.

---

## 3. Veri Güvenliği ve Hata Yönetimi (Robustness)
Finansal verilerde hata payı kabul edilemez. Bu nedenle sistemde gelişmiş hata yakalama mekanizmaları kullanılmıştır:

* **Try-Except Blokları:** Kullanıcının harcama tutarı yerine harf girmesi veya boş değer bırakması gibi durumlarda sistem çökmez; hatayı yakalayarak kullanıcıyı doğru veri girişine yönlendirir.
* **Kapsam (Scope) Kontrolü:** Değişkenlerin yerel ve küresel sınırları net çizilerek, fonksiyonlar arası veri sızıntısı ve hatalı üzerine yazma durumları engellenmiştir.

---

## 4. Teknik Analiz ve Hesaplama Mantığı
Sistem, Python'ın yerleşik fonksiyonlarını kullanarak yüksek performanslı bir analiz sunar:

* **Dinamik Parametreler (*args):** Bildirim kayıt fonksiyonlarında kullanılan `*args` yapısı, sisteme sınırsız sayıda bildirim nesnesi gönderilmesine olanak tanıyarak esnekliği artırır.
* **İstatistiksel Veri İşleme:** `sum()`, `len()`, `max()` ve `min()` fonksiyonları ile bütçe analizi (toplam, ortalama, limit aşımı kontrolü) otonom olarak gerçekleştirilir.

---

## Sonuç
Bu çalışma, yazılım geliştirme sürecinin sadece kod yazmaktan ibaret olmadığını; sistem tasarımı, hata yönetimi ve sürdürülebilir mimari kurmanın önemini kanıtlamaktadır. Proje, gelecekte yeni bildirim kanalları (WhatsApp, Slack vb.) veya yeni finansal modeller eklenebilmesine imkan tanıyan esnek ve profesyonel bir altyapıya sahiptir.