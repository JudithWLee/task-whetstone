from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, ListItem, ListView, Label

class ToDo(Label):
    def __init__(self, content: str):
        super().__init__(content)
        self.content = content

class BootstrapApp(App):
    CSS_PATH = "to_do_list.tcss"
    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(
            ListItem(ToDo("Implement to do content editing"), id = "one"),
            ListItem(ToDo("Implement adding new to do item"), id = "two"),
            ListItem(ToDo("Implement removing to do item"), id = "three"),
        )
        yield Footer()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """If user clicks on item."""
        event.item.add_class("completed") # event.item = the item user clicked on
        todo = event.item.query_one(ToDo)
        todo.update(f"\[DONE] {todo.content}")

if __name__ == "__main__":
    app = BootstrapApp()
    app.run()
