import reflex as rx
from main.controller.pregunta_respuesta import State_qa as sqa

def button(text="", on_click=None):
    return rx.button(
        f"{text}",
        on_click=on_click,
        class_name="button"
    )