import telebot
from telebot import types

TOKEN = "9224286005:AAFmzTt_E0Nv0nVVWwAAOSwgP1qhxhdmtKk"
CHANNEL = "@dababa_hacker"
CHANNEL_LINK = "https://t.me/dababa_hacker"

bot = telebot.TeleBot(TOKEN)

def check_sub(user_id):
    try:
        member = bot.get_chat_member(CHANNEL, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if check_sub(user_id):
        bot.send_message(message.chat.id, "👑 أهلاً بيك يا دبابة\nانت مشترك خلاص، نورتنا!")
    else:
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("📢 اشترك في القناة الاول", url=CHANNEL_LINK)
        btn2 = types.InlineKeyboardButton("✅ اتأكد اني اشتركت", callback_data="check")
        markup.add(btn1)
        markup.add(btn2)
        bot.send_message(message.chat.id, "👑 يا دبابة، عشان تستخدم البوت لازم تشترك في القناة الاول\n\nاشترك ودوس على زرار التأكيد 👇", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "check")
def check(call):
    user_id = call.from_user.id
    if check_sub(user_id):
        bot.edit_message_text("👑 عاش يا دبابة، انت كده مشترك خلاص، نورتنا!", call.message.chat.id, call.message.message_id)
    else:
        bot.answer_callback_query(call.id, "❌ لسه مش مشترك، اشترك الاول يا دبابة", show_alert=True)

print("البوت شغال...")
bot.infinity_polling()
