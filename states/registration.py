from aiogram.dispatcher.filters.state import StatesGroup, State

class registration(StatesGroup):
    group = State()
    name = State()