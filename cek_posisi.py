import pyautogui
import time

print("Pindahkan kursor ke kolom password dalam 5 detik...")
time.sleep(5)
print("Posisi password box:", pyautogui.position())

print("Pindahkan kursor ke tombol login dalam 5 detik...")
time.sleep(5)
print("Posisi tombol login:", pyautogui.position())
