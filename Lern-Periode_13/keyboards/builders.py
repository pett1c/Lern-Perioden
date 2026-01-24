from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🔒 | Management", callback_data="cmd_control"))
    builder.row(InlineKeyboardButton(text="💬 | AI Mode", callback_data="cmd_ai_mode"))
    builder.row(InlineKeyboardButton(text="🪙 | Economics", callback_data="cmd_economics"))
    builder.row(InlineKeyboardButton(text="📊 | Statistics", callback_data="cmd_stats"))
    return builder.as_markup()

def get_economics_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="💰 My Balance", callback_data="eco_balance"))
    builder.row(InlineKeyboardButton(text="🎒 Inventory", callback_data="eco_inventory"))
    builder.row(InlineKeyboardButton(text="💸 Transfer", callback_data="eco_transfer"))
    builder.row(InlineKeyboardButton(text="💎 Shop", callback_data="eco_shop"))
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_back_main"))
    return builder.as_markup()

def get_admin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📢 Send Ad", callback_data="admin_send_ad"))
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_back_main"))
    return builder.as_markup()
