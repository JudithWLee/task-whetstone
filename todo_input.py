from textual.widgets import Input

class ToDoInput(Input):
    BINDINGS = [
        ("escape", "submit", "exit edit mode")
    ]

    def action_submit(self) -> None:
        self.post_message(Input.Submitted(self, self.value))
