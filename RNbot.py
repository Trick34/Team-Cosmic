# (c) @Alone_loverBoy
# keep Credits 🤧 Kangers 


# <--imports--> #
import os
import html 

from telethon import TelegramClient
from telethon import events
from telethon import Button
from telethon.tl.functions.users import GetFullUserRequest 

# <-- Config -->
API_ID = int(os.environ.get("API_ID", 6))
API_HASH = os.environ.get("API_HASH", "")
TOKEN = os.environ.get("TOKEN", "")
FRWD_GP = os.environ.get("FRWD_GP", None) 
    if FRWD_GP is not None:
       try:
           FRWD_GP = int(FRWD_GP)
       except ValueError:
           raise ValueError( 
               "Invalid Group ID. Make sure your ID is starts with -100 and make sure that it is only numbers.")

ABT = """ 
🏆ᴀʙᴏᴜᴛ ᴛᴇᴀᴍ ᴄᴏsᴍɪᴄ🏆

🌀ᴛᴀɢ :- 『⍣Ƭ¢⍣』

🌀ʙᴇɴᴇғɪᴛs :-
✨24/7 sᴜᴘᴘᴏʀᴛ
✨ᴀʟᴡᴀʏs ʜᴇʟᴘs ɪɴ ʟᴇᴀʀɴɪɴɢ ɴᴇᴡ ᴛʜɪɴɢs
✨ʜᴇʟᴘs ɪɴ ɪᴍᴘʀᴏᴠɪɴɢ ᴋɴᴏᴡʟᴇᴅɢᴇ , ᴇᴛᴄ.

🌀ʀᴜʟᴇs :-
🎖️ᴍᴜsᴛ ᴀᴅᴅ ᴛᴀɢ ɪɴ ɴᴀᴍᴇ
🎖️ʀᴇsᴘᴇᴄᴛ ᴏᴛʜᴇʀs
🎖️ᴀʟᴡᴀʏs ʜᴇʟᴘ ᴏᴛʜᴇʀs

🌋ɴᴏᴛᴇ :- ᴅᴏɴ'ᴛ ʙᴇɢ ғᴏʀ ᴘʀᴏᴍᴏᴛɪᴏɴ ɪɴ ᴄᴏᴍᴍᴜɴɪᴛʏ
""" 

# <--Client--> 

bot = TelegramClient("loverboyXD", API_ID, API_HASH).start(bot_token=TOKEN)

#<--START_MESSAGE--> 

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):  
      sender = await event.get_sender()
      xx = sender.first_name
      await bot.send_message(event.chat_id, f"Hey!\n {xx} How are you?☺️\n\nᴛʜɪs ɪs ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴇɴᴛʀʏ ʙᴏᴛ ᴏғ ᴛᴇᴀᴍ ᴄᴏsᴍɪᴄ\
      \n🔹ɪɴ ᴛʜɪs ʙᴏᴛ ᴜ ᴄᴀɴ ᴀᴘᴘʟʏ ᴛᴏ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴜʀ ᴏᴘ sᴋɪʟʟs ᴊᴜsᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ🔹\n\n Choose Why are you Here by Having Clicks on Buttons Below :)", buttons=[
      [
            Button.inline("ᴀᴘᴘʟʏ ᴛᴏ ᴄᴏᴍᴍᴜɴɪᴛʏ", data="aply")
         ],
         [
            Button.inline("Cᴏɴᴀᴛᴄᴛ ᴜs", data="contact"),
            Button.inline("ᴀʙᴏᴜᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ", data="abt")
            ] 
            ]) 
# <-- CallBacks --> 

@bot.on(events.callbackquery.CallbackQuery(data="abt"))
async def abt(event):  
        await event.delete()
        await bot.send_message(event.chat_id, ABT)
  
@bot.on(events.callbackquery.CallbackQuery(data="aply"))
async def aply(event): 
      await event.delete()
      sender = await event.get_sender()
      first_name = sender.first_name 
      await bot.send_message(event.chat_id, f"ʜɪ {first_name} sᴏ ᴜʀ ʜᴇʀᴇ ᴛᴏ ᴀᴘᴘʟʏ ғᴏʀ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ\
      \nғᴏʀ ᴇɴᴛʀʏ ᴜ ʜᴀᴠᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴛʜᴀᴛ ᴛʜᴇ sᴋɪʟʟs ᴡʜᴀᴛ ᴜ ᴋɴᴏᴡ\
      \nғʀᴏᴍ ᴛʜᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴜ ᴡɪʟʟ ɢᴇᴛ ᴍᴀɴʏ sᴋɪʟʟs ɪɴ ᴛʜᴀᴛ ᴜ ʜᴀᴠᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴜʀ sᴋɪʟʟs ᴛʜᴀᴛ ᴜ ᴋɴᴏᴡ ᴠᴇʀʏ ᴡᴇʟʟ\
      \nɪɴ ʙᴇᴛᴡᴇᴇɴ ᴜ ᴡɪʟʟ ʙᴇ ᴛᴀᴋᴇɴ ᴀ sᴍᴀʟʟ ᴛᴇsᴛ ᴀɴᴅ ᴇɴᴛʀʏ ᴡɪʟʟ ʙᴇ ɢɪᴠᴇɴ\
      \n\n\nɴᴏᴛᴇ :- ⁱᶠ ᵃⁿʸ ᵒᶠ ᵗʰᵉ ᵇᵉˡᵒʷ ᵇᵘᵗᵗᵒⁿˢ ᵈⁱᵈⁿ'ᵗ ʷᵒʳᵏ ᵘ ᶜᵃⁿ ˢᵃʸ ᵃᵇᵒᵘᵗ ⁱᵗ ⁱⁿ ᵒᵘʳ ˢᵘᵖᵖᵒʳᵗ", buttons=[
      [
        Button.inline("Logo making", data="log"),
        Button.inline('Binning', data="bin")
        ],
        [
          Button.inline("Bintester", data="bints"),
          Button.inline("Cracker", data="ckr")
        ],
        [
          Button.inline("Developer", data="dev")
        ],
        [
          Button.inline("Cc/Combo Maker", data="ccmake"),
          Button.inline("Cc Spammer", data="ccspamr")
        ],
        [
        Button.inline("Docker", data="dokr")
        ],
        [
          Button.inline("Back🧑‍🦯", data="menu")]
        ])
        
    
