import discord
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv('BMTMzMzM1MDY4NTQxMjAzNjYzOA.GFe5La.lEumT6Tl77F_rWD79hJNF_3dTrosE5O8N-74s0')

print("✅ Запуск бота...")
print(f"✅ Токен {'найден' if TOKEN else 'НЕ НАЙДЕН'}")

class Bot(discord.Client):
    async def on_ready(self):
        print("=" * 50)
        print("✅ БОТ УСПЕШНО ЗАПУЩЕН!")
        print(f"✅ Имя: {self.user}")
        print(f"✅ ID: {self.user.id}")
        print("=" * 50)

if not TOKEN:
    print("❌ ОШИБКА: Токен не найден! Добавьте BOT_TOKEN в переменные окружения")
else:
    bot = Bot(intents=discord.Intents.all())
    bot.run(TOKEN)
