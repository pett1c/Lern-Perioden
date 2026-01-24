from aiogram.fsm.state import State, StatesGroup

class AdSteps(StatesGroup):
    ad_text = State()
    ad_photo = State()
    confirm = State()

class AIState(StatesGroup):
    chat = State()

class TransferState(StatesGroup):
    wait_id = State()
    wait_amount = State()

class UserManState(StatesGroup):
    wait_id = State()
    view_user = State()
    wait_balance = State() # for editing balance

class ItemManState(StatesGroup):
    name = State()
    price = State()
    description = State()
    photo = State()

class ItemTransferState(StatesGroup):
    wait_id = State()
