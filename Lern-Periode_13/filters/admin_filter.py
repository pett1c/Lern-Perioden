from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from config import ADMIN_ID
from data.database import get_user

class AdminCheck(BaseFilter):
    async def __call__(self, event: Union[Message, CallbackQuery]) -> bool:
        # check hardcoded ADMIN_ID first
        if event.from_user.id == ADMIN_ID:
            return True
        
        # check db
        user = await get_user(event.from_user.id)
        if user and user.is_admin:
            return True
            
        return False
