import discord
from discord.ext import commands
import random
import asyncio
import re
import os
import os

bot.run(os.environ.get("TOKEN"))


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=['!', '/'], intents=intents)

voice_clients = {}

def get_response(text):
    text = text.lower().strip()
    
    insults = ["เหี้ย", "ควาย", "ส้นตีน", "ชาติหมา", "ไอ้ส้น", "ไอ้เหี้ย", "กาก", "โง่", "บ้า", "ห่วย", "กระจอก", "ไร้ค่า", "สัส", "สัตว์"]
    
    for insult in insults:
        if insult in text:
            return random.choice([
                "หุบปากมึง!", "อย่าด่ากู!", "ด่ากูทำไมวะ", "เหี้ยไรวะ", "กากเอง", "มึงนั่นแหละกาก", "หุบ!", "ไม่แคร์", "ช่างแม่ง", "555"
            ])
    
    if any(w in text for w in ["หวัดดี", "สวัสดี", "เฮ้ย", "ไง", "ว่าไง", "ว๊อย", "โว้ย"]):
        return random.choice(["👋", "ไง!", "หวัดดีจ้า", "ว่าาาา", "ว๊อยยย", "เฮ้ย!"])
    
    if any(w in text for w in ["สบายดี", "เป็นไง", "เป็นยังไง", "ไงมึง"]):
        return random.choice(["สบายดี", "ก็ดีนะ", "แฮปปี้", "โคตรดี", "ปกติ", "ชิลๆ"])
    
    if any(w in text for w in ["ทำไร", "ทำอะไร", "ทำไรอยู่", "ทำอะไรอยู่"]):
        return random.choice(["นั่งเล่น", "ไม่รู้ดิ", "เฉยๆ", "รออะไรอยู่วะ", "ไม่ทำไร", "ดูมึงเล่น"])
    
    if any(w in text for w in ["ไปไหน", "จะไปไหน", "ไปไหนมา"]):
        return random.choice(["อยู่บ้าน", "ข้างนอก", "ไม่บอก", "ก็ตรงนี้ไง", "มึงไปไหนล่ะ"])
    
    if any(w in text for w in ["เกลียด", "ไม่ชอบ", "แย่"]):
        return random.choice(["เกลียดเลยว่ะ", "ไม่ชอบ", "แย่มาก", "กูก็เกลียด", "ช่างมัน"])
    
    if any(w in text for w in ["ชอบ", "ดี", "เยี่ยม"]):
        return random.choice(["ชอบๆ", "ก็ดีนะ", "โครตชอบ", "กูก็ชอบเหมือนกัน", "ดีจ้า"])
    
    if any(w in text for w in ["ขอบคุณ", "ขอบใจ", "thanks"]):
        return random.choice(["ด้วยความยินดี", "ไม่เป็นไร", "จ้าาา", "ยินดีครับ", "ยินดีจ้า"])
    
    if any(w in text for w in ["ขอโทษ", "sorry", "เสียใจ"]):
        return random.choice(["ไม่เป็นไร", "ช่างมัน", "ได้ๆ", "โอเค", "ไม่เป็นไรจ้า", "เศร้าาา"])
    
    if any(w in text for w in ["รัก", "love"]):
        return random.choice(["💖", "💕", "💗", "กูก็รักมึง", "💘", "🤍"])
    
    if any(w in text for w in ["หิว", "กิน", "ข้าว"]):
        return random.choice(["อร่อยๆ", "กินไรดี", "หิวๆ", "ข้าวก้นหม้อ", "🍜", "🍚"])
    
    if any(w in text for w in ["นอน", "หลับ", "ฝันดี"]):
        return random.choice(["ไปนอนเถอะ", "ฝันดี", "ราตรีสวัสดิ์", "นอนหลับฝันดี", "🌙"])
    
    if any(w in text for w in ["ทำงาน", "เรียน", "งาน", "การบ้าน"]):
        return random.choice(["สู้ๆ", "ตั้งใจนะ", "อย่าเครียด", "เก่งๆ", "💪", "📚"])
    
    if len(text) <= 3:
        return random.choice(["ห้ะ", "ว่า", "อ้าว", "เหรอ", "จิงดิ", "555"])
    
    generic = ["ห้ะ", "ว่าไง", "อ้าว", "เหรอ", "จิงดิ", "แล้วไง", "ช่างแม่ง", "กูไม่รู้", "มึงว่ายังไง", "อืมมม", "หึหึ", "อิอิ", "5555", "🤔", "😆", "🤣", "😎", "👍", "👀", "🙄", "😅", "💀", "🔥"]
    return random.choice(generic)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} ออนไลน์!")
    await bot.tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="/ช่วย หรือ !ช่วย"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    if message.content.strip() and not message.content.startswith(('!', '/')):
        await asyncio.sleep(random.uniform(0.3, 1))
        reply = get_response(message.content)
        await message.channel.send(reply)
    
    await bot.process_commands(message)

