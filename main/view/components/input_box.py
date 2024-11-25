import reflex as rx
from ..styles import chat_style as cs
from main.controller.pregunta_respuesta import State_qa as sqa
def input_box() -> rx.Component:
    return (
        rx.input(
            placeholder="Haz tu pregunta",
            value=sqa.question,
            on_change=sqa.set_question,
            on_key_down=sqa.handle_key_down,
            autofocus=True,
            style= cs.input_style,
            ),       
    )