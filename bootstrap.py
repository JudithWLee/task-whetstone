from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, ListView, Label

class ToDo(Label):
    def __init__(self, content: str):
        super().__init__(content)
        self.content = content

class BootstrapApp(App):
    CSS_PATH = "to_do_list.tcss"
    BINDINGS = [("d", "delete_to_do", "Delete highlighted to do")]

    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(
            ListItem(ToDo("Implement temporary input widget in ListView")),
            ListItem(ToDo("Implement adding new to do item")),
            ListItem(ToDo("Implement to do content editing")),
        )
        yield Footer()

    def action_delete_to_do(self) -> None:
        """Delete highlighted to do."""
        to_do_list = self.query_one(ListView)
        if to_do_list.index is not None:
            to_do_list.pop(to_do_list.index)

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """If user clicks on item."""
        event.item.add_class("completed") # event.item = the item user clicked on
        todo = event.item.query_one(ToDo)
        todo.update(f"\[DONE] {todo.content}")

if __name__ == "__main__":
    app = BootstrapApp()
    app.run()
