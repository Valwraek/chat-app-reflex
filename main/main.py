import reflex as rx
from .view.chat_app import chat

def index() -> rx.Component:
   return rx.container(
      rx.box(
        chat(),
      ),
      )

app = rx.App(
   stylesheets=[
        "/estilos_chat.css",
    ],
    theme=rx.theme(
        appearance="dark",
    )
)
app.add_page(index)
