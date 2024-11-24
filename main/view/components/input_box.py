import reflex as rx
from ..styles import chat_style as cs
from main.controller.pregunta_respuesta import State_qa as sqa
def input_box() -> rx.Component:
    return (
        rx.input(
            placeholder="Haz tu pregunta",
            on_change=sqa.set_question,
            style= cs.input_style,
            ),       
    )