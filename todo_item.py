from textual.app import ComposeResult
from textual.widgets import ListItem, Label, Input

class ToDoItem(ListItem):
    def __init__(self, content: str = ""):
        super().__init__()
        self.content = content

    def compose(self) -> ComposeResult:
        yield Label(self.content)

    def select(self) -> None:
        """If user clicks on item."""
        child = self.query_one("*")

        if self.has_class("completed"):
            child.update(child.content.removeprefix("\[DONE] "))
        else:
            child.update(f"\[DONE] {child.content}")

        self.toggle_class("completed")

    def edit(self) -> None:
        child = self.query_one("*")

        self.remove_children()
        input_box = Input(value = self.content)
        self.mount(input_box)
        input_box.focus()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        # Take the string submitted and make it a label
        self.content = event.value
        self.remove_children()
        self.mount(Label(self.content))

        # Hand focus back to parent
        self.parent.focus()
