from textual.widgets import ListView
from todo_item import ToDoItem

class ToDoList(ListView):
    BINDINGS = [
        ("k", "cursor_up", "Move cursor up"),
        ("j", "cursor_down", "Move cursor down"),
        ("d", "delete_todo", "Delete highlighted to do"),
        ("O", "insert_todo_above", "Insert a new to do above"),
        ("o", "insert_todo_below", "Insert a new to do below"),
        ("i", "edit_todo", "input/edit to do"),
    ]

    def action_delete_todo(self) -> None:
        """Delete highlighted to do."""
        if self.index is not None:
            self.pop(self.index)

    def _insert_todo(self, new_todo_index: int, old_todo_index: int) -> None:
        """Add new to do."""
        new_todo = ToDoItem()

        self.insert(new_todo_index, [new_todo])

        # Update the highlight to the new object
        new_todo.highlighted = True
        self.children[old_todo_index].highlighted = False
        self.index = new_todo_index

    def action_insert_todo_above(self) -> None:
        new_todo_index = self.index
        old_todo_index = self.index + 1
        self._insert_todo(new_todo_index, old_todo_index)

    def action_insert_todo_below(self) -> None:
        new_todo_index = self.index + 1
        old_todo_index = self.index
        self._insert_todo(new_todo_index, old_todo_index)

    def action_edit_todo(self) -> None:
        self.children[self.index].edit()

    def on_list_view_selected(self, event: ListView.Selected) -> None:
        """If user clicks on item."""
        event.item.select()
