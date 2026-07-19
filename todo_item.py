from textual.app import ComposeResult
from textual.widgets import ListItem, Label, Input

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

    def on_input_submitted(self, event: Input.Submitted) -> None:
        # Take the string submitted and make it a label
        self.content = event.value
        self.remove_children()
        self.mount(Label(self.content))

        # Hand focus back to parent
        self.parent.focus()
