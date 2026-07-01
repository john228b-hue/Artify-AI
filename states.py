from aiogram.fsm.state import State, StatesGroup


class GenerateImageStates(StatesGroup):
    waiting_for_prompt = State()
