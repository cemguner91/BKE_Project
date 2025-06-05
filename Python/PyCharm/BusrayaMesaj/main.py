
import asyncio
from telegram import Bot
from telegram.constants import ParseMode
import random
import os

# Ortam degiskenlerinden cekiyoruz (Railway icin)
TOKEN = os.getenv("7804674720:AAEBJIDQb5WcWpy7GoPeb5-ovAHe_867xk0")
CHAT_ID = int(os.getenv("6122085074"))

# Mesaj listesi
messages = [
    "Gülüşün bir şiir gibi, her kelimesi huzur 🍃",
    "Seninle konuşmak içimi ısıtıyor, tıpkı güneş gibi ☀️",
    "Sen bu dünyaya biraz fazla güzelsin gibi geliyor bazen 💫",
    "Zekân, güzelliğinle yarışacak kadar parlıyor ✨",
    "Her mesajın günümün en iyi anı oluyor 💌",
    "Senin gibi biriyle aynı çağda yaşadığım için şanslı hissediyorum 🍀",
    "Sadece güzelliğin değil, kalbin de çok özel ❤️",
    "Bir gülüşünle tüm yorgunluğum gidiyor 😌",
    "Seninle her şey daha anlamlı, daha renkli 🎨",
    "İyi ki varsın. Her şeyinle. Gerçekten. 🌹",
    "Gözlerin galaksi gibi, kayboluyorum içinde 🌌",
    "Sesin huzurun tanımı gibi 🎵",
    "Varlığın yetiyor mutlu olmama 😇",
    "Senin yanında zaman geçmiyor, uçuyor 🕊️",
    "Düşüncelerine hayranım, konuşmaların hep özel 🧠",
    "İnsanın kalbini bu kadar ısıtan başka biri olamazdı 🔥",
    "Sen kahkahanla odanın havasını değiştiriyorsun 😄",
    "Çok güzelsin. Hem de her hâlinle. 🥰",
    "Sen yanımda olduğunda her şey yolunda gibi geliyor 🚀",
    "Seninle yaşlanmak bile eğlenceli olurdu 🙈",
    "Dünyanın en güzel sabahı senin 'günaydın' mesajın olurdu 🌅",
    "Aynaya her baktığında kendine gülümse; çünkü bir mucizeye bakıyorsun ✨",
    "Seninle konuşmak terapi gibi geliyor 💬",
    "Sen olmasan bile aklımdasın. Hep. 💭",
    "Senin gülümsemenle elektrik faturası düşerdi ⚡",
    "Bugün bile güzelliğinle kalbimi çaldın 💘",
    "Bir yıldız kaydı, dilek tutmadım; çünkü seni zaten buldum ⭐",
    "Çay, kahve, kitap güzel ama seninle başka güzel ☕📖❤️",
    "Sen bir ilham kaynağısın, sessizce etrafına ışık saçıyorsun 🕯️",
    "Düşünsene sen bir tablo olsan, Louvre seni kıskanırdı 🎨",
    "Yanımda olman huzurun tanımı gibi 🌿",
    "Sen sadece hayatıma değil, kalbime de renk kattın 🌈",
    "Gülüşünün sesi var sanki… ve o ses bağımlılık yapıyor 🎶",
    "Senin gözlerinde deniz var, dalıp dalıp kayboluyorum 🌊",
    "Sabah kahvesinden bile daha enerjik yapıyorsun beni ☕❤️",
    "Seni tanıdığımdan beri kötü geçen gün kalmadı 💫",
    "Senin gibi birini tanımak, hayatın bana hediyesi 🎁",
    "Seninle geçen her saniye bonus hayat gibi 🎮",
    "Her hâlini seviyorum, filtreye gerek yok 🥹",
    "Senin sevgine doyulmaz, ömür boyu isterim 💍",
    "Sana her baktığımda tekrar âşık oluyorum 💖",
    "Sen konuşunca dünya susuyor gibi hissediyorum 🌍",
    "Kalbin kadar güzel bir şey daha varsa, o da senin gözlerin 👀",
    "Sen gülünce içim açılıyor ☀️",
    "Yalnızca varlığın bile yetiyor mutlu olmama 😊",
    "Senin varlığın, hayatıma şiir yazdırıyor ✍️",
    "En sevdiğim şey, seni sevdiğimi bilmek 💘",
    "Seninle bir ömür, göz açıp kapayıncaya kadar geçer ⏳",
    "Seninle uyandığım her sabah en güzel günüm olurdu 🌄",
    "Senin gibi biri olmasaydı, hayat çok daha sıradan olurdu 😌",
    "Kalbimin en huzurlu köşesinde sen varsın 🩷",
    "Yalnızca seni düşünmek bile içimi ısıtıyor 🔥",
    "Sen benim en güzel alışkanlığımsın 🌷",
    "Seninle hayat çok daha renkli, çok daha güzel 🎨",
    "Seninle konuşmak, en güzel şarkıyı dinlemek gibi 🎼",
    "Senin enerjinle aydınlanıyor çevrem ☀️",
    "Gözlerinde kaybolmak istiyorum… çünkü onlar bir ev gibi sıcak 🏡",
    "Senin dokunuşun bile içimi rahatlatıyor 🌬️",
    "Birlikte olduğumuz her an, en değerli anım oluyor 💎",
    "Sana her gün iltifat etmek, bir görev değil; içimden gelen en güzel şey 🥹",
    "Sen gülerken zaman durmalı bence ⏱️",
    "Seninle geçen zaman, hayatın en tatlı hediyesi 🍭"
]

# Ana mesaj gönderme fonksiyonu
async def send_messages():
    bot = Bot(token=TOKEN)
    while True:
        msg = random.choice(messages)
        try:
            await bot.send_message(chat_id=CHAT_ID, text=msg, parse_mode=ParseMode.HTML)
            print("Gönderildi:", msg)
        except Exception as e:
            print("Hata:", e)
        await asyncio.sleep(60 * 30)  # 30 dakikada bir gönder

if __name__ == '__main__':
    asyncio.run(send_messages())
