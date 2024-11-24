import reflex as rx
from .model.datos_chat_app import datos_chat
from .view.chat_app import chat

def index() -> rx.Component:
   return rx.container(
      chat(),
      )

app = rx.App()
app.add_page(index)
