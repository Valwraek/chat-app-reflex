import reflex as rx


def datos_chat() -> rx.Component:
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
    return qa_pairs


