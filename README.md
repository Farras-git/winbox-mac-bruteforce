# winbox-mac-bruteforce
tools bruteforce yang menargetkan mac-address dari perangkat mikrotik untuk menemukan passwordnya

# 🔐 Winbox MAC Brute Force Tool

Tool ini digunakan untuk melakukan brute force login ke perangkat Mikrotik via Winbox menggunakan MAC address (bukan IP based). Tool memanfaatkan **PyAutoGUI** untuk mengontrol GUI Winbox dan mencoba daftar password satu per satu secara otomatis.

---

## 🛠️ Fitur
- ✅ Brute force via MAC address (bukan IP)
- ✅ Simulasi otomatis klik & ketik di Winbox menggunakan PyAutoGUI
- ✅ Akan masuk kedalam halaman winbox jika 'berhasil'

---

## 📌 Disclaimer

⚠️ Tool ini hanya dibuat untuk pembelajaran & penelitian **etikal**.  
⚠️ Jangan digunakan untuk menyerang sistem yang tidak kamu miliki izin aksesnya.  
⚠️ Segala bentuk penyalahgunaan bukan tanggung jawab pembuat.

---

## 💻 Persyaratan

- OS: Windows
- Python: versi 3.10 atau lebih tinggi
- Winbox versi desktop (buka secara manual)
- Perangkat Mikrotik asli yang bisa diakses via MAC address

---

## 🚀 Instalasi

### 1. Install Python

- Download dari [python.org](https://www.python.org/downloads/)
- Saat instalasi, centang ✅ **Add Python to PATH**
- Verifikasi via CMD:
  ```bash
  python --version
