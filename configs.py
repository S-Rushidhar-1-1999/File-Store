# (c) @PredatorHackerzZ || @TeleRoidGroup

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID", ""))
	API_HASH = os.environ.get("API_HASH", "")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
	BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
	DATABASE_URL = os.environ.get("DATABASE_URL", "")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "")
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", False))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File.I can Work In Channel too Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

â­ââ[ **ð FÉªÊá´Sá´á´Êá´Bá´á´ ð ** ]âââ
â
âð¸ð¤ **My Name: [FÉªÊá´ Sá´á´Êá´ Bá´á´](https://telegram.me/{BOT_USERNAME}) **
â
âð¸ð **Language: [PÊá´Êá´É´](https://www.python.org) **
â
âð¹ð **Library: [PÊÊá´É¢Êá´á´](https://docs.pyrogram.org) **
â
âð¹ð¡ **Hosted On: [Má´É¢á´É´Éªá´s](https://mogenius.com/) **
â
âð¸ð¨âð» **Developer: [Rá´sÊÉªá´Êá´Ê](https://telegram.me/rushidhar1999) **
â
â°ââ[** ð ð [ Rá´sÊÉªá´Êá´Ê ] ð ð **]âââ
"""
	ABOUT_DEV_TEXT = f"""
ð§ð»âð» **ðð²ðð²ð¹ð¼ð½ð²ð¿: [Rá´sÊÉªá´Êá´Ê](https://telegram.me/rushidhar1999) **  

ððð¯ðð¥ð¨ð©ðð« ð¢ð¬ ðð®ð©ðð« ðð¨ð¨ð. ðð®ð¬ð­ ðððð«ð§ð¢ð§ð  ðð«ð¨ð¦ ðððð¢ðð¢ðð¥ ðð¨ðð¬. ðð§ð ðððð¤ð¢ð§ð  ððð¥ð© ðð«ð¨ð¦ ðð«ð¨ ðð¨ððð«ð¬\n** [Rá´sÊÉªá´Êá´Ê](https://telegram.me/rushidhar1999) **

ðð ðð¨ð® ð°ðð§ð­ ð­ð¨ ðð¨ð§ðð­ð ðð®ð« ððð«ð ðð¨ð«ð¤. ðð¨ð® ððð§ ðð¨ð§ð­ððð­ ðð¡ð ððð¯ðð¥ð¨ð©ðð«. 

ðð¥ð¬ð¨ ð«ðð¦ðð¦ððð« ð­ð¡ðð­ ððð¯ðð¥ð¨ð©ðð« ð°ð¢ð¥ð¥ ððð¥ðð­ð ððð®ð¥ð­ ðð¨ð§ð­ðð§ð­ð¬ ðð«ð¨ð¦ ððð­ðððð¬ð. ðð¨ ððð­ð­ðð« ðð¨ð§'ð­ ðð­ð¨ð«ð ðð¡ð¨ð¬ð ðð¢ð§ð ð¨ð ðð¡ð¢ð§ð ð¬.
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FÉªÊá´ Sá´á´Êá´ Bá´á´**.

How to Use Bot & it's Benefits??

ð¢ Send me any File & It will be uploaded in My Database & You will Get the File Link.

â ï¸ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

â **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
