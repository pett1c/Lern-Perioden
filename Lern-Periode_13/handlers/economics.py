from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from keyboards.builders import get_economics_menu, get_main_menu
from data.database import (
    get_balance, update_balance, add_user, get_all_items, get_item, 
    add_item_to_user, get_user_inventory, remove_item_from_user
)
from utils.states import TransferState, ItemTransferState
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

@router.callback_query(F.data == "cmd_economics")
async def open_economics(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🪙 <b>Financial Department of FOX</b>\nChoose an action:",
        reply_markup=get_economics_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "eco_balance")
async def show_balance(callback: types.CallbackQuery):
    balance = await get_balance(callback.from_user.id)
    await callback.answer(f"💰 Your balance: {balance} coins", show_alert=True)

# --- Shop ---
@router.callback_query(F.data == "eco_shop")
async def eco_shop(callback: types.CallbackQuery):
    items = await get_all_items()
    balance = await get_balance(callback.from_user.id)
    
    if not items:
        await callback.answer("🏪 Shop is empty right now.", show_alert=True)
        return

    builder = InlineKeyboardBuilder()
    text = f"💎 <b>Shop</b>\nYour Balance: {balance}\n\nSelect an item to view details:"
    
    # grid layout? single column for now
    for item in items:
        builder.row(InlineKeyboardButton(text=f"{item.name} - {item.price} 🪙", callback_data=f"view_item_{item.id}"))
    
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_economics"))
    
    try:
        await callback.message.edit_text(text, reply_markup=builder.as_markup())
    except Exception:
        # fallback for photo messages
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=builder.as_markup())

@router.callback_query(F.data.startswith("view_item_"))
async def view_item_details(callback: types.CallbackQuery):
    item_id = int(callback.data.split("_")[2])
    item = await get_item(item_id)
    
    if not item:
        await callback.answer("❌ Item not found.", show_alert=True)
        return

    text = f"📦 <b>{item.name}</b>\n\n📝 {item.description}\n\n💰 Price: {item.price} coins"
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="🛒 Buy", callback_data=f"buy_item_{item.id}"))
    builder.row(InlineKeyboardButton(text="🔙 Back to Shop", callback_data="eco_shop"))

    if item.photo_id:
        # delete and send new if photo
        await callback.message.delete()
        await callback.message.answer_photo(item.photo_id, caption=text, reply_markup=builder.as_markup())
    else:
        # just replace message
        await callback.message.delete()
        await callback.message.answer(text, reply_markup=builder.as_markup())

@router.callback_query(F.data.startswith("buy_item_"))
async def buy_item(callback: types.CallbackQuery):
    item_id = int(callback.data.split("_")[2])
    item = await get_item(item_id)
    
    if not item:
        await callback.answer("❌ Item not found.", show_alert=True)
        return
        
    user_id = callback.from_user.id
    balance = await get_balance(user_id)
    
    if balance < item.price:
        await callback.answer(f"❌ Not enough coins! Need {item.price}.", show_alert=True)
        return
    
    await update_balance(user_id, -item.price)
    await add_item_to_user(user_id, item_id)
    await callback.answer(f"✅ You bought {item.name}!", show_alert=True)

# --- inventory ---
@router.callback_query(F.data == "eco_inventory")
async def eco_inventory(callback: types.CallbackQuery):
    
    # ... code ...

    for row in inv:
        inventory, item = row # unwrap
        text += f"📦 <b>{item.name}</b> (x{inventory.quantity})\n"
        builder.row(InlineKeyboardButton(text=f"Give {item.name}", callback_data=f"gift_item_{item.id}"))
        
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_economics"))
    await callback.message.edit_text(text, reply_markup=builder.as_markup())

# --- transfer item ---
@router.callback_query(F.data.startswith("gift_item_"))
async def gift_item_start(callback: types.CallbackQuery, state: FSMContext):
# ...
    
    # verify sender has item
    removed = await remove_item_from_user(sender_id, item_id)
    if not removed:
        await message.answer("❌ Transaction failed. Item not in inventory?")
        await state.clear()
        return
        
    # Ensure recipient exists
    await add_user(recipient_id) # ensure db record
    await add_item_to_user(recipient_id, item_id)
    
    await message.answer(f"✅ Item sent to User {recipient_id}.")
    await state.clear()


# --- Transfer Coins ---
@router.callback_query(F.data == "eco_transfer")
async def eco_transfer(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("💸 Enter the <b>User ID</b> of the recipient:")
    await state.set_state(TransferState.wait_id)
    await callback.answer()

@router.message(TransferState.wait_id)
async def process_transfer_id(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("⚠️ Please enter a valid numeric User ID.")
        return
    
    recipient_id = int(message.text)
    # Self-transfer check
    if recipient_id == message.from_user.id:
        await message.answer("⚠️ You cannot transfer money to yourself.")
        return
        
    await state.update_data(recipient_id=recipient_id)
    await message.answer("💸 Enter the <b>amount</b> to transfer:")
    await state.set_state(TransferState.wait_amount)

@router.message(TransferState.wait_amount)
async def process_transfer_amount(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("⚠️ Please enter a valid numeric amount.")
        return
    
    amount = int(message.text)
    if amount <= 0:
        await message.answer("⚠️ Amount must be positive.")
        return

    sender_id = message.from_user.id
    balance = await get_balance(sender_id)
    
    if balance < amount:
        await message.answer(f"❌ Not enough funds. Your balance: {balance}")
        await state.clear()
        return

    data = await state.get_data()
    await add_user(data.get('recipient_id')) 
    recipient_id = data.get('recipient_id')
    
    await update_balance(sender_id, -amount)
    await update_balance(recipient_id, amount)
    
    await message.answer(f"✅ Successfully transferred {amount} coins to ID {recipient_id}.")
    await state.clear()

