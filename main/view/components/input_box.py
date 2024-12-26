import reflex as rx
from main.controller.pregunta_respuesta import State_qa as sqa
def input_box() -> rx.Component:
    return (
        rx.input(
            placeholder="Haz tu pregunta",
            value=sqa.question,
            on_change=sqa.set_question,
            on_key_down=sqa.handle_key_down,
            autofocus=True,
            class_name="input"
            ),       
    )