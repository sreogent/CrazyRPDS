import discord

# НОВЫЙ ТОКЕН
TOKEN = "MTMzMz1MDY4NTQxMjAzNjYzOA.GpnmlU1vsVOujds293LuDF-BB548wHYGqf06UDAwWGO-U"

print("🚀 Запуск бота...")
print(f"✅ Токен загружен, длина: {len(TOKEN)}")

class Bot(discord.Client):
    async def on_ready(self):
        print("=" * 50)
        print(f"✅✅✅ БОТ УСПЕШНО ЗАПУЩЕН! ✅✅✅")
        print(f"📌 Имя: {self.user}")
        print(f"📌 ID: {self.user.id}")
        print("=" * 50)

bot = Bot(intents=discord.Intents.all())
bot.run(TOKEN)
