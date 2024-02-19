from pyrogram.types import InlineKeyboardButton

from config import SUPPORT_GRP, UPDATE_CHNL
from Lovechat import OWNER
from Lovechat import Lovechat

DEV_OP = [
    [
        InlineKeyboardButton(text="😘𝙾𝚆𝙽𝙴𝚁😘", user_id=OWNER),
        InlineKeyboardButton(text="😘𝚂𝚄𝙿𝙿𝙾𝚁𝚃😘", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="✦ ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ ✦",
            url=f"https://t.me/{Lovechat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
       # InlineKeyboardButton(text="🫀 sᴏᴜʀᴄᴇ 🫀", callback_data="SOURCE"),
        InlineKeyboardButton(text="☁️ ᴀʙᴏᴜᴛ ☁️", callback_data="ABOUT"),
    ],
]

PNG_BTN = [
    [
        InlineKeyboardButton(
            text="😉𝗔𝗗𝗗 𝗠𝗘 𝗕𝗔𝗕𝗬😉",
            url=f"https://t.me/{Lovechat.username}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(
            text="愛 𝙲𝙻𝙾𝚂𝙴 愛",
            callback_data="CLOSE",
        ),
    ],
]


BACK = [
    [
        InlineKeyboardButton(text="愛 𝙱𝙰𝙲𝙺 愛", callback_data="BACK"),
    ],
]


HELP_BTN = [
    [
        InlineKeyboardButton(text="🦚 ᴄʜᴀᴛʙᴏᴛ 🦚", callback_data="CHATBOT_CMD"),
        InlineKeyboardButton(text="👻 ᴛᴏᴏʟs 👻", callback_data="TOOLS_DATA"),
    ],
    [
        InlineKeyboardButton(text="愛 𝙱𝙰𝙲𝙺 愛", callback_data="BACK"),
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


CLOSE_BTN = [
    [
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


CHATBOT_ON = [
    [
        InlineKeyboardButton(text="愛 𝙴𝙽𝙰𝙱𝙻𝙴 愛", callback_data=f"addchat"),
        InlineKeyboardButton(text="愛 𝙳𝙸𝚂𝙰𝙱𝙻𝙴 愛", callback_data=f"rmchat"),
    ],
]


MUSIC_BACK_BTN = [
    [
        InlineKeyboardButton(text="愛𝚂𝙾𝙾𝙽愛", callback_data=f"soom"),
    ],
]

S_BACK = [
    [
        InlineKeyboardButton(text="愛 𝙱𝙰𝙲𝙺 愛", callback_data="SBACK"),
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


CHATBOT_BACK = [
    [
        InlineKeyboardButton(text="愛 𝙱𝙰𝙲𝙺 愛", callback_data="CHATBOT_BACK"),
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


HELP_START = [
    [
        InlineKeyboardButton(text="愛 ʜᴇʟᴘ 愛", callback_data="HELP"),
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


HELP_BUTN = [
    [
        InlineKeyboardButton(
            text="« ʜᴇʟᴘ »", url=f"https://t.me/{Lovechat.username}?start=help"
        ),
        InlineKeyboardButton(text="愛 𝙲𝙻𝙾𝚂𝙴 愛", callback_data="CLOSE"),
    ],
]


ABOUT_BTN = [
    [
        InlineKeyboardButton(text="👻 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 👻", url=f"https://t.me/{SUPPORT_GRP}"),
        InlineKeyboardButton(text="« ʜᴇʟᴘ »", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="💀 𝙾𝚆𝙽𝙴𝚁 💀", user_id=OWNER),
     #   InlineKeyboardButton(text="🫀 sᴏᴜʀᴄᴇ 🫀", callback_data="SOURCE"),
    ],
    [
        InlineKeyboardButton(text="🐙 ᴜᴘᴅᴀᴛᴇs �", url=f"https://t.me/{UPDATE_CHNL}"),
        InlineKeyboardButton(text="愛 𝙱𝙰𝙲𝙺 愛", callback_data="BACK"),
    ],
]
