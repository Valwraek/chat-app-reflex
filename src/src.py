import reflex as rx
from src.chat_app import chat

def index() -> rx.Component:
   return rx.container(chat())

app = rx.App()
app.add_page(index)
