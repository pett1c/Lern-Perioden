import logging
from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message, CallbackQuery

logger = logging.getLogger(__name__)

class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        user = data.get("event_from_user")
        if user:
            user_id = user.id
            username = user.username or "unknown"
            if isinstance(event, Message) and event.text:
                logger.info(f"User {user_id} (@{username}) sent message: {event.text}")
            elif isinstance(event, CallbackQuery):
                logger.info(f"User {user_id} (@{username}) clicked button: {event.data}")
        
        return await handler(event, data)
