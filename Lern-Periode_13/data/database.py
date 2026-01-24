from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Integer, String, Boolean, ForeignKey, select
from config import POSTGRES_DSN

engine = create_async_engine(POSTGRES_DSN, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    coins: Mapped[int] = mapped_column(Integer, default=100)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_banned: Mapped[bool] = mapped_column(Boolean, default=False)
    username: Mapped[str] = mapped_column(String, nullable=True)

class Item(Base):
    __tablename__ = 'items'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    price: Mapped[int] = mapped_column(Integer)
    photo_id: Mapped[str] = mapped_column(String, nullable=True)

class Inventory(Base):
    __tablename__ = 'inventory'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'))
    quantity: Mapped[int] = mapped_column(Integer, default=1)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def add_user(tg_id: int, username: str = None):
    async with async_session() as session:
        user = await session.get(User, tg_id)
        if not user:
            session.add(User(id=tg_id, username=username))
            await session.commit()
        elif username and user.username != username:
            user.username = username
            await session.commit()

async def get_user(tg_id: int) -> User | None:
    async with async_session() as session:
        return await session.get(User, tg_id)

async def get_all_users() -> list[User]:
    async with async_session() as session:
        result = await session.execute(select(User))
        return list(result.scalars().all())

async def get_balance(tg_id: int) -> int:
    async with async_session() as session:
        user = await session.get(User, tg_id)
        # return user coins or 0
        return user.coins if user else 0

async def update_balance(tg_id: int, amount: int):
    async with async_session() as session:
        user = await session.get(User, tg_id)
        if user:
            user.coins += amount
            await session.commit()

async def set_user_coin_balance(tg_id: int, new_balance: int):
    async with async_session() as session:
        user = await session.get(User, tg_id)
        if user:
            user.coins = new_balance
            await session.commit()

async def set_admin_status(tg_id: int, is_admin: bool):
    async with async_session() as session:
        user = await session.get(User, tg_id)
        if user:
            user.is_admin = is_admin
            await session.commit()

async def set_ban_status(tg_id: int, is_banned: bool):
    async with async_session() as session:
        user = await session.get(User, tg_id)
        if user:
            user.is_banned = is_banned
            await session.commit()

# --- items & inventory ---

async def create_item(name: str, description: str, price: int, photo_id: str = None):
    async with async_session() as session:
        session.add(Item(name=name, description=description, price=price, photo_id=photo_id))
        await session.commit()

async def get_all_items() -> list[Item]:
    async with async_session() as session:
        result = await session.execute(select(Item))
        return list(result.scalars().all())

async def get_item(item_id: int) -> Item | None:
    async with async_session() as session:
        return await session.get(Item, item_id)

async def update_item(item_id: int, **kwargs):
    async with async_session() as session:
        item = await session.get(Item, item_id)
        if item:
            for key, value in kwargs.items():
                if hasattr(item, key):
                    setattr(item, key, value)
            await session.commit()

async def delete_item(item_id: int):
    async with async_session() as session:
        item = await session.get(Item, item_id)
        if item:
            await session.delete(item)
            await session.commit()

async def add_item_to_user(user_id: int, item_id: int):
    async with async_session() as session:
        result = await session.execute(select(Inventory).where(Inventory.user_id == user_id, Inventory.item_id == item_id))
        inv_item = result.scalars().first()
        if inv_item:
            inv_item.quantity += 1
        else:
            session.add(Inventory(user_id=user_id, item_id=item_id, quantity=1))
        await session.commit()

async def get_user_inventory(user_id: int):
    async with async_session() as session:
        stmt = select(Inventory, Item).join(Item, Inventory.item_id == Item.id).where(Inventory.user_id == user_id)
        result = await session.execute(stmt)
        return result.all()

async def remove_item_from_user(user_id: int, item_id: int) -> bool:
    async with async_session() as session:
        result = await session.execute(select(Inventory).where(Inventory.user_id == user_id, Inventory.item_id == item_id))
        inv_item = result.scalars().first()
        if inv_item and inv_item.quantity > 0:
            inv_item.quantity -= 1
            if inv_item.quantity == 0:
                await session.delete(inv_item)
            await session.commit()
            return True
        return False
