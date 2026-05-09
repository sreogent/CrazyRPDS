import discord

# ВСТАВЬТЕ ТОКЕН ВРУЧНУЮ (НОВЫЙ, ПОСЛЕ СБРОСА)
TOKEN = "MTMzMzM1MDY4NTQxMjAzNjYzOA.GloWis.T1SK_S0JzV77-DjDPniAkKK7-uTqMDsQZhhv_k"

print("1. Начинаем подключение...")
print(f"2. Длина токена: {len(TOKEN)}")

class TestClient(discord.Client):
    async def on_ready(self):
        print(f"3. ✅✅✅ БОТ ЗАПУЩЕН: {self.user}")
        print(f"4. На серверах: {len(self.guilds)}")
        await self.close()

client = TestClient(intents=discord.Intents.default())
client.run(TOKEN)
