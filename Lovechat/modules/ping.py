

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from Lovechat import Lovechat
from Lovechat.database.chats import add_served_chat
from Lovechat.database.users import add_served_user
from Lovechat.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://telegra.ph/file/c1273112d4bddd5f03b7b.jpg",
    "https://telegra.ph/file/c3ebd7f45b134092c975f.jpg",
    "https://telegra.ph/file/025e1073360b2eca8d054.jpg",
    "https://telegra.ph/file/19832f573094d09e46762.jpg",
    "https://telegra.ph/file/34d48ef1809fee8dd7475.jpg",
    "https://telegra.ph/file/71595feefce7fa31a05cc.jpg",
    "https://telegra.ph/file/0fcdf35ab5d54f16b1ca3.jpg",
    "https://telegra.ph/file/a52eff52b371bd280340c.jpg",
    "https://telegra.ph/file/d37bf7c86a9dfb15cb882.jpg",
    "https://telegra.ph/file/278774082fce47d172c69.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@Lovechat.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{Lovechat.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [MRChiku❣️](https://t.me/{OWNER_USERNAME}) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
