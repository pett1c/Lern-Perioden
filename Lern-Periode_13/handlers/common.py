from aiogram import Router, types, F
from aiogram.filters import CommandStart
from keyboards.builders import get_main_menu
from data.database import add_user

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await add_user(message.from_user.id)
    await message.answer(
        f"Hello, {message.from_user.first_name}! Systems of FOX are operational.",
        reply_markup=get_main_menu()
    )

@router.callback_query(F.data == "cmd_back_main")
async def back_to_main(callback: types.CallbackQuery):
    await callback.message.edit_text(
        f"Hello, {callback.from_user.first_name}! Systems of FOX are operational.",
        reply_markup=get_main_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "cmd_stats")
async def cmd_stats(callback: types.CallbackQuery):
    from data.database import get_all_users, get_all_items, async_session, User, select
    from sqlalchemy import func

    async with async_session() as session:
        # count users
        total_users = await session.scalar(select(func.count(User.id)))
        admins = await session.scalar(select(func.count(User.id)).where(User.is_admin == True))
        regular = total_users - admins
        
        # count groups
        groups = await session.scalar(select(func.count(User.id)).where(User.id < 0))
        # total coins
        total_coins = await session.scalar(select(func.sum(User.coins))) or 0
        
        # total items
        from data.database import Item
        total_items = await session.scalar(select(func.count(Item.id)))

    text = (
        f"📊 <b>Statistics:</b>\n"
        f"👤 Users: {total_users}\n"
        f" ・ Regular: {regular}\n"
        f" ・ Admins: {admins}\n"
        f"📢 Groups: {groups}\n"
        f"💰 Coins: {total_coins}\n"
        f"📦 Items: {total_items}"
    )
    await callback.message.edit_text(text, reply_markup=get_main_menu())

@router.message(F.text)
async def echo_handler(message: types.Message):
    user_text = message.text.lower()
    if "hello" in user_text:
        await message.answer("Greetings, member of clan FOX! 🫡")
    elif "status" in user_text:
        await message.answer("All systems are operational.")
    else:
        await message.answer(f"You wrote: {message.text}. I'm still learning to understand context.")
