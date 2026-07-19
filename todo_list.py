from textual.widgets import ListView
from todo_item import ToDoItem

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
