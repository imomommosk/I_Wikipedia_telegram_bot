import wikipedia
from aiogram import executor, types, Bot, Dispatcher
import logging
API_TOKEN='6313180814:AAEyM983o3KOKJRFcVTwB8lzKUaUravseZY'

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)
wikipedia.set_lang("uz")


@dp.message_handler(commands=["start", "help"])
async def hello(message:types.Message):
    await message.answer(f"Asslomalaykum 'I_bot_wikipedia'ga xush kelibsiz \n sizni qiziqtirgan malumotni yuboring.")

@dp.message_handler()
async def get_date(message: types.Message):
    try:
        matn = message.text
        await message.answer(wikipedia.summary(matn))
    except:
        await message.answer("Bunday malumot topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)