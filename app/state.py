from aiogram.fsm.state import State, StatesGroup

class Reg(StatesGroup):
    task = State()
    step = State()