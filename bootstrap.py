import re
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, ListView, Label, Input
from textual.css.query import NoMatches

class ToDoItem(ListItem):
    def __init__(self, content: str = None):
        super().__init__()
        self.content = content

    def compose(self) -> ComposeResult:
        if self.content is not None:
            yield Label(self.content)
        else:
            yield Input(placeholder = "New to do item")

    def select(self) -> None:
        """If user clicks on item."""
        child = self.query_one("*")

        if isinstance(child, Label):
            if self.has_class("completed"):
                child.update(child.content.removeprefix("\[DONE] "))
            else:
                child.update(f"\[DONE] {child.content}")

            self.toggle_class("completed")
        elif isinstance(child, Input):
            child.focus()
        else:
            self.log("Child type not supported yet, plz implement")

    def submit_content(self) -> None:
        pass

class ToDoList(ListView):
    BINDINGS = [
        ("k", "cursor_up", "Move cursor up"),
        ("j", "cursor_down", "Move cursor down"),
        ("d", "delete_to_do", "Delete highlighted to do"),
        ("i", "insert_to_do", "Insert a new to do"),
    ]

    def action_delete_to_do(self) -> None:
        """Delete highlighted to do."""
        if self.index is not None:
            self.pop(self.index)

    def action_insert_to_do(self) -> None:
        """Add new to do."""
        current_index = self.index
        new_to_do = ToDoItem()

        self.insert(current_index, [new_to_do])

        # Update the highlight to the new object
        new_to_do.highlighted = True
        self.children[current_index+1].highlighted = False

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """If user clicks on item."""
        event.item.select()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        # Take the string submitted
        input_value = event.value

        current_index = self.index
        # Remove the item being selected
        self.pop(current_index)
        # Insert new to do
        new_to_do = ToDoItem(input_value)
        self.insert(current_index, [new_to_do])
        new_to_do.highlighted == True

        self.focus()

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
