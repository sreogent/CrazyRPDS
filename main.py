import discord

# НОВЫЙ ТОКЕН
TOKEN = "MTMzMzM1MDY4NTQxMjAzNjYzOA.GpnmL1vsV0ujds293LuDF-BB548wHYGqf06UdaWGO-U"

print("✅ Запуск бота...")
print(f"✅ Токен загружен, длина: {len(TOKEN)}")

class Bot(discord.Client):
    async def on_ready(self):
        print("=" * 50)
        print("✅ БОТ УСПЕШНО ЗАПУЩЕН! ✅")
        print(f"✅ Имя: {self.user}")
        print(f"✅ ID: {self.user.id}")
        print("=" * 50)

bot = Bot(intents=discord.Intents.all())
bot.run(TOKEN)
