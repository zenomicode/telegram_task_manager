from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
import app.buttons as kb
from app.state import Reg
from app.database.db import tasks
from app.database.requests import get_tasks

router = Router()



@router.callback_query(F.data == "back")
@router.message(CommandStart())
async def cmd_start(message, state: FSMContext) -> None:
    
    if isinstance(message, Message):
        await message.delete()
        await message.answer("Это Планер", reply_markup=kb.main)

    else:
        await message.answer("")
        await message.message.answer("Это Планер",
                                     reply_markup=kb.main)

        
@router.callback_query(F.data == "main_1")
async def add_task(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Reg.task)
    await callback.message.answer("Запишите задачу:")
    
@router.message(Reg.task)
async def reg_name(message: Message, state: FSMContext):
    if message.from_user.id not in tasks:
        tasks[message.from_user.id] = []
    
    tasks[message.from_user.id].append(message.text)
    await message.delete()
    await message.answer("Задача добавлена!",
                                      reply_markup=kb.back)
    
    
    
@router.callback_query(F.data == "main_2")
async def add_task(callback: CallbackQuery, state: FSMContext):
    await get_tasks()
    if len(tasks[callback.from_user.id]) == 0:
        await callback.message.answer(
        text="Задач нет!", 
        reply_markup=kb.back)
    else:
        await callback.message.answer(
            text="".join([f"{num}. {t}\n" for num, t in enumerate(tasks[callback.from_user.id], 1)]), 
            reply_markup=kb.view_tasks)
    
    
    
    
    
@router.callback_query(F.data == "del_task")
async def del_task(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Выберите Задачу для удаления",
                                               reply_markup=await kb.list_tasks(tasks[callback.from_user.id]))
    
@router.callback_query(F.data.startswith("task_"))
async def del_task(callback: CallbackQuery, state: FSMContext):
    task_id = callback.data.split('_')[1]
    tasks[callback.from_user.id].pop(int(task_id) - 1)
    await callback.message.answer(text="Задача удалена",
                                               reply_markup=kb.back)