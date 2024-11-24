import reflex as rx
from ..styles import chat_style as cs
from main.controller.pregunta_respuesta import State_qa as sqa

def button(text="", on_click=None):
    return rx.button(
        f"{text}",
        style=cs.button_style,
        on_click=on_click,
    )