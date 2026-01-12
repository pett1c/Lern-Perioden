import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# token, later to be transferred to .env
TOKEN = "token_here"

logging.basicConfig(level=logging.INFO)

# initialisation of the bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher()

# keyboard
def get_main_menu():
    builder = InlineKeyboardBuilder()
    
    # buttons
    builder.row(InlineKeyboardButton(text="🔒 | Management", callback_data="cmd_control"))
    builder.row(InlineKeyboardButton(text="💬 | AI Mode", callback_data="cmd_ai_mode"))
    builder.row(InlineKeyboardButton(text="💀 | Enemies", callback_data="cmd_enemies"),
                InlineKeyboardButton(text="👥 | Allies", callback_data="cmd_allies"))

    return builder.as_markup()

# /start command handler
@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    
    # greeting text
    welcome_text = (
        f"Hello, {user_name} (ID: {user_id})!\n"
        f"You've logged into ADVICE X system.\n"
        f"Access level: Guest (Level 1)\n"
        f"Organisation: Not assigned"
    )
    
    # send welcome message using keyboard
    await message.answer(welcome_text, reply_markup=get_main_menu())

# button press handling (for now just placeholders)
@dp.callback_query()
async def handle_callbacks(callback: types.CallbackQuery):
    if callback.data == "cmd_control":
        await callback.answer("⛔ Error: Not enough rights (Level 1)", show_alert=True)
    else:
        await callback.answer(f"Function '{callback.data}' is under development!", show_alert=False)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())