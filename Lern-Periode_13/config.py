import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
# Default to local postgres if not set. Warning: User must ensure DB exists or update .env
POSTGRES_DSN = os.getenv("POSTGRES_DSN", "postgresql+asyncpg://postgres:postgres@localhost/foxbot")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