# <-- Contact --> 
@bot.on(events.callbackquery.CallbackQuery(data="contact"))
async def contact(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"Hey [{first_name}](tg://user?id={xx}) can Our Community Moderators at\nHERE==>[CONTACT US](https://t.me/TC_ENTRY)<==", buttons=[
           Button.inline("Back🧑‍🦯", data="menu")])

# <-- Back Button -->
@bot.on(events.callbackquery.CallbackQuery(data="menu"))
async def menu(back):
        await back.delete()
        await bot.send_message(back.chat_id, "ᴛʜɪs ɪs ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴇɴᴛʀʏ ʙᴏᴛ ᴏғ ᴛᴇᴀᴍ ᴄᴏsᴍɪᴄ\
        \n🔹ɪɴ ᴛʜɪs ʙᴏᴛ ᴜ ᴄᴀɴ ᴀᴘᴘʟʏ ᴛᴏ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ ᴡɪᴛʜ ᴜʀ ᴏᴘ sᴋɪʟʟs ᴊᴜsᴛ ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ🔹\n\n Choose Why are you Here by Having Clicks on Buttons Below :)", buttons=[
        [
            Button.inline("ᴀᴘᴘʟʏ ᴛᴏ ᴄᴏᴍᴍᴜɴɪᴛʏ", data="aply")
            ],
            [
            Button.inline("Cᴏɴᴀᴛᴄᴛ ᴜs", data="contact"),
            Button.inline("ᴀʙᴏᴜᴛ ᴏᴜʀ ᴄᴏᴍᴍᴜɴɪᴛʏ", data="abt")
            ]])
            
 # <-- Skills CallBack -->
@bot.on(events.callbackquery.CallbackQuery(data="log"))
async def log(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Logo Making` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) **For Test**")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Logo Making` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx})'s Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data="bin"))
async def bin(event): 
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Binning` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) For Test**.")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Binning` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data="bints"))
async def bints(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Bin tester` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) **For Test**")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Bin Tester` Skill\n\nPlease Have Test of 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data="ckr"))
async def ckr(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Cracker` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) **For Test**")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Cracker` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)
            
@bot.on(events.callbackquery.CallbackQuery(data="dev"))
async def dev(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Developer` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) **For Test**")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Developer` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data="dokr"))
async def dokr(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `Docker` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) **For Test**")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `Docker` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)
        
@bot.on(events.callbackquery.CallbackQuery(data="ccmake"))
async def ccmake(event):
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `CC MAKER` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) For Test**.")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `CCMaker` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)

@bot.on(events.callbackquery.CallbackQuery(data="ccspmr"))
async def spmr(event):  
        sender = await event.get_sender()
        first_name = sender.first_name 
        xx = sender.id
        await event.edit(f"__Hey [{first_name}](tg://user?id={xx})  You Have Sucessfully__ applied for `CC Spammer` __for our Community!__\n\n**We need to check your Skills.! PLEASE Come to** [Skills Tester MODERATORS](https://t.me/TC_ENTRY) For Test**.")
        tosend = f"Hey MODERATORS [{first_name}](tg://user?id={xx}) Has Applied for `CC Spammer` Skill\n\nPlease Have Test of [{first_name}](tg://user?id={xx}) 's Skills!\n\nUSER INFO:\n•ID: {xx}\n•Name: {first_name}\n•Username: {sender.username}•\nProfile Link: [Link](tg://user?id={xx})"
        await bot.send_message(FRWD_GP, tosend)
        
    # <--User Message frwdr--> 
    
@bot.on(events.NewMessage(func=lambda e: e.is_private))
async def one_new_mssg(event):
    incoming = event.raw_text
    who = event.sender_id
    
    if incoming.startswith("/"):
        pass
    else:
        await event.get_sender()
        event.chat_id
        await event.forward_to(FRWD_GP)
# <-- Start-Up --> 
#     ↓↓↓↓↓↓
# To Start Bot😄 
bot.start() 
# To Run all Codes 
bot.run_until_disconnected()