import aiohttp
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from config import OPENROUTER_API_KEY
from keyboards.builders import get_main_menu
from utils.states import AIState

router = Router()

async def query_openrouter(prompt: str):
    if not OPENROUTER_API_KEY:
        return "⚠️ OpenRouter API Key is missing."
    
    # openrouter api
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    # using deepseek as requested
    data = {
        "model": "tngtech/deepseek-r1t2-chimera:free", 
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['message']['content']
                else:
                    return f"Error {response.status}: {await response.text()}"
    except Exception as e:
        return f"Exception: {e}"

@router.callback_query(F.data == "cmd_ai_mode")
async def enter_ai_mode(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "💬 <b>AI Chat Activated</b>\nType anything to talk to AI.\nType /exit to return to main menu."
    )
    await state.set_state(AIState.chat)
    await callback.answer()

@router.message(AIState.chat, Command("exit"))
async def exit_ai_mode(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Main menu returned.", reply_markup=get_main_menu())

@router.message(F.text.startswith("/ask "))
async def ask_ai(message: types.Message):
    prompt = message.text[5:]
    response = await query_openrouter(prompt)
    await message.answer(f"🤖 <b>AI</b>: {response}")

@router.message(AIState.chat)
async def chat_ai(message: types.Message):
    wait_msg = await message.answer("🤔 Thinking...")
    response = await query_openrouter(message.text)
    await wait_msg.delete()
    await message.answer(response)
