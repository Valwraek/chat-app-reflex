import reflex as rx
from ..model.datos_chat_app import datos_chat
from .components.input_box import input_box
from .components.button import button
from .styles import chat_style as cs
#Lógica de formateo de mensajes
def qa(question:str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=cs.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=cs.answer_style),
            text_align="left",
        ),
        margin_y="1em",
        width="100%",
    )

def chat():
    return rx.box(
        * [
            qa(question, answer)
            for question, answer in datos_chat()
        ],
        rx.hstack(
            input_box(),
            button("Enviar"),
            align="center",
        )
    )