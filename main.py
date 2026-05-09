import discord

# НОВЫЙ ТОКЕН
TOKEN = "MTMzMzM1MDY4NTQxMjAzNjYzOA.GFe5La.lEumT6Tl77F_rWD79hJNF_3dTrosE5O8N-74s0"

print("✅ Запуск бота...")
print(f"✅ Токен загружен, длина: {len(TOKEN)}")

class Bot(discord.Client):
    async def on_ready(self):
        print("=" * 50)
        print("✅ БОТ УСПЕШНО ЗАПУЩЕН!")
        print(f"✅ Имя: {self.user}")
        print(f"✅ ID: {self.user.id}")
        print("=" * 50)

bot = Bot(intents=discord.Intents.all())
bot.run(TOKEN)
