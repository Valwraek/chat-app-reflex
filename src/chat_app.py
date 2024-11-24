import reflex as rx

def qa(question:str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "Qué es Reflex?",
            "Una manera de contruir ua página web puramente en Python!"
        ),
        (
           "Que puedo hacer?",
           "Cualquier cosa, desde una simple página web hasta una página web compleja!",
        )
    ]
    return rx.box(
        * [
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )
