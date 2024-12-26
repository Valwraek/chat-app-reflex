import reflex as rx
from .components.input_box import input_box
from .components.button import button
from ..controller.pregunta_respuesta import State_qa as sqa

#Lógica de formateo de mensajes
def qa(question:str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, class_name="question"),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, class_name="answer"),
            text_align="left",
        ),
        margin_y="1em",
        width="100%",
    )

def chat():
    return rx.box(
        rx.box(
            rx.box(
                rx.foreach (
                sqa.chat_history,
                lambda messages: qa(messages[0], messages[1]),
                ),
                class_name="caja-pregunta-respuesta",    
            ),
            
            input_box(),
            class_name="caja-input-historial",
            ),
            
        ),
    