import asyncio
import logging
import os
import sys

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

# load .env
load_dotenv()

# safely get bot token from .env
TOKEN = os.getenv("BOT_TOKEN")

# check if token is available
if not TOKEN:
    print("Error: BOT_TOKEN is not set in environment variables.")
    sys.exit(1) 

# enabling logging
logging.basicConfig(level=logging.INFO)

# initialization
bot = Bot(token=TOKEN)
dp = Dispatcher()

# keyboards

def get_main_menu():
    """main menu keyboard"""
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🔒 | Management", callback_data="cmd_control"))
    builder.row(InlineKeyboardButton(text="💬 | AI Mode", callback_data="cmd_ai_mode"))
    # Task: Economics Menu (Кнопка входа)
    builder.row(InlineKeyboardButton(text="🪙 | Economics", callback_data="cmd_economics"))
    return builder.as_markup()

def get_economics_menu():
    """economics menu keyboard"""
    builder = InlineKeyboardBuilder()
    # Кнопки подменю
    builder.row(InlineKeyboardButton(text="💰 My Balance", callback_data="eco_balance"))
    builder.row(InlineKeyboardButton(text="💸 Transfer", callback_data="eco_transfer"))
    builder.row(InlineKeyboardButton(text="💎 Shop", callback_data="eco_shop"))
    # Кнопка "Назад" обязательна для навигации
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_back_main"))
    return builder.as_markup()

# handlers (logic)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.first_name}! Systems of FOX are operational.",
        reply_markup=get_main_menu()
    )

# handler for economics menu
@dp.callback_query(F.data == "cmd_economics")
async def open_economics(callback: types.CallbackQuery):
    # edit message to show economics menu
    await callback.message.edit_text(
        "🪙 **Financial Department of FOX**\nChoose an action:",
        reply_markup=get_economics_menu()
    )
    await callback.answer()

# handler for "Back" button
@dp.callback_query(F.data == "cmd_back_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Main menu returned.",
        reply_markup=get_main_menu()
    )
    await callback.answer()

# placeholder handlers for economics buttons
@dp.callback_query(F.data.startswith("eco_"))
async def economics_actions(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    await callback.answer(f"Function {action} is under development...", show_alert=True)

# echo-logic
# this handler should be LAST among message handlers
@dp.message(F.text)
async def echo_handler(message: types.Message):
    user_text = message.text.lower()

    if "hello" in user_text:
        await message.answer("Greetings, member of clan FOX! 🫡")
    elif "status" in user_text:
        await message.answer("All systems are operational.")
    else:
        # echo-answer (repeat what user said, or say we don't understand)
        await message.answer(f"You wrote: {message.text}. I'm still learning to understand context.")

# execution (error handling)

async def main():
    print("Starting bot...")
    try:
        # delete webhooks, if any, and start polling
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except Exception as e:
        print(f"🛑 CRITICAL ERROR: {e}")
    except KeyboardInterrupt:
        print("🛑 Bot stopped manually by user.")
    finally:
        print("Session ended.")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")