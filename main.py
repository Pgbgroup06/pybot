from pyrogram import Client,filters


bot = Client(
  "Pgbgroup Bot",
  api_id=9914709,
  api_hash ="b3e7cb5ef23aaa7eb618a63d62405e1d",
  bot_token ="5313087885:AAE8HWHhfy-bT7vznBcpUFsIrrlw3eMBvpQ"
)

@bot.on_message(filters.command('start') & filters.private)
def startmsg(bot,message):
  bot.send_message(message.chat.id,"Hi I Am Online")


@bot.on_message(filters.command('info') & filters.private)
def infomsg(bot,message):
  bot.send_message(message.chat.id,"Made By Pgbgroup")

@bot.on_message(filters.text & filters.private)
def unknowmsg(client,message):
  message.reply_text("Unknown Command")

 
@bot.on_message(filters.chat("testrjrjpgb") & filters.new_chat_members)
def newmembermsg(client,message):
  message.reply_text("Welcome To Group!")

  
print("Running")
bot.run()
