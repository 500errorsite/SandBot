# Man - UserBot
# Copyright (c) 2022 SandBot
# Credits: @mrismanaziz || https://github.com/500errorsite
#
# This file is a part of < https://github.com/500errorsite/SandBot/ >
# t.me/SharingUserbot & t.me/Lunatic0de

from telethon.tl.functions.channels import InviteToChannelRequest

from userbot import BOT_USERNAME
from userbot import BOT_VER as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import MAN2, MAN3, MAN4, MAN5, bot, branch, owner, uid

mention = f"[{owner}](tg://user?id={uid})"
MSG_ON = """
🔥 **SandBot Berhasil Di Aktifkan**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Ketik** `{}alive` **untuk Mengecheck Bot**
➠ **Managed By** {}
━━
"""


async def man_userbot_on():
    try:
        if bot:
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    f"🔥 **SandBot Berhasil Di Aktifkan**\n━━\n➠ **Userbot Version -** `{version}@{branch}`\n➠ **Ketik** `{cmd}alive` **untuk Mengecheck Bot**\n━━",
                )
    except Exception:
        pass
    try:
        if MAN2:
            if BOTLOG_CHATID != 0:
                await MAN2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except Exception:
        pass
    try:
        if MAN3:
            if BOTLOG_CHATID != 0:
                await MAN3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except Exception:
        pass
    try:
        if MAN4:
            if BOTLOG_CHATID != 0:
                await MAN4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except Exception:
        pass
    try:
        if MAN5:
            if BOTLOG_CHATID != 0:
                await MAN5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd, mention),
                )
    except Exception:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass
