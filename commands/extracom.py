import pyautogui
from discord.ext import commands

class Extracomm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def chat(self , ctx , text):
        pyautogui.press("enter")
        pyautogui.typewrite(text)
        pyautogui.press("enter")

async def setup(bot):
    await bot.add_cog(Extracomm(bot))