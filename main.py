import discord , time, pyautogui , keyboard , os
from discord.ext import commands

buttons = ["w","s","a","d"]
buttons2 = ["w","s","a","d","j"]

class gamefucker(commands.Bot):

    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=commands.when_mentioned_or("l"), intents=intents)

    async def on_ready(self):
        await bot.change_presence(status=discord.Status.dnd, activity=discord.Game("games fucked"))

    async def on_message(self , message):
        if message.content == "g":
           pyautogui.press("g")

        if message.content == "uc":
            pyautogui.press("space")
        
        if message.content == "1":
           pyautogui.press("1")
        
        if message.content == "2":
           pyautogui.press("2")
        
        if message.content == "3":
           pyautogui.press("3")
        
        if message.content == "4":
           pyautogui.press("4")

        if message.content == "ctrl":
            keyboard.press("v")

        if message.content == "shift":
            keyboard.press("shift")

        if message.content == "w":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("w")

        if message.content == "a":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("a")

        if message.content == "s":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("s")

        if message.content == "d":
            for key in buttons:
                keyboard.release(key)
            keyboard.press("d")
        
        if message.content == "e":
            keyboard.release("e")
            keyboard.press("e")

        if message.content == "q":
            keyboard.release("q")
            keyboard.press("q")
        
        if message.content == "x":
            keyboard.release("x")
            keyboard.press("x")
        
        if message.content == "c":
            keyboard.release("c")
            keyboard.press("c")

        if message.content == "spray":
            keyboard.release("j")
            keyboard.press("j")
        
        if message.content == "ot":
            keyboard.press("j")
            keyboard.release("j")

        if message.content == "res":
            for key in buttons2:
                keyboard.release(key)


        await bot.process_commands(message)

    async def on_ready(self):
        print(f"{bot.user.name}")
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                try:
                    await bot.load_extension(f'commands.{filename[:-3]}')
                    print(f'{filename} başarıyla yüklendi.')
                except Exception as e:
                    print(e)

bot = gamefucker()




bot.run('urdiscordbottoken')