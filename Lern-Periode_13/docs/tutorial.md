---
title: tg bot user manager with economy・tutorial
---
## 1・goal & previous knowledge

### ・goal & what you'll learn

In this tutorial, we'll create a Telegram bot using **Python** that will be able to do the following:

- **User Management**: basic user management, namely banning in the bot and access to admin functions.
- **Economy**: basic virtual economy, with currency, inventory, shop, and management via the admin panel.
- **Admin panel**: sending advertisements (messages to all users in the bot), user management, and item management.
- **AI functions**: we'll connect the API with a free model.
- **Statistics**: basic statistics.

At the end, you'll create an excellent foundation for developing a versatile bot manager.

### ・previous knowledge

To follow this guide effectively, we assume you:

- Know the basics of **Python 3** (functions, classes, decorators).
- Have a basic understanding of **SQL** (tables, columns, queries).
- Know how to use a terminal.
- Have a Telegram account and have created a bot via `@BotFather`.

---

## 2・tutorial

### ・step 1: foundation (config & db)

Every building needs a foundation. We start by configuring the environment and setting up the database.

1. **Config**: We load sensitive data (tokens), etc. from `.env` in `config.py`.
   ```python
   # ./config.py
   import os
   from dotenv import load_dotenv

   load_dotenv()

   BOT_TOKEN = os.getenv("BOT_TOKEN")
   ADMIN_ID = int(os.getenv("ADMIN_ID"))
   # Default to local postgres if not set. Warning! You must ensure DB exists or update .env.
   POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql+asyncpg://postgres:postgres@localhost/foxbot")
   OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
   ```
2. **Database**: In `data/database.py`, we define our tables (`User`, `Item`, `Inventory`) using SQLAlchemy's async ORM.
   * **Why Async?** We use `asyncpg` so database queries don't "freeze" the bot while waiting for a response.
   * **Code, example**:
     ```python
     # data/database.py
     class User(Base):
         __tablename__ = "users"
         id: Mapped[int] = mapped_column(primary_key=True)
         coins: Mapped[int] = mapped_column(default=0)
         is_admin: Mapped[bool] = mapped_column(default=False)
     ```

### ・step 2: core loop & routers

In `main.py`, we initialize the `DB`, `Bot` and `Dispatcher`. Instead of writing all features in one file, we register **Routers**.

* **Routers** are like mini-dispatchers. We have one for `admin`, one for `economics`, and one for `ai`.
* **Code**:
  ```python
  # main.py
  async def main():
      if not BOT_TOKEN:
          print("Error: BOT_TOKEN is not set.")
          return

      # initialize db
      await init_db()

      bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
      dp = Dispatcher()

      # middleware
      dp.update.middleware(LoggingMiddleware())

      # include routers
      dp.include_router(admin.router) # admin, specialized
      dp.include_router(ai.router)
      dp.include_router(economics.router)
      dp.include_router(common.router) # common, catch-all

      print("Starting bot...")
      try:
          await bot.delete_webhook(drop_pending_updates=True)
          await dp.start_polling(bot)
      except Exception as e:
          print(f"🛑 CRITICAL ERROR: {e}")
      finally:
          await bot.session.close()

  if __name__ == "__main__":
      try:
          asyncio.run(main())
      except KeyboardInterrupt:
          print("Exit")
  ```

### ・step 3: building the admin panel (keyboards & ads)

The admin panel functions as a centralized control center for bot management, utilizing `handlers/admin.py`.

1. **Menu System**: We utilize **Inline Keyboards** to provide an interactive menu experience.

   * **Concept**: We visualize the "menu" using buttons. In `keyboards/builders.py` or directly in the handler, we build rows of buttons.
   * **Code**:
     ```python
     # handlers/admin.py
     def get_admin_menu():
         builder = InlineKeyboardBuilder()
         builder.row(InlineKeyboardButton(text="📢 Send Ad", callback_data="admin_send_ad"))
         builder.row(InlineKeyboardButton(text="👥 User Management", callback_data="admin_users"))
         return builder.as_markup()
     ```
2. **Ad Broadcast**: To send messages to all users, we implement a broadcast loop.

   * **Logic**: We fetch *all* users from the database, then iterate through them.
   * **Crucial**: We implement robust error handling inside the loop. If a user has blocked the bot or the chat is not found, we simply skip them to ensure the broadcast continues for others.
   * **Code**:
     ```python
     @router.message(AdSteps.ad_text)
     async def process_ad_text(message: Message, state: FSMContext, bot: Bot):
         users = await get_all_users()
         for user in users:
             try:
                 await bot.send_message(chat_id=user.id, text=message.text)
             except Exception:
                 pass # User blocked bot? Ignore.
         await message.answer("✅ Ad sent.")
     ```

