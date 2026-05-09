import discord

# СВЕЖИЙ ТОКЕН
TOKEN = "MTMzMz1MDY4NTQxMjAzNjYzOA.GloWis.T1SK_SOJzV77-DjDPniAkKK7-uTqMDsQZhyh_k"

print("🚀 ЗАПУСК НОВОГО БОТА...")

class NewBot(discord.Client):
    async def on_ready(self):
        print(f"✅✅✅ БОТ УСПЕШНО ЗАПУЩЕН! ✅✅✅")
        print(f"📌 Имя бота: {self.user}")
        print(f"📌 ID бота: {self.user.id}")
        print(f"📌 На серверах: {len(self.guilds)}")
        
        # Показываем статус
        await self.change_presence(activity=discord.Game(name="Готов к работе!"))
        
        print("🎉 Бот полностью функционален!")

print("Подключение к Discord...")
bot = NewBot(intents=discord.Intents.all())
bot.run(TOKEN)
