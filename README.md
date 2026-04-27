# 💰 Smart Expense & Notification Management System

Kullanıcıların finansal harcamalarını takip eden, bütçe analizi yapan ve limit aşımlarında otonom bildirimler gönderen uçtan uca bir yönetim sistemi simülasyonudur.

## 📌 İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Özellikler](#özellikler)
- [Teknolojiler](#teknolojiler)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [İletişim](#iletişim)

---

## 📖 Proje Hakkında
Bu proje, modern yazılım prensiplerini (özellikle OOP ve modüler mimari) finansal bir senaryo üzerinde uygulamak amacıyla geliştirilmiştir. Ham verinin işlenmesinden, analizine ve kullanıcıya uygun kanallar (Email/SMS) üzerinden geri bildirim verilmesine kadar olan tüm süreci yönetir.

---

## ✨ Özellikler
- ✔️ **Otonom Bütçe Takibi:** Harcamaların bütçe limitine göre anlık kontrolü.
- ✔️ **Gelişmiş Analiz:** Toplam, ortalama ve ekstrem harcama istatistikleri.
- ✔️ **Akıllı Bildirimler:** Limit aşımı durumunda polimorfik yapıya sahip bildirim gönderimi.
- ✔️ **Hata Yönetimi:** Geçersiz veri girişlerine karşı dayanıklı sistem mimarisi.

---

## 📂 Proje Yapısı

Proje dosyaları mantıksal modüllere ayrılmış şekilde ana klasör altında toplanmıştır:

```text
smart_expense_notification_management_system/
├── models.py           # Veri modelleri (Expense ve Budget sınıfları)
├── notifications.py    # Bildirim mantığı (Kalıtım ve Çok Biçimlilik)
├── utils.py            # Yardımcı fonksiyonlar (Kayıt ve Rastgele üretim)
├── main.ipynb          # Uygulamanın ana yürütme ve test dosyası
└── smart_expense_notification_management_system.md  # Teknik Rapor
```
## 🚀 Kurulum
Repoyu bilgisayarınıza klonlayın:
```bash
git clone [https://github.com/isilbilasa/Smart-Expense-Notification-Management-System.git](https://github.com/isilbilasa/Smart-Expense-Notification-Management-System.git)
```
2.Proje dizinine gidin:
```bash
cd Smart-Expense-Notification-Management-System/smart_expense_notification_management_system
```
3. Gerekli Ortamı Hazırlayın:

Bilgisayarınızda Python 3.x kurulu olduğundan emin olun.

Jupyter Notebook veya VS Code (Jupyter eklentisi ile) kullanmanız önerilir.

4. Çalıştırın:

main.ipynb dosyasını açın ve tüm hücreleri sırasıyla çalıştırın.

## 💻 Kullanım
Sistemi başlattığınızda:

Amount (Tutar) ve Category (Kategori) bilgilerini girin.

Girişi bitirmek için tutar kısmına 0 yazın.

Sistem otomatik olarak bütçe analizinizi yapacak ve limit aşımı varsa rastgele bir kanal (Email veya SMS) üzerinden size bildirim simülasyonu gönderecektir.

## 📧 İletişim
Geliştirici: Işıl Bilasa
