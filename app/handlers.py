# imports
from aiogram import F, Router, Bot

from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.enums import ParseMode

from config import TG_BOT_TOKEN
from buttons import Buttons
from text import menu_text, info_text


router = Router()
bot = Bot(TG_BOT_TOKEN, parse_mode=ParseMode.HTML)


@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{menu_text}", 
                         reply_markup=Buttons.menu_button)


@router.message(F.text == 'В меню🧑🏿‍💻🗂')
async def get_menu(message: Message):
    await message.answer(str(menu_text), reply_markup=Buttons.menu_button)


@router.message(F.text == 'Информация о нас')
async def get_info_about_us(message: Message):
    await message.answer(str(info_text), reply_markup=Buttons.info_button)