### ・step 4: economy & inventory system

The economy system manages the flow of items and currency balances within the bot, handled by `handlers/economics.py`.

1. **Dynamic Shop Buttons**:

   * **Logic**: We retrieve the list of available items from the database and dynamically generate a button for each one.
   * **Callback Magic**: We embed the Item ID in the button: `callback_data=f"buy_item_{item.id}"`. When clicked, we extract this ID to process the specific purchase.
   * **Code**:
     ```python
     # handlers/economics.py
     items = await get_all_items()
     builder = InlineKeyboardBuilder()
     for item in items:
         builder.row(InlineKeyboardButton(
             text=f"{item.name} - {item.price} 🪙", 
             callback_data=f"view_item_{item.id}"
         ))
     ```
2. **Inventory & Gifting**:

   * **Logic**: Inventory is structured as a mapped relationship in the database. We iterate through `user.inventory` to display owned items.
   * **Interaction**: We provide a "Gift" button next to each item to facilitate transfers.
   * **Code**:
     ```python
     # handlers/economics.py
     for row in inv:
         inventory, item = row
         text += f"📦 {item.name} (x{inventory.quantity})\n"
         builder.row(InlineKeyboardButton(
             text=f"🎁 Gift {item.name}", 
             callback_data=f"gift_item_{item.id}"
         ))
     ```

### ・step 5: ai integration (api binding & finding full free ai model)

We integrate an external AI service to provide chat functionality, managed by `handlers/ai.py`.

1. **API Connection**: We use `aiohttp` to send asynchronous POST requests to OpenRouter.

   * **Headers**: The `Authorization: Bearer KEY` header is required for authentication.
   * **Model**: We use `deepseek-r1t2-chimera` (free).
   * **Code**:
     ```python
     # handlers/ai.py
     async def query_openrouter(prompt: str):
         headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}
         data = {
             "model": "tngtech/deepseek-r1t2-chimera:free",
             "messages": [{"role": "user", "content": prompt}]
         }
         async with aiohttp.ClientSession() as session:
             async with session.post(url, json=data, headers=headers) as resp:
                 result = await resp.json()
                 return result['choices'][0]['message']['content']
     ```
2. **Finding free OpenRouter API model**:

   * To get started, go to [https://openrouter.ai](https://openrouter.ai) and click ‘Explore Models’. Then, on the left, you will see the Prompt Pricing settings: select Free and choose the model you like. After that, at the bottom, you will find ‘Create API Key’. Create it and save it (because you will only see it once). Profit!

   ![OpenRouter Pricing](https://files.catbox.moe/lf9ni6.jpg)

---

## 3・Conclusion

### ・what could go wrong?

Errors you might face during development:

1. **`TelegramForbiddenError` (Bot Blocked)**: specific to `aiogram`. Occurs when you try to send a message to a user who has stopped the bot.
   * *Fix*: Always wrap `send_message` calls in `try...except` blocks, especially in loops.
2. **`TelegramConflictError`**: Occurs when you run two instances of the bot with the same token (e.g., one on your PC and one on a server).
   * *Fix*: Ensure only one instance is running at a time.
3. **`TelegramRetryAfter` (Flood Control)**: If you send too many messages too quickly (e.g., >30 per second), Telegram will block you temporarily.
   * *Fix*: Use `asyncio.sleep()` in your broadcast loops to rate-limit yourself.
4. **`PendingRollbackError` (SQLAlchemy)**: Happens if a previous DB query failed (raised an exception) and the session was not rolled back.
   * *Fix*: Always use `async with async_session() as session:` context managers, or explicitly call `session.rollback()` in exception handlers.
5. **`TelegramBadRequest: Message is not modified`**: Occurs when submitting an edit request identical to the current message state.
   * *Fix*: Check if the content has changed before calling `edit_text`.

### ・result (gif)

![result](https://files.catbox.moe/8d7sip.gif)

### ・further work

* **deployment**: Move the bot from local hosting to a cloud environment (e.g., Railway, Heroku, or a VPS).
* **containerization (Docker):** Create a `Dockerfile` and `docker-compose.yml` for the bot and the PostgreSQL database.
* **enhance AI**: Implement a history buffer (Redis or DB) for the AI chat so it remembers context across multiple messages & create detailed system prompt.