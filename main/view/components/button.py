import reflex as rx
from ..styles import chat_style as cs

def button(text=""):
    return rx.button(
        "Pregunta",
        style=cs.button_style,
    )