@bot.command()
async def เข้า(ctx):
    if not ctx.author.voice:
        await ctx.send("❌ มึงต้องอยู่ในช่องเสียงก่อน!")
        return
    
    channel = ctx.author.voice.channel
    try:
        vc = await channel.connect()
        voice_clients[ctx.guild.id] = vc
        await ctx.send(f"✅ เข้า {channel.name} แล้ว!")
    except Exception as e:
        await ctx.send(f"❌ เข้าไม่ได้: {e}")

@bot.command()
async def ออก(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        voice_clients.pop(ctx.guild.id, None)
        await ctx.send("👋 บาย!")
    else:
        await ctx.send("❌ กูไม่ได้อยู่ในช่องเสียง")

@bot.command()
async def พูด(ctx, *, text):
    if not ctx.voice_client:
        await ctx.send("❌ กูต้องอยู่ในช่องเสียงก่อน! ใช้ !เข้า หรือ /เข้า")
        return
    
    bad_words = ["เหี้ย", "ควาย", "ส้นตีน", "ชาติหมา", "ไอ้ส้น", "ไอ้เหี้ย", "กาก", "โง่", "บ้า"]
    for bw in bad_words:
        if bw in text.lower():
            text = f"มึงพูด {bw} มา เหี้ยไรวะ"
            break
    
    await ctx.send(text, tts=True)

@bot.command()
async def ด่า(ctx, user: discord.Member, *, reason=None):
    insults = [
        f"{user.mention} เหี้ยไรวะ",
        f"{user.mention} กาก",
        f"{user.mention} ควาย",
        f"ไอ้{user.display_name} ส้นตีน",
        f"{user.mention} อย่ามาหน้าโง่เลย",
        f"{user.mention} หุบปาก",
        f"มึง {user.display_name} น่ะเหี้ย",
    ]
    await ctx.send(random.choice(insults))

@bot.command()
async def ชม(ctx, user: discord.Member, *, reason=None):
    compliments = [
        f"{user.mention} เก่งมาก",
        f"{user.mention} เท่มาก",
        f"{user.mention} น่ารักจัง",
        f"{user.mention} โคตรเท่",
    ]
    await ctx.send(random.choice(compliments))

@bot.command()
async def เต๋า(ctx, sides: int = 6):
    result = random.randint(1, sides)
    await ctx.send(f"🎲 ทอยได้ {result} / {sides}!")

@bot.command()
async def ทาย(ctx, *, question):
    answers = ["ใช่", "ไม่", "อาจจะ", "ไม่แน่นอน", "ชัวร์!", "กูว่าไม่"]
    await ctx.send(f"🎱 {random.choice(answers)}")

@bot.command()
async def บอท(ctx, *, text=None):
    if text:
        await ctx.send(get_response(text))
    else:
        await ctx.send("ว่าไง")

@bot.command()
async def อยู่(ctx):
    await ctx.send(f"กูอยู่! {round(bot.latency * 1000)}ms")

@bot.command()
async def ช่วย(ctx):
    embed = discord.Embed(title="📚 คำสั่งบอท (ใช้ ! หรือ /)", color=0x00AAFF)
    embed.add_field(name="🗣️ Voice", value="!เข้า, /เข้า\n!ออก, /ออก\n!พูด <ข้อความ>, /พูด <ข้อความ>", inline=False)
    embed.add_field(name="💬 คำสั่งสนุก", value="!ด่า @คน, /ด่า @คน\n!ชม @คน, /ชม @คน\n!เต๋า, /เต๋า\n!ทาย <คำถาม>, /ทาย <คำถาม>", inline=False)
    embed.add_field(name="📌 ทั่วไป", value="!บอท <ข้อความ>, /บอท <ข้อความ>\n!อยู่, /อยู่\n!ช่วย, /ช่วย", inline=False)
    embed.add_field(name="🎯 พิมพ์อะไรก็ได้", value="บอทตอบเองอัตโนมัติ (ยกเว้นขึ้นต้นด้วย ! หรือ /)", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
