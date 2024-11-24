import reflex as rx

def input_box() -> rx.Component:
    return (
        rx.input(placeholder="Haz tu pregunta"),
    )