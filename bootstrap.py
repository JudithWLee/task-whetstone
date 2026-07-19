import re
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header
from todo_item import ToDoItem
from todo_list import ToDoList

class BootstrapApp(App):
    CSS_PATH = "to_do_list.tcss"
    BINDINGS = [
    ]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield ToDoList(
            ToDoItem("Implement inputting stuff into the new input"),
            ToDoItem("Implement turning the input into new to do"),
            ToDoItem("Implement to do content editing"),
            ToDoItem("Refactor bindings into ToDoList"),
        )
        yield Footer()

if __name__ == "__main__":
    app = BootstrapApp()
    app.run()
