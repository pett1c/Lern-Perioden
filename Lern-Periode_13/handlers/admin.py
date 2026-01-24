from aiogram import Router, types, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from filters.admin_filter import AdminCheck
from utils.states import AdSteps, UserManState, ItemManState
from keyboards.builders import get_admin_menu, get_main_menu
from data.database import (
    get_all_users, get_user, update_balance, set_admin_status, set_ban_status,
    create_item, delete_item, get_all_items, set_user_coin_balance
)
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

def get_admin_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="📢 Send Ad", callback_data="admin_send_ad"))
    builder.row(InlineKeyboardButton(text="👥 User Management", callback_data="admin_users"))
    builder.row(InlineKeyboardButton(text="🛍️ Item Management", callback_data="admin_items"))
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_back_main"))
    return builder.as_markup()

@router.callback_query(F.data == "cmd_control", AdminCheck())
async def admin_control(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🔒 <b>Admin Control Panel</b>\nSelect an action:",
        reply_markup=get_admin_menu()
    )
    await callback.answer()

@router.callback_query(F.data == "cmd_control")
async def admin_control_fail(callback: types.CallbackQuery):
    await callback.answer("⛔ Access Denied", show_alert=True)

# --- ad sending ---
@router.callback_query(F.data == "admin_send_ad")
async def cmd_send_ad(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter the advertisement text:")
    await state.set_state(AdSteps.ad_text)
    await callback.answer()

@router.message(AdSteps.ad_text)
async def process_ad_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Now send a photo (or type 'skip'):")
    await state.set_state(AdSteps.ad_photo)

@router.message(AdSteps.ad_photo)
async def process_ad_photo(message: types.Message, state: FSMContext, bot: Bot):
    if message.photo:
        await state.update_data(photo=message.photo[-1].file_id)
    elif message.text and message.text.lower() != 'skip':
         await message.answer("Please send a photo or type 'skip'.")
         return
    
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')

    users = await get_all_users()
    count = 0
    
    # broadcast loop
    for user in users:
        try:
            if photo:
                await bot.send_photo(chat_id=user.id, photo=photo, caption=text)
            else:
                await bot.send_message(chat_id=user.id, text=text)
            count += 1
        except Exception:
            # blocked user or other error
            pass
    
    await state.clear()
    await message.answer(f"✅ Ad sent to {count} users.", reply_markup=get_main_menu())

# --- user management ---
@router.callback_query(F.data == "admin_users")
async def admin_users_menu(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter User ID to manage:")
    await state.set_state(UserManState.wait_id)
    await callback.answer()

@router.message(UserManState.wait_id)
async def user_man_show(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Invalid ID.")
        return
    
    user_id = int(message.text)
    user = await get_user(user_id)
    if not user:
        await message.answer("User not found.")
        return
    
    await state.update_data(target_id=user_id)
    
    # User status text
    status = []
    if user.is_admin: status.append("Admin")
    if user.is_banned: status.append("BANNED")
    status_str = ", ".join(status) if status else "User"

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✏️ Edit Balance", callback_data="adm_edit_bal"))
    builder.row(InlineKeyboardButton(text="🛡️ Toggle Admin", callback_data="adm_toggle_admin"))
    builder.row(InlineKeyboardButton(text="🚫 Toggle Ban", callback_data="adm_toggle_ban"))
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_control")) # Should clear state?

    await message.answer(
        f"👤 <b>User:</b> {user_id}\n"
        f"💰 <b>Balance:</b> {user.coins}\n"
        f"🏷️ <b>Status:</b> {status_str}",
        reply_markup=builder.as_markup()
    )
    await state.set_state(UserManState.view_user)
    
    # ... code ...

    await set_user_coin_balance(target_id, new_bal)
    await message.answer(f"✅ Balance set to {new_bal}.")
    await state.clear() # exit to menu

@router.callback_query(UserManState.view_user, F.data == "adm_toggle_admin")
async def adm_toggle_admin(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    target_id = data.get('target_id')
    user = await get_user(target_id)
    
    new_status = not user.is_admin
    await set_admin_status(target_id, new_status)
    await callback.answer(f"Admin status set to: {new_status}", show_alert=True)

# ...

# --- item management ---
@router.callback_query(F.data == "admin_items")
async def admin_items_menu(callback: types.CallbackQuery):
    items = await get_all_items()
    text = "<b>Items:</b>\n"
    for item in items:
        text += f"ID: {item.id} | {item.name} | {item.price} coins\n"
        
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="➕ Add Item", callback_data="adm_add_item"))
    builder.row(InlineKeyboardButton(text="✏️ Edit Item", callback_data="adm_edit_item_start"))
    builder.row(InlineKeyboardButton(text="❌ Delete Item", callback_data="adm_del_item"))
    builder.row(InlineKeyboardButton(text="🔙 Back", callback_data="cmd_control"))
    
    await callback.message.edit_text(text, reply_markup=builder.as_markup())
    
# --- edit item handlers ---
class ItemEditState(StatesGroup):
    wait_id = State()
    view_item = State()
    edit_name = State()
    edit_price = State()
    edit_desc = State()
    edit_photo = State()

@router.callback_query(F.data == "adm_edit_item_start")
async def adm_edit_item_start(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter Item ID to edit:")
    await state.set_state(ItemEditState.wait_id)
    await callback.answer()

@router.message(ItemEditState.wait_id)
async def adm_edit_item_show(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Invalid ID.")
        return
    
    item_id = int(message.text)
    from data.database import get_item
    item = await get_item(item_id)
    
    if not item:
        await message.answer("Item not found.")
        return
    
    await state.update_data(item_id=item_id)
    
    text = (f"🛠 <b>Editing Item</b> {item_id}\n"
            f"Name: {item.name}\n"
            f"Price: {item.price}\n"
            f"Desc: {item.description}\n"
            f"Photo: {'Has photo' if item.photo_id else 'None'}")
            
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="Name", callback_data="edit_item_name"), InlineKeyboardButton(text="Price", callback_data="edit_item_price"))
    builder.row(InlineKeyboardButton(text="Desc", callback_data="edit_item_desc"), InlineKeyboardButton(text="Photo", callback_data="edit_item_photo"))
    builder.row(InlineKeyboardButton(text="✅ Done", callback_data="admin_items"))

    await message.answer(text, reply_markup=builder.as_markup())
    await state.set_state(ItemEditState.view_item)

@router.callback_query(ItemEditState.view_item, F.data == "edit_item_name")
async def edit_trigger_name(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter new name:")
    await state.set_state(ItemEditState.edit_name)
    await callback.answer()

@router.message(ItemEditState.edit_name)
async def edit_process_name(message: types.Message, state: FSMContext):
    data = await state.get_data()
    from data.database import update_item
    await update_item(data['item_id'], name=message.text)
    await message.answer("✅ Content updated.")
    # return to menu
    await message.answer("Saved. Go back to list.", reply_markup=get_admin_menu())
    await state.clear()

@router.callback_query(ItemEditState.view_item, F.data == "edit_item_price")
async def edit_trigger_price(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter new price:")
    await state.set_state(ItemEditState.edit_price)
    await callback.answer()

@router.message(ItemEditState.edit_price)
async def edit_process_price(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Invalid price.")
        return
    data = await state.get_data()
    from data.database import update_item
    await update_item(data['item_id'], price=int(message.text))
    await message.answer("✅ Price updated.")
    await state.clear()

@router.callback_query(ItemEditState.view_item, F.data == "edit_item_desc")
async def edit_trigger_desc(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter new description:")
    await state.set_state(ItemEditState.edit_desc)
    await callback.answer()

@router.message(ItemEditState.edit_desc)
async def edit_process_desc(message: types.Message, state: FSMContext):
    data = await state.get_data()
    from data.database import update_item
    await update_item(data['item_id'], description=message.text)
    await message.answer("✅ Description updated.")
    await state.clear()

@router.callback_query(ItemEditState.view_item, F.data == "edit_item_photo")
async def edit_trigger_photo(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Send new photo:")
    await state.set_state(ItemEditState.edit_photo)
    await callback.answer()

@router.message(ItemEditState.edit_photo)
async def edit_process_photo(message: types.Message, state: FSMContext):
    if not message.photo:
         await message.answer("No photo.")
         return
    data = await state.get_data()
    from data.database import update_item
    await update_item(data['item_id'], photo_id=message.photo[-1].file_id)
    await message.answer("✅ Photo updated.")
    await state.clear()

@router.message(ItemManState.name)
async def item_name_or_id(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get("mode") == "delete":
        if not message.text.isdigit():
             await message.answer("Invalid ID")
             return
        await delete_item(int(message.text))
        await message.answer("✅ Item deleted.")
        await state.clear()
        return

    await state.update_data(name=message.text)
    await message.answer("Enter Price:")
    await state.set_state(ItemManState.price)

@router.message(ItemManState.price)
async def item_price(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("invalid price")
        return
    await state.update_data(price=int(message.text))
    await message.answer("Enter Description:")
    await state.set_state(ItemManState.description)

@router.message(ItemManState.description)
async def item_desc(message: types.Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await message.answer("Send Photo (or type 'skip'):")
    await state.set_state(ItemManState.photo)

@router.message(ItemManState.photo)
async def item_photo(message: types.Message, state: FSMContext):
    photo_id = None
    if message.photo:
        photo_id = message.photo[-1].file_id
    elif message.text and message.text.lower() != 'skip':
        await message.answer("Please send photo or 'skip'")
        return

    data = await state.get_data()
    # check if we are in edit mode? 
    # current flow is "add item".
    
    await create_item(
        name=data['name'],
        description=data['desc'],
        price=data['price'],
        photo_id=photo_id
    )
    await message.answer("✅ Item added.")
    await state.clear()

@router.callback_query(F.data == "adm_del_item")
async def adm_del_item_start(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Enter Item ID to delete:")
    await state.set_state(ItemManState.price) # reusing 'price' state as a holder for id int reading, or create new.
    # reusing ItemManState.name but logic differs.
    await state.set_state(ItemManState.name)
    await state.update_data(mode="delete") 
    await callback.answer()

# need to adjust ItemManState.name handler to handle delete mode

