import reflex as rx
from ..styles import chat_style as cs
 
def input_box() -> rx.Component:
    return (
        rx.input(
            placeholder="Haz tu pregunta",
            style= cs.input_style,
            ),       
    )