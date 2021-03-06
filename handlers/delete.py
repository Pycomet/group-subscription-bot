from config import *
from utils import *

@bot.message_handler(commands=['removeuser'])
def removeUser(msg):
    """
    Removes A User From Group
    """
    try:
        message = msg.text.split(" ")
        user = loop.run_until_complete(
            client.get_entity(int(message[1]))
        )

        if user is not None:
            # Schedule User
            status = remove_user(user.id)
            if status == True:
                bot.send_message(
                    msg.from_user.id,
                    "User Deleted Successfully"
                )
            else:
                bot.send_message(
                    msg.from_user.id,
                    "User Removal Failed"
                )

        else:
            bot.send_message(
                msg.from_user.id,
                "User Not Found"
            )
    except Exception as e:
        print(e)
        bot.send_message(
            msg.from_user.id,
            "User ID Not Found"
        )