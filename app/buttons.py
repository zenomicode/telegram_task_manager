from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Создать задачу", callback_data="main_1")],
    [InlineKeyboardButton(text="Показать задачи", callback_data="main_2")]
])

back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="<<<<<<", callback_data="back")]])

view_tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Удалить задачи", callback_data="del_task")],
    [InlineKeyboardButton(text="<<<<<<", callback_data="back")]
])

async def list_tasks(tasks: list):
    builder = InlineKeyboardBuilder()
    # Добавляем кнопки вопросов
    for task_id, _ in enumerate(tasks, 1):
        builder.add(
            InlineKeyboardButton(
                text=str(task_id),
                callback_data=f'task_{task_id}'
            )
        )
    return builder.adjust(5).as_markup()