import tkinter

window = tkinter.Tk()
window.minsize(width=300,height=300)
window.title("BKI Hesaplama")

kilo_label = tkinter.Label(text="Lütfen Kilonuzu Giriniz (kg)")
kilo_label.pack()

kilo_entry = tkinter.Entry()
kilo_entry.pack()

boy_label = tkinter.Label(text="Lütfen Boyunuzu Giriniz (cm)")
boy_label.pack()

boy_entry = tkinter.Entry()
boy_entry.pack()

def hesap():
    kilo = kilo_entry.get()
    boy = boy_entry.get()

    if boy == "" or kilo == "":
        sonuc_label.config(text="Lütfen Değer Giriniz")
    else :
        try:
            hesapsonuc = float(kilo) / (float(boy) / 100) ** 2
            sonuc_label.config(text=f"Beden Kitle Endeksiniz : {hesapsonuc}")
            sonuc_yazdır(hesapsonuc)
        except:
            sonuc_label.config(text="Değer Girmediniz")

sonuc_buton = tkinter.Button(text="Hesapla",command=hesap)
sonuc_buton.pack()

sonuc_label = tkinter.Label()
sonuc_label.pack()

def sonuc_yazdır(hesapsonuc):
    if hesapsonuc >= 30:
        sonuc_label.config(text=f"Beden Kitle Endeksiniz: {round(hesapsonuc,2)}, Obezsiniz.")
    elif hesapsonuc < 30 and hesapsonuc >= 25:
        sonuc_label.config(text=f"Beden Kitle Endeksiniz: {round(hesapsonuc,2)}, Kilolusunuz.")
    elif hesapsonuc < 25 and hesapsonuc >= 20:
        sonuc_label.config(text=f"Beden Kitle Endeksiniz: {round(hesapsonuc,2)}, Normalsiniz.")
    else:
        sonuc_label.config(text=f"Beden Kitle Endeksiniz: {round(hesapsonuc,2)}, Zayıfsınız.")


window.mainloop()