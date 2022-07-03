from config import *
from utils import *


@bot.message_handler(commands=["start"])
def startbot(msg):
    # import pdb; pdb.set_trace()
    user.id = msg.from_user.id
    "Ignites the bot application to take action"

    bot.reply_to(msg, ts.translate(f"Hey {msg.from_user.first_name}", "es"))

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    a = types.InlineKeyboardButton(
        text=ts.translate("Standard Plan - $10/month", "es"), callback_data="subscribe"
    )
    keyboard.add(a)

    bot.send_message(
        msg.from_user.id,
        ts.translate(
            f"""
<b>Telegram Chat</b>

Please select your subscription plan:
        """,
            "es",
        ),
        parse_mode="html",
        reply_markup=keyboard,
    )


@bot.message_handler(regexp="^Back")
def startbotn(msg):
    startbot(msg)


# Callback Handlers
@bot.callback_query_handler(func=lambda call: True)
def callback_answer(call):
    """
    Button Response
    """

    if call.data == "subscribe":

        payment_url, payment_id = buy_plan()

        short_url = shortener.tinyurl.short(payment_url)

        bot.send_message(
            call.message.chat.id,
            text=ts.translate(
                f"""
            
    <b>Payment ID - {payment_id}</b>
Make Your Payment Here To Receive Subscription Pass
    
    {short_url}
    
You have 15 seconds before this url disappears
            """,
                "es",
            ),
            parse_mode="html",
        )

    else:
        pass
