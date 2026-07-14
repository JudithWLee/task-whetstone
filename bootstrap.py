from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, ListView, Label, Input

class ToDo(Label):
    def __init__(self, content: str):
        super().__init__(content)
        self.content = content

class VimListView(ListView):
    BINDINGS = [
        ("k", "cursor_up", "Move cursor up"),
        ("j", "cursor_down", "Move cursor down"),
    ]

class BootstrapApp(App):
    CSS_PATH = "to_do_list.tcss"
    BINDINGS = [
        ("d", "delete_to_do", "Delete highlighted to do"),
        ("i", "insert_to_do", "Insert a new to do")
    ]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield VimListView(
            ListItem(ToDo("Implement inputting stuff into the new input")),
            ListItem(ToDo("Implement turning the input into new to do")),
            ListItem(ToDo("Implement to do content editing")),
            ListItem(ToDo("Refactor bindings into VimListView")),
        )
        yield Footer()

    def action_delete_to_do(self) -> None:
        """Delete highlighted to do."""
        to_do_list = self.query_one(ListView)
        if to_do_list.index is not None:
            to_do_list.pop(to_do_list.index)

    def action_insert_to_do(self) -> None:
        """Add new to do."""
        to_do_list = self.query_one(ListView)
        current_index = to_do_list.index
        new_input = Input(placeholder = "New to do item")
        new_to_do = ListItem(new_input)

        to_do_list.insert(current_index, [new_to_do])

        # Update the highlight to the new object
        new_to_do.highlighted = True
        to_do_list.children[current_index+1].highlighted = False

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """If user clicks on item."""
        event.item.add_class("completed") # event.item = the item user clicked on
        todo = event.item.query_one(ToDo)
        todo.update(f"\[DONE] {todo.content}")

if __name__ == "__main__":
    app = BootstrapApp()
    app.run()
