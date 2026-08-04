# ==========================================================
# Discord Slash Bot (discord.py 최신 버전)
# 파일명: bot.py
#
# 필요한 라이브러리 설치:
# pip install -U discord.py
# ==========================================================

import os
import discord
from discord import app_commands
from discord.ext import commands

# ==========================================================
# Render 환경 변수에서 TOKEN 가져오기
# ==========================================================
TOKEN = os.getenv("TOKEN")

# ==========================================================
# Intents 설정
# ==========================================================
intents = discord.Intents.default()

# ==========================================================
# Bot 생성
# ==========================================================
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# ==========================================================
# 봇 실행 완료
# ==========================================================
@bot.event
async def on_ready():
    print("=" * 40)
    print(f"로그인 완료 : {bot.user}")
    print(f"Bot ID : {bot.user.id}")
    print("=" * 40)

    try:
        synced = await bot.tree.sync()

        print(f"슬래시 명령어 동기화 완료 ({len(synced)}개)")
        for cmd in synced:
            print(f" - /{cmd.name}")

    except Exception as e:
        print("명령어 동기화 실패")
        print(e)

# ==========================================================
# /리엘
# ==========================================================
@bot.tree.command(
    name="리엘",
    description="리엘을 불러옵니다."
)
async def riel(interaction: discord.Interaction):
    await interaction.response.send_message("난 냥이다.")

# ==========================================================
# 실행
# ==========================================================
if TOKEN is None:
    print("오류: Render 환경 변수 TOKEN이 설정되지 않았습니다.")
else:
    bot.run(TOKEN)